#!/usr/bin/env python3
"""
medhA Keyboard Layout Multi-Platform Packaging Tool
===================================================
Author       : lalitaalaalitah
Website      : https://www.lalitaalaalitah.com
GitHub       : https://github.com/lalitaalaalitah
Version      : 1.2.0
Description  : Packages per-version macOS DMGs (with drag-and-drop hints), Linux, and Windows editions of medhA keyboard layout.
"""

import os
import sys
import shutil
import argparse
import subprocess
import tarfile
import zipfile
from pathlib import Path

__version__ = "1.3.0"
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


def _build_single_mac_dmg(bundle_path: Path, ver_label: str, vol_name: str, out_dmg: Path, out_dir: Path):
    if not bundle_path.exists():
        print(f"{FG_YELLOW}   [WARN] Bundle not found: {bundle_path}{CLR_RESET}")
        return

    dmg_stage = out_dir / f"macOS_dmg_stage_{ver_label}"
    if dmg_stage.exists():
        shutil.rmtree(dmg_stage)
    dmg_stage.mkdir(parents=True, exist_ok=True)

    # 1. Copy target bundle with canonical name medhA.bundle for clean in-place replacement
    canonical_bundle_name = "medhA.bundle"
    shutil.copytree(bundle_path, dmg_stage / canonical_bundle_name)

    # 2. Create Drag-and-Drop Symlink to system Keyboard Layouts directory (/Library/Keyboard Layouts)
    kb_symlink = dmg_stage / "Keyboard Layouts"
    if not kb_symlink.exists():
        os.symlink("/Library/Keyboard Layouts", kb_symlink)

    # 3. Add clear drag-and-drop instruction file
    instructions = (
        f"medhA Sanskrit Keyboard Layout ({ver_label}) Installation Instructions:\n"
        "======================================================================\n\n"
        "1. Drag 'medhA.bundle' into the 'Keyboard Layouts' shortcut folder.\n"
        "   If an older version exists, click 'Replace' to upgrade in place.\n"
        "   (This installs the layout to /Library/Keyboard Layouts/medhA.bundle)\n\n"
        "2. UPGRADE NOTE: If you previously installed an older version under a\n"
        "   different filename (such as 'medhA-macOSX.1.5.bundle' or 'medhA-macOSX-v_1.7.bundle'),\n"
        "   please delete those older bundle files from Keyboard Layouts to avoid duplicates.\n\n"
        "3. Open System Settings -> Keyboard -> Input Sources.\n"
        "4. Click '+' (Add Input Source), search for Sanskrit or English (US), and select 'medhA'.\n\n"
        "For complete uninstallation details, see docs/UNINSTALLATION_GUIDE.md\n"
        "Author: lalitaalaalitah | https://www.lalitaalaalitah.com\n"
    )
    with open(dmg_stage / "INSTALL_INSTRUCTIONS.txt", "w", encoding="utf-8") as f:
        f.write(instructions)

    if out_dmg.exists():
        out_dmg.unlink()

    # 4. Build DMG using hdiutil if available
    if shutil.which("hdiutil"):
        cmd = [
            "hdiutil",
            "create",
            "-volname",
            vol_name,
            "-srcfolder",
            str(dmg_stage),
            "-ov",
            "-format",
            "UDZO",
            str(out_dmg),
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode != 0:
            print(f"{FG_RED}Error running hdiutil for {ver_label}: {res.stderr}{CLR_RESET}")
        else:
            print(f"{FG_GREEN}   [OK] Generated DMG ({ver_label}): {out_dmg}{CLR_RESET}")
    else:
        out_zip = out_dir / f"medhA-keyboard-macOS-{ver_label}.zip"
        with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED, strict_timestamps=False) as zf:
            for root, dirs, files in os.walk(dmg_stage):
                for file in files:
                    file_path = Path(root) / file
                    rel_path = file_path.relative_to(dmg_stage)
                    zf.write(file_path, rel_path)
        print(f"{FG_GREEN}   [OK] Generated Fallback ZIP ({ver_label}): {out_zip}{CLR_RESET}")

    shutil.rmtree(dmg_stage, ignore_errors=True)


def package_mac_dmgs(repo_root: Path, out_dir: Path, app_version: str):
    mac_dir = repo_root / "MacOS"
    print(f"{FG_TEXT}Packaging macOS editions into individual DMGs (Version: {app_version})...{CLR_RESET}")

    clean_ver = app_version.lstrip("v")
    ver_label = f"v{clean_ver}"

    # Active Canonical medhA bundle (unversioned for clean in-place updates)
    bundle_curr = mac_dir / "medhA.bundle"
    if not bundle_curr.exists():
        bundle_curr = mac_dir / "medhA_1.7_working.bundle"

    out_dmg_versioned = out_dir / f"medhA-keyboard-macOS-{ver_label}.dmg"
    _build_single_mac_dmg(bundle_curr, ver_label, f"medhA Keyboard {ver_label}", out_dmg_versioned, out_dir)

    # Legacy DMG aliases for reference
    bundle_16 = mac_dir / "medhA_1.6_working.bundle"
    if bundle_16.exists():
        out_dmg_16 = out_dir / "medhA-keyboard-macOS-v1.6.dmg"
        _build_single_mac_dmg(bundle_16, "v1.6", "medhA Keyboard v1.6", out_dmg_16, out_dir)

    # Create unversioned default macOS DMG alias for backwards compatibility
    out_dmg_default = out_dir / "medhA-keyboard-macOS.dmg"
    if out_dmg_versioned.exists():
        if out_dmg_default.exists():
            out_dmg_default.unlink()
        shutil.copy2(out_dmg_versioned, out_dmg_default)
        print(f"{FG_GREEN}   [OK] Generated Default macOS DMG ({ver_label} alias): {out_dmg_default}{CLR_RESET}")


def package_linux(repo_root: Path, out_dir: Path, app_version: str) -> Path:
    clean_ver = app_version.lstrip("v")
    linux_dir = repo_root / "Linux"
    out_tar_ver = out_dir / f"medhA-keyboard-Linux-v{clean_ver}.tar.gz"
    out_tar_default = out_dir / "medhA-keyboard-Linux.tar.gz"

    print(f"{FG_TEXT}Packaging Linux edition -> {FG_YELLOW}{out_tar_ver.name}{CLR_RESET}")
    with tarfile.open(out_tar_ver, "w:gz") as tf:
        for root, dirs, files in os.walk(linux_dir):
            for file in files:
                if file.startswith(".DS_Store"):
                    continue
                file_path = Path(root) / file
                rel_path = Path("Linux") / file_path.relative_to(linux_dir)
                tf.add(file_path, arcname=rel_path)

    if out_tar_default.exists():
        out_tar_default.unlink()
    shutil.copy2(out_tar_ver, out_tar_default)

    print(f"{FG_GREEN}   [OK] Generated {out_tar_ver}{CLR_RESET}")
    return out_tar_ver


def package_windows(repo_root: Path, out_dir: Path, app_version: str) -> Path:
    clean_ver = app_version.lstrip("v")
    win_dir = repo_root / "Windows"
    out_zip_ver = out_dir / f"medhA-keyboard-Windows-v{clean_ver}.zip"
    out_zip_default = out_dir / "medhA-keyboard-Windows.zip"

    print(f"{FG_TEXT}Packaging Windows edition -> {FG_YELLOW}{out_zip_ver.name}{CLR_RESET}")
    with zipfile.ZipFile(out_zip_ver, "w", zipfile.ZIP_DEFLATED, strict_timestamps=False) as zf:
        for root, dirs, files in os.walk(win_dir):
            for file in files:
                if file.startswith(".DS_Store"):
                    continue
                file_path = Path(root) / file
                rel_path = Path("Windows") / file_path.relative_to(win_dir)
                zf.write(file_path, rel_path)

    if out_zip_default.exists():
        out_zip_default.unlink()
    shutil.copy2(out_zip_ver, out_zip_default)

    print(f"{FG_GREEN}   [OK] Generated {out_zip_ver}{CLR_RESET}")
    return out_zip_ver


def package_all_combined(repo_root: Path, out_dir: Path, app_version: str) -> Path:
    clean_ver = app_version.lstrip("v")
    out_zip_ver = out_dir / f"medhA-keyboard-All-Platforms-v{clean_ver}.zip"
    out_zip_default = out_dir / "medhA-keyboard-All-Platforms.zip"

    print(f"{FG_TEXT}Packaging All-in-One archive -> {FG_YELLOW}{out_zip_ver.name}{CLR_RESET}")
    with zipfile.ZipFile(out_zip_ver, "w", zipfile.ZIP_DEFLATED, strict_timestamps=False) as zf:
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

        for doc_name in ["README.md", "HOW_TO_USE.md"]:
            doc_path = repo_root / doc_name
            if doc_path.exists():
                zf.write(doc_path, doc_name)

    if out_zip_default.exists():
        out_zip_default.unlink()
    shutil.copy2(out_zip_ver, out_zip_default)

    print(f"{FG_GREEN}   [OK] Generated {out_zip_ver}{CLR_RESET}")
    return out_zip_ver


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
        "--app-version",
        default=os.environ.get("APP_VERSION", "1.7.5"),
        help="App release version string (e.g. 1.7.5). Defaults to APP_VERSION env var or 1.7.5.",
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
    print(f"{FG_BLUE}Output Directory: {out_dir}{CLR_RESET}")
    print(f"{FG_BLUE}App Version     : {args.app_version}{CLR_RESET}\n")

    if args.platform in ["mac", "all"]:
        package_mac_dmgs(repo_root, out_dir, args.app_version)
    if args.platform in ["linux", "all"]:
        package_linux(repo_root, out_dir, args.app_version)
    if args.platform in ["windows", "all"]:
        package_windows(repo_root, out_dir, args.app_version)
    if args.platform == "all":
        package_all_combined(repo_root, out_dir, args.app_version)

    print(f"\n{FG_GREEN}Packaging completed successfully! Artifacts saved in {out_dir}{CLR_RESET}")


if __name__ == "__main__":
    main()

