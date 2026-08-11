# medhA Keyboard Layout Uninstallation & Upgrade Cleanup Guide

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**GitHub Repository**: [github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

---

## Overview

When upgrading to a new release of `medhA` keyboard layout, older installations with versioned filenames (e.g. `medhA-macOSX.1.5.bundle`, `medhA-macOSX-v_1.7.bundle`, or `medhA_1.6_working.bundle`) may remain on disk alongside the new `medhA.bundle`. To prevent duplicate entries or confusion in your system's Input Sources menu, follow the platform-specific instructions below to clean up legacy versions.

---

## 1. macOS Uninstallation & Legacy Cleanup

### Step 1: Remove Old Bundle Files from Finder
1. Open **Finder**.
2. Press **`Command + Shift + G`** (Go to Folder).
3. Check both of the following locations:
   - **`~/Library/Keyboard Layouts`** (User installation)
   - **`/Library/Keyboard Layouts`** (System-wide installation)
4. Move any older `medhA` bundle files to Trash:
   - `medhA-macOSX.1.3.bundle`
   - `medhA-macOSX.1.5.bundle`
   - `medhA_1.6_working.bundle`
   - `medhA-macOSX-v_1.7.bundle`
5. Empty the Trash.

### Step 2: Remove Stale Input Sources in System Settings
1. Open **System Settings** -> **Keyboard** -> **Input Sources**.
2. If multiple `medhA` layouts appear, select the old layout entry and click the **`-`** (Remove) button at the bottom.
3. Log out and log back in (or restart your Mac) to refresh Apple's input menu cache.

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
