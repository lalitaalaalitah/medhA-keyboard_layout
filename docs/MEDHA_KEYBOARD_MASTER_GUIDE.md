# medhA Sanskrit Keyboard Layout – Master Guide & Multi-Platform Manual

**Author**: `lalitaalaalitah`
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)
**Published on**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)
**GitHub Repository**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)

> 🟢 **Current Version**: `v1.7.5` | **Last Updated**: August 29, 2026 | [View GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases)

> 📌 **Website Publication Source**: This document is the canonical source content for the living Master Guide Page published on **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)**. For website publishing rules, see **[WEBSITE_MAINTENANCE_HOW_TO.md](WEBSITE_MAINTENANCE_HOW_TO.md)**.

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Version History & Changelog](#2-version-history--changelog)
3. [Multi-Platform Installation](#3-multi-platform-installation)
   - [3.1 macOS](#31-macos)
   - [3.2 Linux (Debian, Ubuntu, Arch, Fedora, NixOS)](#32-linux-debian-ubuntu-arch-fedora-nixos)
   - [3.3 Windows (10 / 11)](#33-windows-10--11)
4. [HowTO & Typing Guide](#4-howto--typing-guide)
   - [4.1 Phonetic Key Mapping Principles](#41-phonetic-key-mapping-principles)
   - [4.2 Vowels & Matras](#42-vowels--matras)
   - [4.3 Punctuation & Devanagari Signs](#43-punctuation--devanagari-signs)
   - [4.4 Conjunct Consonants & Ligatures](#44-conjunct-consonants--ligatures)
   - [4.5 Precision Controls: ZWJ & ZWNJ](#45-precision-controls-zwj--zwnj)
   - [4.6 Vedic Accents (Svaras)](#46-vedic-accents-svaras)
5. [Visual Keymaps & Layer Reference](#5-visual-keymaps--layer-reference)
6. [Troubleshooting & FAQs](#6-troubleshooting--faqs)
7. [Sub-Pages & Dedicated Modular Guides](#7-sub-pages--dedicated-modular-guides)

---

## 1. Introduction

### 1.1 What is medhA?
**`medhA`** is an intuitive, high-efficiency Devanagari keyboard layout developed by **lalitaalaalitah** for Sanskrit, Hindi, Marathi, Nepali, and other languages written in the Devanagari script.

Traditional layout systems (like InScript) rearrange keys based on typewriter geometry rather than phonetic intuition. In contrast, `medhA` maps Devanagari letters directly to standard QWERTY keys according to their **phonetic acoustic similarity**, allowing anyone accustomed to an English keyboard to type Sanskrit naturally and rapidly.

### 1.2 Key Features
* **Phonetic Intuition**: Typing `k` produces **क**, `g` produces **ग**, `t` produces **त**, `d` produces **द**.
* **Frequency-Based Shift Mapping**: Unshifted keys output the most frequent consonants/vowels, while `Shift` outputs aspirated variants or full vowels (e.g. `k` = **क**, `Shift+K` = **ख**).
* **Complete Ligature Control**: Full control over Virama suppressions, half-consonants, and explicit non-joining forms.
* **Vedic Text Support**: Built-in native support for Vedic accents (Udatta, Anudatta, Swarita).

### 1.3 Supported Languages & Regional Scripts
`medhA` supports full Devanagari typography for:
* **Primary Languages**: Sanskrit (Classical & Vedic), Hindi, Marathi, Nepali.
* **Regional & Historical Languages**: Newari, Maithili, Bhojpuri, Konkani, Marwari, Magahi, Gujari, Pahari (Garhwali & Kumaoni), Bhili, Santhali, Tharu, Sindhi, Sherpa, Kashmiri, and historical Devanagari-written Gujarati.

---

## 2. Version History & Changelog

| Version | Release Date | Summary of Key Changes & Improvements |
| :--- | :--- | :--- |
| **v1.7.5** | August 2026 | Added automated Homebrew Cask sync, Nix Flake support (`nix-darwin` & NixOS), unified cross-platform release packager (`package_keyboards.py`), and enhanced Vedic svara mappings. |
| **v1.7.0** | Early 2026 | Introduced updated macOS `.bundle` structure, standalone DMG installer, clean Linux XKB `sa` symbol integration, and Windows setup executables. |
| **medhA 3** | Historical | Introduced special formatting shortcuts (`Ctrl+Shift+1` ZWJ, `Ctrl+Shift+2` ZWNJ, `Ctrl+Shift+3..5` Vedic Svaras), Marathi half-Ra (**र्‌क**), and explicit Virama control. |
| **v1.0.0** | Initial Release | Core phonetic layout definition for macOS, Linux, and Windows. |

> 📌 **Full Release Announcements**: Detailed historical release posts and changelogs are published on **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)** and tagged on **[GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases)**.

---

## 3. Multi-Platform Installation

### 3.1 macOS

#### Option A: Homebrew Cask (Recommended)
```bash
brew tap lalitaalaalitah/tap
brew install --cask medha-keyboard
```

#### Option B: DMG Installer
1. Download `medhA-keyboard-macOS.dmg` from [GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Double-click the DMG and drag **`medhA.bundle`** into the **`Keyboard Layouts`** shortcut folder.
3. Open **System Settings** -> **Keyboard** -> **Input Sources**, click **+**, search for **Sanskrit** or **English (US)**, and select `medhA`.

#### Option C: Nix-Darwin Flake
Add to your `flake.nix` inputs:
```nix
inputs.medhA-keyboard.url = "github:lalitaalaalitah/medhA-keyboard_layout";
```
Enable the package in your system configuration to link `/Library/Keyboard Layouts/medhA.bundle`.

---

### 3.2 Linux (Debian, Ubuntu, Arch, Fedora, NixOS)

#### Automated Script Installation
1. Download `medhA-keyboard-Linux.tar.gz` and extract:
   ```bash
   tar -xvf medhA-keyboard-Linux.tar.gz
   cd Linux && sudo ./install.sh
   ```
2. **Desktop Activation**:
   * **GNOME (Ubuntu / Debian / Pop!_OS / Fedora)**: Settings -> Keyboard -> Input Sources -> Add **Sanskrit (medhA)**.
   * **KDE Plasma (Arch / Manjaro)**: System Settings -> Input Devices -> Keyboard -> Layouts -> Add **sa**.
   * **CLI Quick Test**: `setxkbmap -layout 'us,sa'`

#### NixOS Configuration
```nix
services.xserver.xkb.extraLayouts.medhA = {
  description = "medhA Sanskrit Keyboard Layout";
  languages = [ "sa" ];
  symbolsFile = ./Linux/sa;
};
```

---

### 3.3 Windows (10 / 11)

1. Download `medhA-keyboard-Windows.zip` from [GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Extract the archive and run `medha-6.exe` (or `setup.exe`).
3. Follow the wizard setup. Switch input layouts using `Win + Space` or `Alt + Shift`.

---

## 4. HowTO & Typing Guide

### 4.1 Phonetic Key Mapping Principles

| QWERTY Key | Unshifted Output | Shifted Output |
| :---: | :---: | :---: |
| **k** | **क** (Ka) | **ख** (Kha) |
| **g** | **ग** (Ga) | **घ** (Gha) |
| **c** | **च** (Cha) | **छ** (Chha) |
| **j** | **ज** (Ja) | **झ** (Jha) |
| **t** | **त** (Dental Ta) | **ट** (Retroflex Tta) |
| **d** | **द** (Dental Da) | **ड** (Retroflex Dda) |
| **p** | **प** (Pa) | **फ** (Pha) |
| **b** | **ब** (Ba) | **भ** (Bha) |
| **m** | **म** (Ma) | **ङ** (Nga) |
| **n** | **न** (Na) | **ण** (Retroflex Nna) |

---

### 4.2 Vowels & Matras

* **Dependent Vowel Signs (Matras)**:
  * `a` -> **ा** (Matra AA)
  * `i` -> **ि** (Matra I)
  * `Shift + I` -> **ी** (Matra II)
  * `u` -> **ु** (Matra U)
  * `Shift + U` -> **ू** (Matra UU)
  * `e` -> **े** (Matra E)
  * `o` -> **ो** (Matra O)

---

### 4.3 Punctuation & Devanagari Signs

* **Halanta / Virama (्)**: Type `,` (comma).
* **Anusvara (ं)**: Type `.` (period).
* **Visarga (ः)**: Type `/` (slash).
* **Single Danda (।)**: Type `Shift + /`.
* **Double Danda (॥)**: Type `Shift + .`.

---

### 4.4 Conjunct Consonants & Ligatures

To form conjunct consonants, type the first consonant, followed by Virama (`,`), followed by the second consonant:
* `k` + `,` + `t` = **क्त** (k + ् + t)
* `s` + `,` + `p` + `&` = **स्पृ** (with matra RI)
* `k` + `,` + `sh` = **क्ष**

---

### 4.5 Precision Controls: ZWJ & ZWNJ

* **Zero-Width Joiner (ZWJ - `Ctrl + Shift + 1`)**: Prevents complex ligature formation and forces half-consonant appearance. Used for Marathi/Newari half-Ra:
  * `r` + `,` + `Ctrl+Shift+1` (ZWJ) + `k` = **र्‌क**
* **Zero-Width Non-Joiner (ZWNJ - `Ctrl + Shift + 2`)**: Forces explicit Virama visibility:
  * `k` + `,` + `Ctrl+Shift+2` (ZWNJ) + `t` = **क्‌त**

---

### 4.6 Vedic Accents (Svaras)

`medhA` includes native support for Vedic text composition:
* **Udatta (॑)**: `U+0951` (`Ctrl + Shift + 3` / Devanagari Stress Sign Datta)
* **Anudatta (॒)**: `U+0952` (`Ctrl + Shift + 4` / Devanagari Stress Sign Anudatta)
* **Swarita / Triple Udatta (᳚)**: `U+1CDA` / `U+0951` (`Ctrl + Shift + 5`)

---

## 5. Visual Keymaps & Layer Reference

Below are visual screenshots captured from the macOS Keyboard Viewer:

### 5.1 Unshifted State
![medhA Keyboard Viewer Normal](screenshots/medhA_macOS/medhA_1.7_normal.png)

### 5.2 Shifted State
![medhA Keyboard Viewer Shift](screenshots/medhA_macOS/medhA_1.7_shift.png)

### 5.3 CapsLock State
![medhA Keyboard Viewer CapsLock](screenshots/medhA_macOS/medhA_1.7_CapsLock.png)

---

## 6. Troubleshooting & FAQs

* **Q: I see duplicate medhA entries in System Settings on macOS.**
  *A: Delete old bundle files (such as `medhA-macOSX.1.5.bundle` or `medhA-macOSX-v_1.7.bundle`) from `~/Library/Keyboard Layouts/` or `/Library/Keyboard Layouts/`. See [UNINSTALLATION_GUIDE.md](UNINSTALLATION_GUIDE.md).*

* **Q: How do I switch input layouts quickly?**
  *A: macOS: `Control + Space` or `Globe key`. Linux: `Super + Space` or `Alt + Shift`. Windows: `Win + Space`.*

---

## 7. Sub-Pages & Dedicated Modular Guides

For modular details, dedicated platform sub-pages, uninstallation steps, and maintenance guidelines, explore the following documentation:

- 📖 **[HOW_TO_USE.md](../HOW_TO_USE.md)**: Exhaustive multi-distro and multi-OS installation guide.
- 🍎 **[macOS Installation Guide](posts/01_macOS_medhA_Keyboard_Installation_Guide.md)**: Detailed macOS manual and Homebrew/Nix setup.
- 🪟 **[Windows Installation Guide](posts/01_Windows_medhA_Keyboard_Installation_Guide.md)**: Native MSKLC setup, XP/Vista/7/10/11 activation, & Sanskrit2003 font setup.
- 📋 **[RELEASE_STANDARDS.md](../RELEASE_STANDARDS.md)**: Release versioning standards, tag naming, and Homebrew Tap update procedure.
- 🌐 **[WEBSITE_MAINTENANCE_HOW_TO.md](WEBSITE_MAINTENANCE_HOW_TO.md)**: Architecture guide for maintaining website living guides & historical release posts.
- 🗑️ **[UNINSTALLATION_GUIDE.md](UNINSTALLATION_GUIDE.md)**: Uninstallation & legacy version cleanup guide across all platforms.
- 🗺️ **[DOCUMENTATION_PLAN.md](DOCUMENTATION_PLAN.md)**: Blog post roadmap & screenshot inventory.
