# How to Use medhA Keyboard Layout

**Author**: `lalitaalaalitah`  
**Website**: https://www.lalitaalaalitah.com  
**GitHub**: https://github.com/lalitaalaalitah/medhA-keyboard_layout  

---

## Important Note for Upgrading Users

> [!IMPORTANT]
> If you are upgrading from an older version of `medhA` (such as `v1.3`, `v1.5`, or `v1.7`), please delete or remove older bundle files (e.g. `medhA-macOSX.1.5.bundle` or `medhA-macOSX-v_1.7.bundle`) from your `Keyboard Layouts` folder to avoid duplicate or confusing layout entries in System Settings.
> 
> For full step-by-step uninstallation and legacy cleanup instructions across all platforms, see **[UNINSTALLATION_GUIDE.md](docs/UNINSTALLATION_GUIDE.md)**.

---

## 1. Installation Guide

### macOS (Homebrew Cask Installation - Recommended)
```bash
brew tap lalitaalaalitah/tap
brew install --cask medha-keyboard
```

### macOS (.dmg Manual Installation)
1. Download `medhA-keyboard-macOS.dmg` from the latest release.
2. Double-click `medhA-keyboard-macOS.dmg` to mount the disk image.
3. Drag and drop **`medhA.bundle`** into the **`Keyboard Layouts`** shortcut folder (links to `/Library/Keyboard Layouts`). If prompted, click **Replace**.
4. Open **System Settings** -> **Keyboard** -> **Input Sources**.
5. Click **+**, search for **Sanskrit** or **English (US)**, and select `medhA`.
6. Switch between input sources using `Control + Space` or `Globe key`.

### Linux (Debian, Ubuntu, Pop!_OS, Arch, Manjaro, Fedora, NixOS)
1. Download `medhA-keyboard-Linux.tar.gz` from the latest release.
2. Extract the archive:
   ```bash
   tar -xvf medhA-keyboard-Linux.tar.gz
   cd Linux
   ```
3. Run the automated installer (automatically replaces previous `sa` symbol file and clears XKB cache):
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

## 3. Uninstallation & Legacy Cleanup

For detailed platform-specific uninstallation steps, see **[UNINSTALLATION_GUIDE.md](docs/UNINSTALLATION_GUIDE.md)**.
