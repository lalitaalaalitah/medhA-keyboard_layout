# medhA Sanskrit Keyboard Layout for Linux (XKB & Distro Setup Guide)

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**Original Article / Linux Source**: [medhA Layout on GitHub (Linux)](https://github.com/lalitaalaalitah/medhA-keyboard_layout/tree/master/Linux)  
**Published on**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)  
**GitHub Repository**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

> 📌 **Website Publication Source**: This page is the dedicated Linux installation guide published on **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)**. For the canonical living Master Guide, see **[MEDHA_KEYBOARD_MASTER_GUIDE.md](../MEDHA_KEYBOARD_MASTER_GUIDE.md)**.

---

## 1. Origin & Motivation

> *"A few of us are used to typing with the medhA keyboard layout. It follows phonetics mostly and is easy to use. To have fun and to learn something about computing, I switched to Linux and felt that medhA was missing. So, I created a custom layout for XKB. Through trial and error, I built a working keyboard for Linux!"*

The **`medhA` keyboard layout for Linux** brings the identical sound-based Devanagari typing scheme to X11 and Wayland desktop environments across all major Linux distributions (Debian, Ubuntu, Pop!_OS, Arch Linux, Manjaro, Fedora, RHEL, and NixOS).

---

## 2. Linux XKB Architecture & Symbol Definition (`sa`)

On Linux, keyboard layouts are handled natively by **XKB** (X Keyboard Extension). The `medhA` layout is defined in the `sa` symbols file located at `/usr/share/X11/xkb/symbols/sa`.

### Highlights of the `sa` Symbol Definition:
- **XKB Symbol Group**: `xkb_symbols "sa" { name[Group1] = "sanskrit"; ... };`
- **Level 3 (AltGr / Right Alt) Key Switch**: Includes `level3(ralt_switch)` allowing access to Vedic accents (`U0951` Udatta, `U0952` Anudatta, `U1CDA` Swarita, `U1CF2`, etc.) via the **`Right Alt (AltGr)`** key.
- **Zero-Width Controls**: Includes `nbsp(zwnj3zwj4)` for Zero-Width Joiner (ZWJ) and Zero-Width Non-Joiner (ZWNJ).
- **Phonetic Consonants & Matras**: Maps Devanagari numbers (`U0966-U096F`), full vowels, matras, anusvara, visarga, and dandas directly aligned with QWERTY sounds.

---

## 3. Automated Installation (`sudo ./install.sh`) — Recommended

The manual process of copying XKB symbol files and editing XML rules is fully automated by the repository's installer script:

1. Download **`medhA-keyboard-Linux.tar.gz`** from [GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Extract the archive in your terminal:
   ```bash
   tar -xvf medhA-keyboard-Linux.tar.gz
   cd Linux
   ```
3. Run the installer script with superuser privileges:
   ```bash
   sudo ./install.sh
   ```
   *What `install.sh` does*: Copies `sa` to `/usr/share/X11/xkb/symbols/sa`, registers `<variant>` in `/usr/share/X11/xkb/rules/evdev.xml`, and clears the XKB compiled cache (`/var/lib/xkb/*.xkm`).

---

## 4. Manual XKB Configuration (Step-by-Step)

If you prefer to configure XKB manually on your Linux distribution:

### Step 1: Create the XKB Symbol File (`/usr/share/X11/xkb/symbols/sa`)
Copy the `Linux/sa` symbol definition file into `/usr/share/X11/xkb/symbols/sa`.

### Step 2: Register Variant in `evdev.xml`
Edit `/usr/share/X11/xkb/rules/evdev.xml` and insert the following `<variant>` entry inside the layout section:

```xml
<variant>
  <configItem>
    <name>sa</name>
    <description>sanskrit</description>
    <languageList>
      <iso639Id>sa</iso639Id>
    </languageList>
  </configItem>
</variant>
```

### Step 3: Quick CLI Testing (X11 & Wayland)
To test the layout instantly in your current terminal session:
```bash
setxkbmap -layout 'us,sa'
```

---

## 5. Desktop Environment Activation

### GNOME (Ubuntu / Debian / Pop!_OS / Fedora)
1. Open **Settings** -> **Keyboard** -> **Input Sources**.
2. Click **+** (Add Input Source).
3. Search for **Sanskrit** or **sa**, select **Sanskrit (medhA)**, and click **Add**.
4. Toggle input sources using **`Super + Space`** or **`Shift + Super + Space`**.

### KDE Plasma (Arch Linux / Manjaro / openSUSE)
1. Open **System Settings** -> **Input Devices** -> **Keyboard** -> **Layouts**.
2. Click **Add Layout**, select Language **Sanskrit**, Layout **sa**.
3. Apply changes and toggle using **`Ctrl + Alt + K`** or the system tray indicator.

### NixOS Configuration (`configuration.nix` / Flake)
For NixOS users, add the extra XKB layout declaratively:

```nix
services.xserver.xkb.extraLayouts.medhA = {
  description = "medhA Sanskrit Keyboard Layout";
  languages = [ "sa" ];
  symbolsFile = ./Linux/sa;
};
```

---

## 6. Key Differences: Linux XKB vs Windows MSKLC

* **Ligature Formation via Virama**: On Linux XKB, pre-composed ligatures like **प्र** are typed using standard Virama composition:  
  `p` + `,` (Virama) + `r` -> **प्र**  
  *(Rather than pressing `Shift + p` directly as on older Windows layouts).*
* **AltGr Layer for Vedic Accents**: Holding **`AltGr` (Right Alt)** unlocks Vedic Udatta, Anudatta, Swarita, and special Vedic marks directly without switching to an English layout.

---

## 7. Recommended Linux Fonts

For optimal Devanagari rendering on X11, Wayland, Firefox, LibreOffice, and TeX/LaTeX:
- **Adishila** (Primary Recommended Font, available at [adishila.com/fonts](https://adishila.com/fonts/))
- **Noto Serif Devanagari** / **Noto Sans Devanagari**
- **Gargi** / **Chandas** / **Sanskrit2003**

---

## 8. Uninstallation

To remove `medhA` from Linux, run the uninstallation script:
```bash
cd Linux && sudo ./uninstall.sh
```
For detailed multi-platform uninstallation guidance, see **[UNINSTALLATION_GUIDE.md](../UNINSTALLATION_GUIDE.md)**.

---

<div align="center">

**परदेवतायाश्चरणनिर्णेजनजलक्षालितः**  
**॥ललितालालितः॥**

</div>

---

## Navigation Links

- 📘 **[Master Guide](../MEDHA_KEYBOARD_MASTER_GUIDE.md)**
- 🏠 **[Main README](../../README.md)**
- 📖 **[How To Use Guide](../../HOW_TO_USE.md)**
- 🗑️ **[Uninstallation Guide](../UNINSTALLATION_GUIDE.md)**
- 🌐 **[Website Maintenance How-To](../WEBSITE_MAINTENANCE_HOW_TO.md)**
