# How to Use medhA Keyboard Layout

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**GitHub**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

[← Back to Main README Overview](README.md) | [Quick Command Summary](README.md#quick-command-summary) | [Supported Platforms](README.md#supported-platforms--installation)

---

## Important Note for Upgrading Users

> [!IMPORTANT]
> If you are upgrading from an older version of `medhA` (such as `v1.3`, `v1.5`, or `v1.7`), please delete or remove older bundle files (e.g. `medhA-macOSX.1.5.bundle` or `medhA-macOSX-v_1.7.bundle`) from your `Keyboard Layouts` folder to avoid duplicate or confusing layout entries in System Settings.
>
> For full step-by-step uninstallation and legacy cleanup instructions across all platforms, see **[UNINSTALLATION_GUIDE.md](docs/UNINSTALLATION_GUIDE.md)**.

---

## 1. Installation Guide

### macOS

#### Option A: Homebrew Cask (Recommended)
For a 1-line installation summary, see [README.md#quick-command-summary](README.md#quick-command-summary).

```bash
brew tap lalitaalaalitah/tap
brew install --cask medha-keyboard
```

#### Option B: DMG / Disk Image Installation
1. Download `medhA-keyboard-macOS.dmg` from the [latest release](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Double-click `medhA-keyboard-macOS.dmg` to mount the disk image.
3. Drag and drop **`medhA.bundle`** into the **`Keyboard Layouts`** shortcut folder (links to `/Library/Keyboard Layouts`). If prompted, click **Replace**.
4. Open **System Settings** -> **Keyboard** -> **Input Sources**.
5. Click **+**, search for **Sanskrit** or **English (US)**, and select `medhA`.
6. Switch between input sources using `Control + Space` or `Globe key`.

#### Option C: Manual Bundle Copy
Download `medhA-keyboard-macOS.zip` from the [latest release](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases), unzip, and copy `medhA.bundle` directly to `/Library/Keyboard Layouts/`.

#### Option D: Nix Flake (`nix-darwin`)
For `nix-darwin` users managing macOS via Nix:

1. Add the repository to your `flake.nix` inputs:
   ```nix
   inputs.medhA-keyboard.url = "github:lalitaalaalitah/medhA-keyboard_layout";
   ```

2. Create a custom `medhA_keyboard.nix` module:
   ```nix
   {
     pkgs,
     lib,
     medhA-keyboard,
     ...
   }:

   let
     medhAPkg = medhA-keyboard.packages.${pkgs.stdenv.hostPlatform.system}.default;
   in
   {
     environment.systemPackages = [ medhAPkg ];

     # Install medhA Sanskrit keyboard layout bundle system-wide to /Library/Keyboard Layouts/medhA.bundle
     system.activationScripts.postActivation.text = lib.mkAfter ''
       echo "Installing medhA keyboard layout bundle system-wide to /Library/Keyboard Layouts..."
       mkdir -p "/Library/Keyboard Layouts"
       rm -rf "$HOME/Library/Keyboard Layouts/medhA.bundle" "$HOME/Library/Keyboard Layouts/medhA_keyboard.bundle" || true
       rm -rf "/Library/Keyboard Layouts/medhA.bundle" "/Library/Keyboard Layouts/medhA_keyboard.bundle" || true
       cp -R "${medhAPkg}/Library/Keyboard Layouts/medhA.bundle" "/Library/Keyboard Layouts/medhA.bundle"
       chmod -R 755 "/Library/Keyboard Layouts/medhA.bundle"
       chown -R root:wheel "/Library/Keyboard Layouts/medhA.bundle" || true
       /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -R -f "/Library/Keyboard Layouts/medhA.bundle" || true
       /usr/bin/touch "/Library/Keyboard Layouts"
     '';
   }
   ```

3. Import `medhA_keyboard.nix` in your `darwinConfigurations`:
   ```nix
   darwinConfigurations."hostname" = nix-darwin.lib.darwinSystem {
     inherit system specialArgs;
     modules = [
       ./modules/darwin
       ./medhA_keyboard.nix
     ];
   };
   ```

---

### Linux (Debian, Ubuntu, Pop!_OS, Arch, Manjaro, Fedora, NixOS)

#### Automated Installer
1. Download `medhA-keyboard-Linux.tar.gz` from the [latest release](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Extract the archive:
   ```bash
   tar -xvf medhA-keyboard-Linux.tar.gz
   cd Linux
   ```
3. Run the automated installer (replaces `sa` symbol file and clears XKB cache):
   ```bash
   sudo ./install.sh
   ```

#### Activation by Desktop Environment
- **GNOME (Ubuntu / Debian / Pop!_OS / Fedora)**: Go to **Settings** -> **Keyboard** -> **Input Sources** -> Add **Sanskrit (medhA)**.
- **KDE Plasma (Arch / Manjaro)**: Go to **System Settings** -> **Input Devices** -> **Keyboard** -> **Layouts** -> Add **Sanskrit (sa)**.
- **Command Line (X11 Quick Test)**:
  ```bash
  setxkbmap -layout 'us,sa'
  ```

#### NixOS Configuration
Using Flake module or directly in `configuration.nix`:

```nix
# In flake.nix outputs / NixOS configuration:
services.xserver.xkb.extraLayouts.medhA = {
  description = "medhA Sanskrit Keyboard Layout";
  languages = [ "sa" ];
  symbolsFile = ./Linux/sa;
};
```

---

### Windows (10 / 11)

1. Download `medhA-keyboard-Windows.zip` from the [latest release](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Extract the ZIP archive and run `medha-6.exe` (or `setup.exe`).
3. Follow the setup wizard to complete installation.
4. Switch input layouts using `Win + Space` or `Alt + Shift`.

---

## 2. Packaging Releases Locally

To package all platform release archives locally into `dist/` (see [README.md#packaging-releases](README.md#packaging-releases)):

```bash
python3 scripts/package_keyboards.py --app-version 1.7.5 --platform all
```

Generated outputs in `dist/`:
- `medhA-keyboard-macOS-v1.7.5.dmg` (and `medhA-keyboard-macOS.dmg`)
- `medhA-keyboard-Linux-v1.7.5.tar.gz` (and `medhA-keyboard-Linux.tar.gz`)
- `medhA-keyboard-Windows-v1.7.5.zip` (and `medhA-keyboard-Windows.zip`)
- `medhA-keyboard-All-Platforms-v1.7.5.zip` (and `medhA-keyboard-All-Platforms.zip`)

For release versioning rules and release workflow, refer to **[RELEASE_STANDARDS.md](RELEASE_STANDARDS.md)**.

---

## 3. Uninstallation & Legacy Cleanup

For complete platform-specific uninstallation instructions, see **[UNINSTALLATION_GUIDE.md](docs/UNINSTALLATION_GUIDE.md)**.

---

## Navigation Links

- 🏠 **[Main Overview & Landing Page](README.md)**
- 📘 **[Comprehensive Master Guide](docs/MEDHA_KEYBOARD_MASTER_GUIDE.md)**
- ⚡ **[Quick Command Summary](README.md#quick-command-summary)**
- 📋 **[Release Standards & Tap Workflow](RELEASE_STANDARDS.md)**
- 🗑️ **[Uninstallation Guide](docs/UNINSTALLATION_GUIDE.md)**
- 🌐 **[Website Maintenance & Publishing How-To](docs/WEBSITE_MAINTENANCE_HOW_TO.md)**
- 🗺️ **[Documentation Plan](docs/DOCUMENTATION_PLAN.md)**


