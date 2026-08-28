# medhA Sanskrit Keyboard Layout (medhA-keyboard_layout)

[![Packaging Tool](https://img.shields.io/badge/packaging--tool-v1.0.0-blue.svg)](scripts/package_keyboards.py)
[![Author](https://img.shields.io/badge/author-lalitaalaalitah-purple.svg)](https://www.lalitaalaalitah.com)
[![Platform Support](https://img.shields.io/badge/platform-macOS_|_Linux_|_Windows_|_nix_|_nix--darwin-darkgreen.svg)](#supported-platforms--installation)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An intuitive, high-efficiency Sanskrit / Devanagari keyboard layout available for **macOS**, **Linux** (Debian, Ubuntu, Pop!_OS, Arch, Manjaro, Fedora, NixOS), and **Windows**.

---

## Author & Project Metadata

- **Author**: `lalitaalaalitah`
- **Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)
- **GitHub**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)
- **Technical Articles**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)

---

## Supported Platforms & Installation

For full, step-by-step installation instructions for every operating system and desktop environment, see **[HOW_TO_USE.md](HOW_TO_USE.md)**.

| Platform | Quick Command / Package | Full Guide |
| :--- | :--- | :--- |
| **macOS (Homebrew)** | `brew tap lalitaalaalitah/tap && brew install --cask medha-keyboard` | [macOS Setup](HOW_TO_USE.md#macos) |
| **macOS (DMG / Bundle)** | `medhA-keyboard-macOS.dmg` / `medhA.bundle` | [DMG Setup](HOW_TO_USE.md#option-b-dmg--disk-image-installation) |
| **macOS (Nix-Darwin)** | `inputs.medhA-keyboard.url` Flake module | [Nix-Darwin Setup](HOW_TO_USE.md#option-d-nix-flake-nix-darwin) |
| **Linux (Installer)** | `tar -xvf medhA-keyboard-Linux.tar.gz && sudo ./install.sh` | [Linux Setup](HOW_TO_USE.md#linux-debian-ubuntu-pop_os-arch-manjaro-fedora-nixos) |
| **Linux (NixOS)** | `services.xserver.xkb.extraLayouts.medhA` | [NixOS Setup](HOW_TO_USE.md#nixos-configuration) |
| **Windows (10 / 11)** | `medhA-keyboard-Windows.zip` (`medha-6.exe`) | [Windows Setup](HOW_TO_USE.md#windows-10--11) |

---

## Quick Command Summary

### macOS (Homebrew Cask)
```bash
brew tap lalitaalaalitah/tap
brew install --cask medha-keyboard
```

### Linux (Automated Script)
```bash
tar -xvf medhA-keyboard-Linux.tar.gz
cd Linux && sudo ./install.sh
```

### Windows (Setup Installer)
```powershell
Expand-Archive -Path medhA-keyboard-Windows.zip -DestinationPath .
.\medha-6.exe
```


---

## Packaging Releases

Build release archives locally across all platforms:

```bash
python3 scripts/package_keyboards.py --app-version 1.7.5 --platform all
```

---

## Repository Documentation Index

- **[docs/MEDHA_KEYBOARD_MASTER_GUIDE.md](docs/MEDHA_KEYBOARD_MASTER_GUIDE.md)**: Comprehensive master guide & canonical source content for [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com).
- **[HOW_TO_USE.md](HOW_TO_USE.md)**: Exhaustive multi-distro and multi-OS installation guide.
- **[RELEASE_STANDARDS.md](RELEASE_STANDARDS.md)**: Release versioning standards, tag naming, and Homebrew Tap update procedure.
- **[docs/WEBSITE_MAINTENANCE_HOW_TO.md](docs/WEBSITE_MAINTENANCE_HOW_TO.md)**: Architecture specification guiding website content publication & post updates on `code.lalitaalaalitah.com`.
- **[docs/UNINSTALLATION_GUIDE.md](docs/UNINSTALLATION_GUIDE.md)**: Uninstallation & legacy version cleanup guide.
- **[docs/DOCUMENTATION_PLAN.md](docs/DOCUMENTATION_PLAN.md)**: Blog post roadmap & screenshot inventory for `code.lalitaalaalitah.com`.
- **[docs/HOMEBREW_RELEASE_PLAN.md](docs/HOMEBREW_RELEASE_PLAN.md)**: Homebrew Cask distribution plan.
- **[docs/LAYOUT_PARITY_AND_ENHANCEMENT_ANALYSIS.md](docs/LAYOUT_PARITY_AND_ENHANCEMENT_ANALYSIS.md)**: Layout parity & character mapping enhancement analysis.

