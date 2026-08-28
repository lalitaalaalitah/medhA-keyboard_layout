# How to Maintain Website Pages & Release Posts (Hub & Spoke Architecture)

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**GitHub**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

[← Back to Main README Overview](../README.md) | [How To Use Guide](../HOW_TO_USE.md) | [Release Standards](../RELEASE_STANDARDS.md)

> 📌 **Website Publication Directive**: This document is the master specification that guides all content creation, layout structuring, and post updates for **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)**.

---

## 1. Executive Summary & Problem Statement

When releasing software updates or new keyboard layout versions, publishing a static blog post with installation instructions creates a long-term SEO and maintenance trap:
* **The Problem**: Over time, search engines point beginners (noobs) to old blog posts (e.g., *v1.2 Release & Setup*), leading to outdated installation steps, dead links, or broken procedures.
* **The Solution**: Separate **Evergreen Documentation (Hubs)** from **Release Announcements (Spokes)**.

---

## 2. Hub & Spoke Architecture

```
                         ┌──────────────────────────────────────────────┐
  [ Release Post v1.0 ] ─►│  EVERGREEN MASTER GUIDE (Canonical Hub)      │
  [ Release Post v1.5 ] ─►│  URL: /docs/medha-keyboard-master-guide       │
  [ Release Post v2.0 ] ─►│  - Always updated with the latest release    │
                         │  - Step-by-Step Installation & Layout Map   │
                         └──────────────────────────────────────────────┘
```

### 2.1 The Hub (Evergreen Master Guide)
* **Permalink URL**: Use a fixed, un-versioned URL (e.g., `/docs/medha-keyboard-master-guide` or `/docs/macos-medha-installation`).
* **Content**: The single source of truth for installation, layout maps, key bindings, and troubleshooting.
* **Update Frequency**: Updated continuously on every software release.
* **Target Audience**: Beginners, new installers, and search engine (SEO) landing traffic.

### 2.2 The Spokes (Release Announcements & Blog Posts)
* **Permalink URL**: Use dated or versioned URLs (e.g., `/blog/2026/08/medha-keyboard-v2-release` or `/changelog/v2.0.0`).
* **Content**: Historical point-in-time record of what changed, release notes, and backstory.
* **Update Frequency**: Written once and archived (immutable).
* **Target Audience**: Existing users, subscribers, and developers tracking changelogs.

---

## 3. Implementation Rules & Best Practices

### Rule 1: Canonical Living Pages
Never put version numbers in the URL path of primary guides or installation manuals.
* ❌ **Bad URL**: `https://www.lalitaalaalitah.com/blog/medha-keyboard-v1.7-install`
* ✅ **Good URL**: `https://www.lalitaalaalitah.com/docs/macos-medha-installation`

### Rule 2: Top Metadata Banner on Master Guide
Every living guide must feature a prominent header block indicating its current compatibility:

```markdown
> 🟢 **Current Version**: `v2.1.0` | **Last Updated**: August 28, 2026 | [View Full Changelog](/changelog)
```

### Rule 3: Top Notice Banner on Historical Blog Posts
Every release post or blog article MUST contain a mandatory top alert redirecting new users to the Master Guide:

```markdown
> [!IMPORTANT]
> **Looking for setup instructions?**  
> This post covers the historical release highlights for **v1.7.0**. For the latest up-to-date installation instructions and layout guide, please visit the **[medhA Keyboard Master Guide](/docs/medha-keyboard-master-guide)**.
```

### Rule 4: "What's New" Section in the Living Guide
Keep a short "What's New in `vX.Y.Z`" section inside the Master Guide that links back to the full Release Announcement for context.

---

## 4. Step-by-Step Release Maintenance Workflow

When publishing a new release (e.g., `v2.0.0`):

1. **Update Living Guides**:
   - Update `01_medhA_Sanskrit_Keyboard_Master_Guide_Improved.md` and OS-specific setup guides with new download links, bundle changes, or key mappings.
   - Update the top metadata banner (`Current Version: v2.0.0`).

2. **Publish Release Post**:
   - Create the new blog post or release announcement (`medha-keyboard-v2.0.0-release.md`).
   - Add the mandatory **Rule 3 Notice Banner** at the top of the post linking to the Master Guide.

3. **Verify SEO & Internal Links**:
   - Ensure all internal links on the site point to the canonical guide URLs (`/docs/...`).

4. **Git & Repository Sync**:
   - Commit documentation updates along with code releases.
   - Tag the release (`v2.0.0`) and trigger CI/CD packaging pipelines.

---

## 5. Bidirectional Markdown <-> WordPress Sync Tool

To automatically pull remote post content from **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)** (or any site in the network), compare it with local repository `.md` files, perform a cohesive merge retaining historical notes, and update both local files and remote WordPress posts simultaneously:

### 5.1 CLI Tool Location
- Repository script: **`scripts/sync_wordpress_md.py`**
- Centralized helper tool: **`website_manipulation_helpers/post_sync/sync_wordpress_md.py`**

### 5.2 Command Examples

```bash
# 1. Preview changes and cohesive diff (dry-run mode)
uv run scripts/sync_wordpress_md.py \
  --domain code.lalitaalaalitah.com \
  --slug medha-6-unicode-sanskrit-keyboard-layou \
  --local-file docs/posts/01_Windows_medhA_Keyboard_Installation_Guide.md \
  --dry-run

# 2. Perform live bidirectional sync (updates local .md and remote WordPress post)
uv run scripts/sync_wordpress_md.py \
  --domain code.lalitaalaalitah.com \
  --slug medha-mac-os \
  --local-file docs/posts/01_macOS_medhA_Keyboard_Installation_Guide.md \
  --sync
```

---

## Navigation Links

- 🏠 **[Main Overview & Landing Page](../README.md)**
- ⚡ **[Quick Command Summary](../README.md#quick-command-summary)**
- 📖 **[How To Use Guide](../HOW_TO_USE.md)**
- 📋 **[Release Standards & Tap Workflow](../RELEASE_STANDARDS.md)**
- 🗺️ **[Documentation Plan](DOCUMENTATION_PLAN.md)**
