#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "click",
#     "html2text",
#     "markdown",
#     "beautifulsoup4"
# ]
# ///
"""
==============================================================================
Script: sync_wordpress_md.py
Version: 1.0.0
Author: lalitaalaalitah
Website: https://www.lalitaalaalitah.com
GitHub: https://github.com/lalitaalaalitah
Description: Pulls remote WordPress post/page content, compares with local 
             Markdown document (.md), merges changes cohesively preserving 
             critical notes, links, formatting, and syncs bidirectionally.
==============================================================================
"""

import sys
import os
import re
import json
import base64
import subprocess
import difflib
import click
import html2text
import markdown
from bs4 import BeautifulSoup

__version__ = "1.0.0"
AUTHOR = "lalitaalaalitah"
WEBSITE = "https://www.lalitaalaalitah.com"
GITHUB = "https://github.com/lalitaalaalitah"

# Catppuccin Mocha Truecolor Palette
CLR_RESET = "\033[0;48;2;30;30;46;38;2;205;214;244m"
BG_BASE = "\033[48;2;30;30;46m"
FG_TEXT = "\033[38;2;205;214;244m"
FG_GREEN = "\033[38;2;166;227;161m"
FG_MAUVE = "\033[38;2;203;166;247m"
FG_PEACH = "\033[38;2;250;179;135m"
FG_RED = "\033[38;2;243;139;168m"
FG_BLUE = "\033[38;2;137;180;250m"

SSH_HOST = "user@hostname_or_ip"
SSH_KEY = "~/.ssh/id_ed25519"
SSH_PORT = "65002"

def print_banner():
    banner = f"""{BG_BASE}{FG_MAUVE}================================================={CLR_RESET}
{BG_BASE}{FG_GREEN}   WordPress <-> Markdown Cohesive Sync Tool{CLR_RESET}
{BG_BASE}{FG_TEXT}   Author:  {FG_PEACH}{AUTHOR}{CLR_RESET}
{BG_BASE}{FG_TEXT}   Website: {FG_PEACH}{WEBSITE}{CLR_RESET}
{BG_BASE}{FG_TEXT}   GitHub:  {FG_PEACH}{GITHUB}{CLR_RESET}
{BG_BASE}{FG_TEXT}   Version: {FG_PEACH}{__version__}{CLR_RESET}
{BG_BASE}{FG_MAUVE}================================================={CLR_RESET}"""
    click.echo(banner)

def pull_remote_post(domain, slug=None, post_id=0):
    """Pulls WordPress post or page content via SSH remote PHP execution."""
    if not slug and not post_id:
        click.echo(f"{BG_BASE}{FG_RED}Error: Must provide either --slug or --post-id{CLR_RESET}")
        sys.exit(1)

    php_fetch_script = f"""define('WP_USE_THEMES', false);
require_once('domains/{domain}/public_html/wp-load.php');

$post = null;
if ({post_id} > 0) {{
    $post = get_post({post_id});
}} else if (!empty('{slug}')) {{
    $post = get_page_by_path('{slug}', OBJECT, array('post', 'page'));
    if (!$post) {{
        $posts = get_posts(array('name' => '{slug}', 'post_type' => 'any', 'posts_per_page' => 1));
        if (!empty($posts)) {{
            $post = $posts[0];
        }}
    }}
}}

if (!$post) {{
    echo 'JSON_RESULT:' . json_encode(array('error' => 'Post not found on site {domain}'));
}} else {{
    $cats = wp_get_post_categories($post->ID, array('fields' => 'names'));
    $tags = wp_get_post_tags($post->ID, array('fields' => 'names'));
    $result = array(
        'success'    => true,
        'id'         => $post->ID,
        'title'      => $post->post_title,
        'content'    => $post->post_content,
        'slug'       => $post->post_name,
        'status'     => $post->post_status,
        'type'       => $post->post_type,
        'modified'   => $post->post_modified,
        'categories' => $cats,
        'tags'       => $tags,
        'permalink'  => get_permalink($post->ID)
    );
    echo 'JSON_RESULT:' . json_encode($result);
}}
"""

    b64_php = base64.b64encode(php_fetch_script.encode("utf-8")).decode("ascii")
    remote_command = f"php -r 'eval(base64_decode(\"{b64_php}\"));'"

    ssh_cmd = [
        "ssh",
        "-p", SSH_PORT,
        "-i", SSH_KEY,
        "-o", "StrictHostKeyChecking=accept-new",
        SSH_HOST,
        remote_command
    ]

    click.echo(f"\n{BG_BASE}{FG_MAUVE}[*] Pulling remote content from {domain} via SSH...{CLR_RESET}")
    result = subprocess.run(ssh_cmd, capture_output=True, text=True)

    if result.returncode != 0:
        click.echo(f"{BG_BASE}{FG_RED}SSH execution failed: {result.stderr}{CLR_RESET}")
        sys.exit(1)

    json_str = None
    for line in result.stdout.splitlines():
        if "JSON_RESULT:" in line:
            json_str = line.split("JSON_RESULT:")[1].strip()
            break

    if not json_str:
        click.echo(f"{BG_BASE}{FG_RED}Failed to parse PHP output. Output was:\n{result.stdout}{CLR_RESET}")
        sys.exit(1)

    data = json.loads(json_str)
    if "error" in data:
        click.echo(f"{BG_BASE}{FG_RED}WordPress Error: {data['error']}{CLR_RESET}")
        sys.exit(1)

    return data

def convert_html_to_markdown(html_content):
    """Converts HTML / Gutenberg markup to clean Markdown."""
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.single_line_break = False
    md = h.handle(html_content)
    # Clean trailing spaces and excessive blank lines
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    return md

def merge_markdown_cohesively(local_md, remote_md, title=None):
    """Smartly merges remote and local Markdown documents cohesively."""
    local_lines = local_md.splitlines()
    remote_lines = remote_md.splitlines()

    seen_headers = set()
    for line in local_lines:
        if line.startswith("#"):
            seen_headers.add(line.strip())

    merged_md = local_md.strip()

    # Find unique remote sections (e.g. historical quotes or signature lines not in local)
    missing_remote_parts = []
    in_unique_block = False
    current_unique = []

    for line in remote_lines:
        if line.startswith("#"):
            if current_unique:
                missing_remote_parts.append("\n".join(current_unique))
                current_unique = []
            if line.strip() not in seen_headers:
                in_unique_block = True
                current_unique.append(line)
            else:
                in_unique_block = False
        elif in_unique_block:
            current_unique.append(line)

    if current_unique:
        missing_remote_parts.append("\n".join(current_unique))

    if missing_remote_parts:
        merged_md += "\n\n---\n\n## Additional Synchronized Content\n\n" + "\n\n".join(missing_remote_parts)

    return merged_md.strip()

def push_updated_post(domain, post_id, title, slug, status, content_md, categories=None, tags=None):
    """Pushes merged cohesive Markdown content back to WordPress site."""
    # Convert Markdown to HTML for WordPress post_content
    html_content = markdown.markdown(content_md, extensions=['extra', 'codehilite', 'tables', 'fenced_code'])

    b64_title = base64.b64encode(title.encode("utf-8")).decode("ascii")
    b64_content = base64.b64encode(html_content.encode("utf-8")).decode("ascii")
    b64_categories = base64.b64encode(json.dumps(categories).encode("utf-8")).decode("ascii") if categories else ""
    b64_tags = base64.b64encode(json.dumps(tags).encode("utf-8")).decode("ascii") if tags else ""

    php_update_script = f"""define('WP_USE_THEMES', false);
require_once('domains/{domain}/public_html/wp-load.php');

$title = base64_decode('{b64_title}');
$content = base64_decode('{b64_content}');

$post_data = array(
    'ID'           => {post_id},
    'post_title'   => $title,
    'post_content' => $content,
    'post_status'  => '{status}',
    'post_name'    => '{slug}'
);

$res = wp_update_post($post_data);
if (is_wp_error($res)) {{
    echo 'JSON_RESULT:' . json_encode(array('error' => $res->get_error_message()));
}} else {{
    $b64_cats = '{b64_categories}';
    if (!empty($b64_cats)) {{
        $cat_list = json_decode(base64_decode($b64_cats), true);
        if (is_array($cat_list)) {{
            $cat_ids = array();
            foreach ($cat_list as $cat_name) {{
                $term = get_term_by('name', $cat_name, 'category');
                if (!$term) {{
                    $created = wp_insert_term($cat_name, 'category');
                    if (!is_wp_error($created) && isset($created['term_id'])) {{
                        $cat_ids[] = (int)$created['term_id'];
                    }}
                }} else {{
                    $cat_ids[] = (int)$term->term_id;
                }}
            }}
            if (!empty($cat_ids)) {{
                wp_set_post_categories({post_id}, $cat_ids);
            }}
        }}
    }}
    echo 'JSON_RESULT:' . json_encode(array('success' => true, 'post_id' => {post_id}, 'url' => get_permalink({post_id})));
}}
"""

    b64_php = base64.b64encode(php_update_script.encode("utf-8")).decode("ascii")
    remote_command = f"php -r 'eval(base64_decode(\"{b64_php}\"));'"

    ssh_cmd = [
        "ssh",
        "-p", SSH_PORT,
        "-i", SSH_KEY,
        "-o", "StrictHostKeyChecking=accept-new",
        SSH_HOST,
        remote_command
    ]

    click.echo(f"\n{BG_BASE}{FG_GREEN}[*] Updating remote post ID {post_id} on {domain}...{CLR_RESET}")
    result = subprocess.run(ssh_cmd, capture_output=True, text=True)

    if result.returncode != 0:
        click.echo(f"{BG_BASE}{FG_RED}SSH execution failed: {result.stderr}{CLR_RESET}")
        sys.exit(1)

    json_str = None
    for line in result.stdout.splitlines():
        if "JSON_RESULT:" in line:
            json_str = line.split("JSON_RESULT:")[1].strip()
            break

    if not json_str:
        click.echo(f"{BG_BASE}{FG_RED}Failed to parse PHP update output:\n{result.stdout}{CLR_RESET}")
        sys.exit(1)

    data = json.loads(json_str)
    if "error" in data:
        click.echo(f"{BG_BASE}{FG_RED}Update Error: {data['error']}{CLR_RESET}")
        sys.exit(1)

    click.echo(f"{BG_BASE}{FG_GREEN}[✓] Successfully updated remote post! URL: {data['url']}{CLR_RESET}")

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--domain', required=True, help='WordPress domain (e.g. code.lalitaalaalitah.com)')
@click.option('--slug', default=None, help='WordPress post/page slug')
@click.option('--post-id', default=0, type=int, help='WordPress post/page ID')
@click.option('--local-file', required=True, type=click.Path(exists=True), help='Path to local Markdown (.md) file')
@click.option('--sync/--no-sync', default=True, help='Bidirectional sync mode (merge and update both remote & local)')
@click.option('--dry-run', is_flag=True, help='Preview diff and merge without updating remote or local')
@click.option('--version', is_flag=True, help='Show script version and exit')
def main(domain, slug, post_id, local_file, sync, dry_run, version):
    """Pulls WordPress post, compares with local Markdown, merges cohesively, and syncs."""
    print_banner()

    if version:
        sys.exit(0)

    # 1. Pull Remote Post
    remote_data = pull_remote_post(domain, slug=slug, post_id=post_id)

    click.echo(f"\n{BG_BASE}{FG_GREEN}[✓] Remote Post Retrieved:{CLR_RESET}")
    click.echo(f"{BG_BASE}{FG_TEXT}  - ID: {remote_data['id']}{CLR_RESET}")
    click.echo(f"{BG_BASE}{FG_TEXT}  - Title: {remote_data['title']}{CLR_RESET}")
    click.echo(f"{BG_BASE}{FG_TEXT}  - Slug: {remote_data['slug']}{CLR_RESET}")
    click.echo(f"{BG_BASE}{FG_TEXT}  - Modified: {remote_data['modified']}{CLR_RESET}")
    click.echo(f"{BG_BASE}{FG_TEXT}  - Permalink: {remote_data['permalink']}{CLR_RESET}")

    # 2. Read Local Markdown
    with open(local_file, "r", encoding="utf-8") as f:
        local_md = f.read()

    # 3. Convert Remote HTML to Markdown
    remote_md = convert_html_to_markdown(remote_data['content'])

    # 4. Display Diff Preview
    click.echo(f"\n{BG_BASE}{FG_BLUE}[*] Diff Preview (Local vs Remote):{CLR_RESET}")
    diff = difflib.unified_diff(
        remote_md.splitlines(),
        local_md.splitlines(),
        fromfile='remote_wordpress',
        tofile='local_markdown',
        lineterm=''
    )
    diff_lines = list(diff)
    if not diff_lines:
        click.echo(f"{BG_BASE}{FG_GREEN}[✓] Local file and remote WordPress post are in perfect sync!{CLR_RESET}")
    else:
        for line in diff_lines[:30]:  # Show first 30 lines of diff
            if line.startswith('+'):
                click.echo(f"{BG_BASE}{FG_GREEN}{line}{CLR_RESET}")
            elif line.startswith('-'):
                click.echo(f"{BG_BASE}{FG_RED}{line}{CLR_RESET}")
            else:
                click.echo(f"{BG_BASE}{FG_TEXT}{line}{CLR_RESET}")
        if len(diff_lines) > 30:
            click.echo(f"{BG_BASE}{FG_PEACH}... ({len(diff_lines) - 30} more diff lines truncated){CLR_RESET}")

    # 5. Perform Cohesive Merge
    cohesive_md = merge_markdown_cohesively(local_md, remote_md, title=remote_data['title'])

    if dry_run:
        click.echo(f"\n{BG_BASE}{FG_PEACH}[DRY RUN] Cohesive merge complete. No files updated.{CLR_RESET}")
        return

    # 6. Update Local File
    if sync:
        with open(local_file, "w", encoding="utf-8") as f:
            f.write(cohesive_md)
        click.echo(f"{BG_BASE}{FG_GREEN}[✓] Updated local Markdown file: {local_file}{CLR_RESET}")

        # 7. Push Updated Merged Content back to WordPress
        push_updated_post(
            domain=domain,
            post_id=remote_data['id'],
            title=remote_data['title'],
            slug=remote_data['slug'],
            status=remote_data['status'],
            content_md=cohesive_md,
            categories=remote_data.get('categories'),
            tags=remote_data.get('tags')
        )

if __name__ == '__main__':
    main()
