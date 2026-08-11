#!/usr/bin/env python3
"""
medhA Keyboard Layout Multi-Platform Packaging Tool
===================================================
Author       : lalitaalaalitah
Website      : https://www.lalitaalaalitah.com
GitHub       : https://github.com/lalitaalaalitah
Version      : 1.1.0
Description  : Packages macOS (DMG format with drag-and-drop hints), Linux, and Windows editions of medhA keyboard layout.
"""

import os
import sys
import shutil
import argparse
import subprocess
import tarfile
import zipfile
from pathlib import Path

__version__ = "1.1.0"
__author__ = "lalitaalaalitah"
__website__ = "https://www.lalitaalaalitah.com"
__github__ = "https://github.com/lalitaalaalitah"

# Catppuccin Mocha ANSI Palette
CLR_RESET = "\033[0;48;2;30;30;46;38;2;205;214;244m"
BG_BASE = "\033[48;2;30;30;46m"
FG_TEXT = "\033[38;2;205;214;244m"
FG_LAVENDER = "\033[38;2;180;190;254m"
FG_GREEN = "\033[38;2;166;227;161m"
FG_YELLOW = "\033[38;2;249;226;175m"
FG_RED = "\033[38;2;243;139;168m"
FG_BLUE = "\033[38;2;137;180;250m"


def print_banner():
    print(f"{BG_BASE}{FG_LAVENDER}")
    print("=================================================================")
    print("         medhA Keyboard Layout Packaging Utility                 ")
    print(f"                       Version: {__version__}                   ")
    print(f"      Author: {__author__} | {__website__}")
    print("=================================================================")
    print(f"{CLR_RESET}")


def package_mac_dmg(repo_root: Path, out_dir: Path) -> Path:
    mac_dir = repo_root / "MacOS"
    out_dmg = out_dir / "medhA-keyboard-macOS.dmg"
    dmg_stage = out_dir / "macOS_dmg_stage"

    print(f"{FG_TEXT}Packaging macOS DMG -> {FG_YELLOW}{out_dmg.name}{CLR_RESET}")

    if dmg_stage.exists():
        shutil.rmtree(dmg_stage)
    dmg_stage.mkdir(parents=True, exist_ok=True)

    # 1. Copy bundles into staging folder
    bundle_17 = mac_dir / "medhA-macOSX-v_1.7.bundle"
    bundle_16 = mac_dir / "medhA_1.6_working.bundle"

    if bundle_17.exists():
        shutil.copytree(bundle_17, dmg_stage / bundle_17.name)
    if bundle_16.exists():
        shutil.copytree(bundle_16, dmg_stage / bundle_16.name)

    # 2. Create Drag-and-Drop Symlinks to Keyboard Layouts directories
    # System-wide install directory (/Library/Keyboard Layouts)
    system_kb_symlink = dmg_stage / "System Keyboard Layouts"
    if not system_kb_symlink.exists():
        os.symlink("/Library/Keyboard Layouts", system_kb_symlink)

    # Per-user install directory (~/Library/Keyboard Layouts)
    user_kb_path = os.path.expanduser("~/Library/Keyboard Layouts")
    user_kb_symlink = dmg_stage / "User Keyboard Layouts"
    if not user_kb_symlink.exists():
        os.symlink(user_kb_path, user_kb_symlink)

    # 3. Add clear drag-and-drop instruction file
    instructions = (
        "medhA Sanskrit Keyboard Layout Installation Instructions:\n"
        "=========================================================\n\n"
        "1. Drag 'medhA-macOSX-v_1.7.bundle' (or 'medhA_1.6_working.bundle') into either:\n"
        "   - 'User Keyboard Layouts' (Install for current user: ~/Library/Keyboard Layouts)\n"
        "   - 'System Keyboard Layouts' (Install for all users: /Library/Keyboard Layouts)\n\n"
        "2. Open System Settings -> Keyboard -> Input Sources.\n"
        "3. Click '+' (Add Input Source), search for Sanskrit or English (US), and select 'medhA'.\n\n"
        "Author: lalitaalaalitah | https://www.lalitaalaalitah.com\n"
    )
    with open(dmg_stage / "INSTALL_INSTRUCTIONS.txt", "w", encoding="utf-8") as f:
        f.write(instructions)

    if out_dmg.exists():
        out_dmg.unlink()

    # 4. Build DMG using hdiutil if available (macOS)
    if shutil.which("hdiutil"):
        cmd = [
            "hdiutil",
            "create",
            "-volname",
            "medhA Keyboard Layout",
            "-srcfolder",
            str(dmg_stage),
            "-ov",
            "-format",
            "UDZO",
            str(out_dmg),
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode != 0:
            print(f"{FG_RED}Error running hdiutil: {res.stderr}{CLR_RESET}")
            sys.exit(res.returncode)
        print(f"{FG_GREEN}   [OK] Generated DMG: {out_dmg}{CLR_RESET}")
    else:
        print(f"{FG_YELLOW}   [WARN] 'hdiutil' not found (non-macOS system). Creating fallback ZIP for macOS files.{CLR_RESET}")
        out_zip = out_dir / "medhA-keyboard-macOS.zip"
        with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(dmg_stage):
                for file in files:
                    file_path = Path(root) / file
                    rel_path = file_path.relative_to(dmg_stage)
                    zf.write(file_path, rel_path)
        print(f"{FG_GREEN}   [OK] Generated Fallback ZIP: {out_zip}{CLR_RESET}")

    # Cleanup temporary staging directory
    shutil.rmtree(dmg_stage, ignore_errors=True)
    return out_dmg


def package_linux(repo_root: Path, out_dir: Path) -> Path:
    linux_dir = repo_root / "Linux"
    out_tar = out_dir / "medhA-keyboard-Linux.tar.gz"

    print(f"{FG_TEXT}Packaging Linux edition -> {FG_YELLOW}{out_tar.name}{CLR_RESET}")
    with tarfile.open(out_tar, "w:gz") as tf:
        for root, dirs, files in os.walk(linux_dir):
            for file in files:
                if file.startswith(".DS_Store"):
                    continue
                file_path = Path(root) / file
                rel_path = Path("Linux") / file_path.relative_to(linux_dir)
                tf.add(file_path, arcname=rel_path)

    print(f"{FG_GREEN}   [OK] Generated {out_tar}{CLR_RESET}")
    return out_tar


def package_windows(repo_root: Path, out_dir: Path) -> Path:
    win_dir = repo_root / "Windows"
    out_zip = out_dir / "medhA-keyboard-Windows.zip"

    print(f"{FG_TEXT}Packaging Windows edition -> {FG_YELLOW}{out_zip.name}{CLR_RESET}")
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(win_dir):
            for file in files:
                if file.startswith(".DS_Store"):
                    continue
                file_path = Path(root) / file
                rel_path = Path("Windows") / file_path.relative_to(win_dir)
                zf.write(file_path, rel_path)

    print(f"{FG_GREEN}   [OK] Generated {out_zip}{CLR_RESET}")
    return out_zip


def package_all_combined(repo_root: Path, out_dir: Path) -> Path:
    out_zip = out_dir / "medhA-keyboard-All-Platforms.zip"

    print(f"{FG_TEXT}Packaging All-in-One archive -> {FG_YELLOW}{out_zip.name}{CLR_RESET}")
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for platform in ["MacOS", "Linux", "Windows"]:
            p_dir = repo_root / platform
            if not p_dir.exists():
                continue
            for root, dirs, files in os.walk(p_dir):
                for file in files:
                    if file.startswith(".DS_Store"):
                        continue
                    file_path = Path(root) / file
                    rel_path = file_path.relative_to(repo_root)
                    zf.write(file_path, rel_path)

        # Add root README.md & HOW_TO_USE.md if present
        for doc_name in ["README.md", "HOW_TO_USE.md"]:
            doc_path = repo_root / doc_name
            if doc_path.exists():
                zf.write(doc_path, doc_name)

    print(f"{FG_GREEN}   [OK] Generated {out_zip}{CLR_RESET}")
    return out_zip


def main():
    parser = argparse.ArgumentParser(
        description=f"medhA Keyboard Packaging Utility v{__version__} by {__author__} ({__website__})"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"medhA Keyboard Packaging Tool v{__version__} by {__author__} ({__website__})",
    )
    parser.add_argument(
        "--platform",
        choices=["all", "mac", "linux", "windows"],
        default="all",
        help="Target platform to package (default: all)",
    )
    parser.add_argument(
        "--outdir",
        default="dist",
        help="Output directory for generated archives (default: dist)",
    )

    args = parser.parse_args()

    print_banner()

    repo_root = Path(__file__).resolve().parent.parent
    out_dir = repo_root / args.outdir
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"{FG_BLUE}Repository Root : {repo_root}{CLR_RESET}")
    print(f"{FG_BLUE}Output Directory: {out_dir}{CLR_RESET}\n")

    if args.platform in ["mac", "all"]:
        package_mac_dmg(repo_root, out_dir)
    if args.platform in ["linux", "all"]:
        package_linux(repo_root, out_dir)
    if args.platform in ["windows", "all"]:
        package_windows(repo_root, out_dir)
    if args.platform == "all":
        package_all_combined(repo_root, out_dir)

    print(f"\n{FG_GREEN}Packaging completed successfully! Artifacts saved in {out_dir}{CLR_RESET}")


if __name__ == "__main__":
    main()
