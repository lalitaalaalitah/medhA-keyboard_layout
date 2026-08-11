# How to Use medhA Keyboard Layout

**Author**: `lalitaalaalitah`  
**Website**: https://www.lalitaalaalitah.com  
**GitHub**: https://github.com/lalitaalaalitah/medhA-keyboard_layout  

---

## 1. Installation Guide

### macOS (.dmg Installation)
1. Download `medhA-keyboard-macOS.dmg` from the latest release.
2. Double-click `medhA-keyboard-macOS.dmg` to mount the disk image.
3. Simply **drag and drop** **`medhA.bundle`** into the **`Keyboard Layouts`** shortcut folder (which links to `/Library/Keyboard Layouts`). If an older version of `medhA.bundle` exists, click **Replace** to upgrade in-place.
4. Open **System Settings** -> **Keyboard** -> **Input Sources**.
5. Click **+**, search for **Sanskrit** or **English (US)**, and select `medhA-macOSX-v7`.
6. Switch between input sources using `Control + Space` or `Globe key`.

### Linux (Debian, Ubuntu, Pop!_OS, Arch, Manjaro, Fedora, NixOS)
1. Download `medhA-keyboard-Linux.tar.gz` from the latest release.
2. Extract the archive:
   ```bash
   tar -xvf medhA-keyboard-Linux.tar.gz
   cd Linux
   ```
3. Run the automated installer:
   ```bash
   sudo ./install.sh
   ```
4. **Activation by Desktop Environment**:
   - **GNOME (Ubuntu / Debian / Pop!_OS / Fedora)**: Go to **Settings** -> **Keyboard** -> **Input Sources** -> Add **Sanskrit (medhA)**.
   - **KDE Plasma (Arch / Manjaro)**: Go to **System Settings** -> **Input Devices** -> **Keyboard** -> **Layouts** -> Add **Sanskrit (sa)**.
   - **Command Line (X11 Quick Test)**:
     ```bash
     setxkbmap -layout 'us,sa'
     ```
   - **NixOS**:
     Include `flake.nix` module or add to your `configuration.nix`:
     ```nix
     services.xserver.xkb.extraLayouts.medhA = {
       description = "medhA Sanskrit Keyboard Layout";
       languages = [ "sa" ];
       symbolsFile = ./Linux/sa;
     };
     ```

### Windows
1. Download `medhA-keyboard-Windows.zip` from the latest release.
2. Extract the archive and run `medha-6.exe` (or installer setup).
3. Switch input layouts using `Win + Space` or `Alt + Shift`.

---

## 2. Packaging Releases Locally

To package all platform release archives locally into `dist/`:

```bash
python3 scripts/package_keyboards.py --platform all
```

Outputs archives into `dist/`:
- `medhA-keyboard-macOS.dmg`
- `medhA-keyboard-Linux.tar.gz`
- `medhA-keyboard-Windows.zip`
- `medhA-keyboard-All-Platforms.zip`

---

## 3. Uninstallation

### Linux
```bash
cd Linux
sudo ./uninstall.sh
```

### macOS
Remove `medhA-macOSX-v_1.7.bundle` from `~/Library/Keyboard Layouts/` or `/Library/Keyboard Layouts/`.
