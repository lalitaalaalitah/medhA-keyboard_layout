# medhA Sanskrit Keyboard Layout for macOS (Definitive Guide & Setup)

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**Original Article**: [https://eng.lalitaalaalitah.com/medha-mac-os/](https://eng.lalitaalaalitah.com/medha-mac-os/)  
**Historical Release Asset**: [medhA-keyboard_mac_1.5_release_1.dmg](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases/download/release_v_0.1/medhA-keyboard_mac_1.5_release_1.dmg)  
**Published on**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)  
**GitHub Repository**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

> 📌 **Website Publication Source**: This page is the dedicated macOS installation guide published on **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)**. For the canonical living Master Guide, see **[MEDHA_KEYBOARD_MASTER_GUIDE.md](../MEDHA_KEYBOARD_MASTER_GUIDE.md)**.

---

## Introduction & Design Scheme

The **`medhA` keyboard layout for macOS** brings the trusted Devanagari typing scheme from Windows and Linux to Apple Mac computers. If you are shifting to Apple computers, `medhA` ensures you feel right at home with identical sound-based key placements for Sanskrit, Hindi, Marathi, Nepali, and other Devanagari-script languages.

### Why macOS Keyboard Layouts are Powerful
It appears that we might be able to get even more benefit from the keyboard layout system in macOS, as the macOS input subsystem supports rich multi-key layer combinations (`Normal`, `Shift`, `CapsLock`, `CapsLock + Shift`, and `Option`) to get different linguistic results naturally.

---

## 1. Evolution of macOS Releases

* **`medhA-macOSX.1.3`**: Initial macOS bundle layout porting the core sound-based phonetic scheme.
* **`medhA-macOSX.1.5`**: Added standalone DMG installer packaging (`medhA-keyboard_mac_1.5_release_1.dmg`) and bundle structure.
* **`medhA-macOSX v1.7.0 / v1.7.5`**: Modern unified bundle (`medhA.bundle`) supporting Homebrew Cask distribution (`brew install --cask medha-keyboard`) and declarative `nix-darwin` Flake integration.

---

## 2. Installation Methods on macOS

### Method A: Drag-and-Drop Installation via DMG (Recommended)

1. Download **`medhA-keyboard-macOS.dmg`** (or historical `medhA-keyboard_mac_1.5_release_1.dmg`) from [GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Double-click the downloaded `.dmg` file to mount the disk image.
3. Simply **drag the `medhA.bundle`** (or `medhA-macOSX.1.5.bundle`) file into the **`Keyboard Layouts`** shortcut folder.
4. Go to **System Settings** (or **System Preferences** on older macOS) -> **Keyboard** -> **Input Sources**.
5. Click **+**, search for **`Sanskrit`** or **`English (US)`**, select **`medhA`**, and click **Add** (or **Done**).

> ⚠️ **Important Note for Upgrading Users**: If you previously installed an older version with a versioned filename (such as `medhA-macOSX.1.3.bundle` or `medhA-macOSX.1.5.bundle`), please delete those older bundle files from your `Keyboard Layouts` folder to avoid duplicate entries in System Settings.
> For detailed uninstallation instructions across macOS, Linux, and Windows, see **[UNINSTALLATION_GUIDE.md](../UNINSTALLATION_GUIDE.md)**.

![medhA 1.7 DMG Installer](../screenshots/medhA_macOS/medhA_1.7_Installer.png)

---

### Method B: Manual Bundle Copying in Finder (`Command + Shift + G`)

1. Download the `medhA.bundle` (or `medhA-macOSX.1.5.bundle`) file.
2. Open **Finder**, press **`Command + Shift + G`** (Go to Folder shortcut).
3. Type **`~/Library/Keyboard Layouts`** (for current user) or **`/Library/Keyboard Layouts`** (for all system users) in the pop-up window and press **Enter**. It will open the mentioned folder.
4. Paste the file (`medhA.bundle`) inside the **`Keyboard Layouts`** folder and close the window.
5. Go to **System Settings** (or **System Preferences**) -> **Keyboard** -> **Input Sources**.
6. Search for **`Sanskrit`**, select **`medhA`** keyboard, and click **Done**.

---

### Method C: Homebrew Cask

Install directly via terminal using Homebrew:

```bash
brew tap lalitaalaalitah/tap
brew install --cask medha-keyboard
```

---

### Method D: Declarative Nix Setup (`nix-darwin`)

For users managing macOS via `nix-darwin`:

```nix
# In your flake.nix inputs:
inputs.medhA-keyboard.url = "github:lalitaalaalitah/medhA-keyboard_layout";

# In system packages / darwin module:
environment.systemPackages = [ inputs.medhA-keyboard.packages.aarch64-darwin.default ];
```

---

## 3. Activating the Keyboard in System Settings

1. Open **System Settings** (or **System Preferences** on macOS Monterey and earlier) -> **Keyboard** -> **Input Sources**.
2. Click **+** (Add Input Source).
3. Search for **`Sanskrit`** or **`English (US)`**.
4. Select **`medhA-macOSX-v7`** (or `medhA`) and click **Add**.
5. Switch between keyboard layouts using **`Control + Space`** or the Globe key.

![medhA 1.7 Installed in System Settings](../screenshots/medhA_macOS/medhA_1.7_Installed.png)

---

## 4. Official Visual Layout Maps

Here are the official keymap layer images captured directly from macOS Keyboard Viewer for version 1.7:

### 4.1 Normal / Unshifted State
Default key placements for matras, primary consonants, anusvara, and visarga.

![medhA 1.7 Keyboard Viewer Normal](../screenshots/medhA_macOS/medhA_1.7_normal.png)

---

### 4.2 Shift State
Holding **`Shift`** accesses full vowels (अ, आ, इ, ई, उ, ऊ, ऋ, ॠ), aspirated consonants (ख, घ, छ, झ, ठ, ढ, थ, ध, फ, भ), and double danda (॥).

![medhA 1.7 Keyboard Viewer Shift](../screenshots/medhA_macOS/medhA_1.7_shift.png)

---

### 4.3 Caps Lock State
Turning on **`CapsLock`** locks the layout into uppercase / Shifted Devanagari mappings for continuous typing.

![medhA 1.7 Keyboard Viewer CapsLock](../screenshots/medhA_macOS/medhA_1.7_CapsLock.png)

---

### 4.4 Caps Lock + Shift State
Combining **`CapsLock + Shift`** dynamically inverts the state back to unshifted matras and consonants.

![medhA 1.7 Keyboard Viewer CapsLock Shift](../screenshots/medhA_macOS/medhA_1.7_CapsLock_Shift.png)

---

## 5. Quick Typing Formatting Reference

| Action | Key Combination | Output Result |
| :--- | :--- | :--- |
| **Virama / Halanta** | `,` (comma) | **्** (e.g. `k` + `,` + `t` -> **क्त**) |
| **Anusvara** | `.` (period) | **ं** |
| **Visarga** | `/` (slash) | **ः** |
| **Single Danda** | `Shift + /` | **।** |
| **Double Danda** | `Shift + .` | **॥** |

---

## 6. What's Next for Version 8.0.0

In current macOS v1.7, the **`Option (⌥)`** key layer is unmapped, whereas Linux `sa` and Windows `medhA-6` use AltGr for Vedic accents (`U+0951`, `U+0952`, `U+1CDA`). The upcoming **Version 8.0.0** release will align the `Option` key on macOS to output Vedic accents, achieving 100% parity across macOS, Linux, and Windows!

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
