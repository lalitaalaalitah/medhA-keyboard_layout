# Documentation & Screenshot Plan for code.lalitaalaalitah.com

**Author**: `lalitaalaalitah`  
**Website**: https://www.lalitaalaalitah.com  
**Target Blog**: https://code.lalitaalaalitah.com  

---

## 1. Overview & Strategy

This document outlines the detailed structure and screenshot capture checklist for publishing three comprehensive technical posts on `code.lalitaalaalitah.com`, detailing the installation, layout map, usage, and troubleshooting of the `medhA` Sanskrit Keyboard Layout across macOS, Linux, and Windows.

---

## 2. Blog Post 1: *Installing & Mastering medhA Keyboard Layout on macOS*

### Target Audience
macOS users looking for an elegant, high-efficiency Sanskrit / Devanagari input layout.

### Article Outline
1. **Introduction to medhA Layout for macOS**
   - Background, phonetic/logical key placement principles.
2. **Installation Methods**
   - **Method A: Manual Bundle Installation**: Copying `medhA-macOSX-v_1.7.bundle` to `/Library/Keyboard Layouts` or `~/Library/Keyboard Layouts`.
   - **Method B: Homebrew Cask**: `brew install lalitaalaalitah/tap/medha-keyboard`.
   - **Method C: Nix / nix-darwin**: Declarative installation via `flake.nix`.
3. **Activation in macOS System Settings**
   - Navigating to System Settings -> Keyboard -> Input Sources -> Add Input Source.
4. **Keyboard Layout Maps & Keymaps**
   - Normal (Unshifted) keymap diagram.
   - Shifted keymap diagram.
   - Option (AltGr) keymap diagram for Vedic accents and diacritics.
5. **Typing Examples & Best Practices**
   - Typing conjunct consonants using Virama (`/`).
   - Typing Vedic accents (Udatta, Anudatta, Svara).

### Screenshot Capture Inventory (macOS Edition - Captured)
- [x] `medhA_1.7_Installer.png`: Mounted DMG window with bundle and `Keyboard Layouts` shortcut.
- [x] `medhA_1.7_Installed.png`: macOS System Settings -> Keyboard -> Input Sources showing active medhA-macOSX-v7 layout.
- [x] `medhA_1.7_normal.png`: macOS Keyboard Viewer in Unshifted / Normal state.
- [x] `medhA_1.7_shift.png`: macOS Keyboard Viewer in Shifted state.
- [x] `medhA_1.7_CapsLock.png`: macOS Keyboard Viewer in CapsLock state.
- [x] `medhA_1.7_CapsLock_Shift.png`: macOS Keyboard Viewer in CapsLock + Shift state.
- [!] *Observation*: Option and Shift+Option states are currently unmapped in macOS v1.7 (logged as TODO item in `LAYOUT_PARITY_AND_ENHANCEMENT_ANALYSIS.md`).

---

## 3. Blog Post 2: *Configuring medhA Sanskrit Layout across Linux Distros (Debian, Ubuntu, Pop!_OS, Arch, Manjaro, Fedora & NixOS)*

### Target Audience
Linux enthusiasts, developers, and scholars on X11 / Wayland environments.

### Article Outline
1. **Linux XKB Keyboard Architecture**
   - How `xkb/symbols/sa` and `xkb/rules/evdev.xml` function in modern Linux desktops.
2. **Automated Multi-Distro Installation (`install.sh`)**
   - Running `sudo ./install.sh` for instant setup.
3. **Distro-Specific Setup Guides**
   - **Debian / Ubuntu / Pop!_OS (System76 / GNOME)**: Desktop input source selection and `gsettings` CLI configuration.
   - **Arch Linux / Manjaro (KDE Plasma / X11 / Wayland)**: `localectl set-x11-keymap us,sa` and Plasma keyboard settings.
   - **Fedora / RHEL**: Wayland input handling via libxkbcommon.
   - **NixOS**: Adding the layout declaratively using `services.xserver.xkb.extraLayouts` in `configuration.nix` or `flake.nix`.
4. **Keymap Visuals & Vedic Character Layout**
   - Normal, Shift, Level 3 (RAlt / AltGr) maps.
5. **Troubleshooting & Reverting**
   - Command line toggling (`setxkbmap -layout us,sa`) and `uninstall.sh`.

### Screenshot Capture Inventory
- [ ] `linux_01_gnome_settings_ubuntu.png`: Ubuntu / Pop!_OS GNOME Keyboard Settings adding Sanskrit medhA.
- [ ] `linux_02_kde_plasma_manjaro.png`: Manjaro / Arch KDE Plasma Layout Manager showing `sa` layout.
- [ ] `linux_03_terminal_install_output.png`: Terminal screenshot of `./install.sh` output with Catppuccin Mocha colors.
- [ ] `linux_04_xkb_viewer_layout.png`: `xkbprint` or GNOME Layout Viewer screenshot showing `sa` layout.

---

## 4. Blog Post 3: *Setting Up medhA Keyboard Layout on Windows 10/11*

### Target Audience
Windows users typing Sanskrit documents, TeX files, or Office documents.

### Article Outline
1. **Overview of medhA Windows Edition**
   - Built with Microsoft Keyboard Layout Creator (MSKLC).
2. **Installation Instructions**
   - Running `medha-6.exe` / installer package.
   - Enabling Sanskrit input in Windows Settings -> Time & Language -> Language & Region.
3. **Switching Keyboards in Windows**
   - Using `Win + Space` or `Alt + Shift` shortcuts.
4. **Visual Layout Maps & Layer Guide**
   - Default, Shift, AltGr (Right Alt), and Shift+AltGr layers.

### Screenshot Capture Inventory
- [ ] `win_01_installer_screen.png`: Windows installer execution screen.
- [ ] `win_02_language_settings.png`: Windows 10/11 Language & Region settings displaying medhA layout.
- [ ] `win_03_on_screen_keyboard.png`: Windows On-Screen Keyboard showing medhA layout keys.
- [ ] `win_04_altgr_layer.png`: AltGr visual mapping diagram.
