# medhA Keyboard Layout Uninstallation & Upgrade Cleanup Guide

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**GitHub Repository**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

---

## Overview

When upgrading to a new release of `medhA` keyboard layout, older installations with versioned filenames (e.g. `medhA-macOSX.1.5.bundle`, `medhA-macOSX-v_1.7.bundle`, or `medhA_1.6_working.bundle`) may remain on disk alongside the new `medhA.bundle`. To prevent duplicate entries or confusion in your system's Input Sources menu, follow the platform-specific instructions below to clean up legacy versions.

---

## 1. macOS Uninstallation & Legacy Cleanup

Depending on how you originally installed `medhA` on macOS, follow the corresponding uninstallation method below:

### Method 1: If Installed via Manual `.bundle` or DMG

1. Open **Finder**.
2. Press **`Command + Shift + G`** (Go to Folder shortcut).
3. Check both of the following keyboard layout locations:
   - **`~/Library/Keyboard Layouts`** (Current user installation)
   - **`/Library/Keyboard Layouts`** (System-wide installation)
4. Move `medhA.bundle` and any legacy bundle files to Trash:
   - `medhA.bundle`
   - `medhA-macOSX.1.3.bundle`
   - `medhA-macOSX.1.5.bundle`
   - `medhA_1.6_working.bundle`
   - `medhA-macOSX-v_1.7.bundle`
5. Empty the Trash.

---

### Method 2: If Installed via Homebrew Cask (`brew`)

Run the following command in terminal to uninstall the Homebrew cask:

```bash
brew uninstall --cask medha-keyboard
```

*(Optional)* To untap the repository:

```bash
brew untap lalitaalaalitah/tap
```

---

### Method 3: If Installed via Nix (`nix-darwin` / Nix Flake)

1. Open your `nix-darwin` configuration file (`flake.nix` or `darwin-configuration.nix`).
2. Remove `inputs.medhA-keyboard` from your `environment.systemPackages` list:
   ```nix
   # Remove from environment.systemPackages:
   # environment.systemPackages = [ inputs.medhA-keyboard.packages.aarch64-darwin.default ];
   ```
3. Rebuild your system configuration:
   ```bash
   darwin-rebuild switch --flake .
   ```
4. Clear unreferenced store paths with garbage collection:
   ```bash
   nix-collect-garbage -d
   ```

---

### Clearing Stale Input Sources in macOS System Settings

After removing the files using any of the methods above:

1. Open **System Settings** (or **System Preferences**) -> **Keyboard** -> **Input Sources**.
2. Select the `medhA` layout entry and click the **`-`** (Remove) button at the bottom.
3. Log out and log back in (or restart your Mac) to clear Apple's input menu cache.

---

## 2. Linux Uninstallation & Cache Reset

### Automated Uninstallation Script
If installed via the `medhA` Linux package, open terminal and run:

```bash
cd Linux
sudo ./uninstall.sh
```

### Manual Cleanup
1. Remove the installed XKB symbol file:
   ```bash
   sudo rm -f /usr/share/X11/xkb/symbols/sa
   ```
2. Clear the compiled XKB keymap cache:
   ```bash
   sudo rm -f /var/lib/xkb/*.xkm
   ```
3. Remove **Sanskrit (medhA)** from your Desktop Environment settings:
   - **GNOME (Ubuntu / Debian / Pop!_OS / Fedora)**: Settings -> Keyboard -> Input Sources -> Remove `sa`.
   - **KDE Plasma (Arch / Manjaro)**: System Settings -> Keyboard -> Layouts -> Remove `sa`.

---

## 3. Windows Uninstallation

1. Open **Settings** -> **Apps** -> **Installed Apps** (or **Control Panel** -> **Programs and Features**).
2. Search for **`medhA`** or **`medha`**.
3. Select **Uninstall** and follow the prompt.
4. Go to **Settings** -> **Time & Language** -> **Language & Region** -> **Sanskrit** / **Hindi**, and remove any duplicate `medhA` layout entries.

---

<div align="center">

**परदेवतायाश्चरणनिर्णेजनजलक्षालितः**  
**॥ललितालालितः॥**

</div>

---

## Navigation Links

- 📘 **[Master Guide](MEDHA_KEYBOARD_MASTER_GUIDE.md)**
- 🏠 **[Main README](../README.md)**
- 📖 **[How To Use Guide](../HOW_TO_USE.md)**
- 🍎 **[macOS Installation Guide](posts/01_macOS_medhA_Keyboard_Installation_Guide.md)**
- 🐧 **[Linux Installation Guide](posts/01_Linux_medhA_Keyboard_Installation_Guide.md)**
- 🪟 **[Windows Installation Guide](posts/01_Windows_medhA_Keyboard_Installation_Guide.md)**
