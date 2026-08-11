# medhA Sanskrit Keyboard Layout (medhA-keyboard_layout)

[![Packaging Tool](https://img.shields.io/badge/packaging--tool-v1.0.0-blue.svg)](scripts/package_keyboards.py)
[![Author](https://img.shields.io/badge/author-lalitaalaalitah-brightgreen.svg)](https://www.lalitaalaalitah.com)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-orange.svg)](#supported-platforms)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An intuitive, high-efficiency Sanskrit / Devanagari keyboard layout available for **macOS**, **Linux** (Debian, Ubuntu, Pop!_OS / System76, Arch Linux, Manjaro, Fedora, NixOS), and **Windows**.

---

## Author & Project Metadata

- **Author**: `lalitaalaalitah`
- **Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)
- **GitHub**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)
- **Technical Articles**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)

---

## Supported Platforms & Editions

| Platform | Edition File / Package | Installation Method |
| :--- | :--- | :--- |
| **macOS** | `medhA-macOSX-v_1.7.bundle` | Bundle copy, Homebrew Cask, or Nix Flake |
| **Linux** | `sa` (XKB Symbols) | Automated `install.sh` (GNOME/KDE/X11/Wayland/NixOS) |
| **Windows** | `medha-6.exe` | Executable setup installer |

---

## Quick Setup

For complete, step-by-step installation instructions for macOS, Linux, and Windows, see [HOW_TO_USE.md](HOW_TO_USE.md).

### Linux Automated Installer
```bash
tar -xvf medhA-keyboard-Linux.tar.gz
cd Linux
sudo ./install.sh
```

### macOS Installation

**Option A: Via Homebrew Cask (Recommended)**
```bash
brew tap lalitaalaalitah/tap
brew install --cask medha-keyboard
```

**Option B: Manual Bundle Copy**
Download `medhA-keyboard-macOS.zip` and move `medhA-macOSX-v_1.7.bundle` to `~/Library/Keyboard Layouts/`.

### Nix Flake Installation
```nix
# In your flake.nix inputs:
inputs.medhA-keyboard.url = "github:lalitaalaalitah/medhA-keyboard_layout";

# NixOS module:
imports = [ inputs.medhA-keyboard.nixosModules.default ];
```

---

## Packaging Utility

To build release archives for all platforms locally:

```bash
python3 scripts/package_keyboards.py --platform all
```

Outputs archives into `dist/`:
- `medhA-keyboard-macOS.zip`
- `medhA-keyboard-Linux.tar.gz`
- `medhA-keyboard-Windows.zip`
- `medhA-keyboard-All-Platforms.zip`

---

## Documentation & Future Roadmap

- **[HOW_TO_USE.md](HOW_TO_USE.md)**: Exhaustive multi-distro and multi-OS installation guide.
- **[docs/UNINSTALLATION_GUIDE.md](docs/UNINSTALLATION_GUIDE.md)**: Uninstallation & legacy version cleanup guide.
- **[docs/DOCUMENTATION_PLAN.md](docs/DOCUMENTATION_PLAN.md)**: Blog post roadmap & screenshot inventory for `code.lalitaalaalitah.com`.
- **[docs/HOMEBREW_RELEASE_PLAN.md](docs/HOMEBREW_RELEASE_PLAN.md)**: Homebrew Cask distribution plan.
- **[docs/LAYOUT_PARITY_AND_ENHANCEMENT_ANALYSIS.md](docs/LAYOUT_PARITY_AND_ENHANCEMENT_ANALYSIS.md)**: [TODO] Layout parity & character mapping enhancement analysis.
