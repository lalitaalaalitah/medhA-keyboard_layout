# medhA Sanskrit Keyboard Layout for Windows (Definitive Guide & Setup)

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**Original Article**: [https://code.lalitaalaalitah.com/medha-6-unicode-sanskrit-keyboard-layou/](https://code.lalitaalaalitah.com/medha-6-unicode-sanskrit-keyboard-layou/)  
**Published on**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)  
**GitHub Repository**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

> 📌 **Website Publication Source**: This page is the dedicated Windows installation guide published on **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)**. For the canonical living Master Guide, see **[MEDHA_KEYBOARD_MASTER_GUIDE.md](../MEDHA_KEYBOARD_MASTER_GUIDE.md)**.

---

## 1. What is medhA for Windows & What is Its Purpose?

**`medhA`** is a lightweight, high-efficiency keyboard layout program for Microsoft Windows that maps [Devanagari](https://en.wikipedia.org/wiki/Devanagari) script characters to your conventional English QWERTY keyboard. It enables scholars, researchers, developers, and students to write [Sanskrit](https://en.wikipedia.org/wiki/Sanskrit), Hindi, Marathi, Nepali, and other Devanagari-script languages naturally and rapidly.

Unlike cumbersome traditional typewriter layouts (such as InScript), `medhA` integrates seamlessly into Windows as a native input method without requiring third-party background software or resident applications.

---

## 2. Development History & Sound-Based Design Scheme

`medhA` for Windows was originally developed using **MSKLC** ([Microsoft Keyboard Layout Creator](https://msdn.microsoft.com/en-us/goglobal/bb964665)). 

### Phonetic Acoustic Matching Principle
Devanagari letters are assigned to QWERTY keys strictly according to **phonetic sound similarity**. A Sanskrit letter that sounds similar to an English letter is mapped to that exact key:
- **`अ`** is placed on **`a`**
- **`ब`** is placed on **`b`**
- **`द`** and **`ड`** are both phonetically similar to **`d`**, so both are placed on the **`d`** key.
- **`क`** and **`ख`** are both phonetically similar to **`k`**, so both are placed on the **`k`** key.

### Leveraging Frequency & Shift Key Switching
Sanskrit has the advantage of not distinguishing between uppercase and lowercase letters. `medhA` takes advantage of this by using the **`Shift`** key to alternate between letters placed on the same key:
1. **Unshifted (Direct Keypress)**: Outputs the most frequent or primary sound variant (e.g. pressing `k` directly outputs **`क`**).
2. **Shifted (`Shift + Key`)**: Outputs the less frequent or aspirated sound variant, or full vowel (e.g. pressing `Shift + K` outputs **`ख`**).

---

## 3. Advantages of the Sound-Based Scheme

When typing Devanagari on a standard English keyboard, the primary challenge is that Devanagari letters are not printed on physical keycaps. Without a clear mapping philosophy, users are forced to memorize arbitrary key positions or rely on physical keyboard stickers.

Mapping by sound eliminates this cognitive barrier:
* Anyone who reads Sanskrit/Hindi and English is already familiar with the phonetic sounds of both alphabets.
* Once you understand the phonetic logic of `medhA`, remembering key positions becomes second nature without needing physical stickers or on-screen key lookup tables.

---

## 4. Software Format Evolution & Download Details

* **Historical Note**: Early versions of `medhA` were compressed in `.iso` format and hosted on Google Groups (requiring ISO extraction tools like WinRAR, 7-Zip, or PowerISO).
* **Modern Executable Format**: Modern releases are compiled into a direct, single-click Windows executable installer package (**`medha-6.exe`** / **`setup.exe`** inside `medhA-keyboard-Windows.zip`).

> 📥 **Latest Version Download**: Download `medhA-keyboard-Windows.zip` directly from **[GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases)** or **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com/medha-6-unicode-sanskrit-keyboard-layou/)**.

---

## 5. System Requirements & Windows Compatibility

`medhA` is compatible across all modern and legacy versions of Microsoft Windows (32-bit, 64-bit, and ARM64 architecture):
- **Modern Windows**: Windows 11, Windows 10
- **Legacy Windows**: Windows 8.1, Windows 8, Windows 7, Windows Vista, Windows XP

---

## 6. Step-by-Step Installation & Setup

### Modern Windows (Windows 10 & 11)

1. Download **`medhA-keyboard-Windows.zip`** from [GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Right-click the ZIP archive and select **Extract All...** (or extract using PowerShell: `Expand-Archive -Path medhA-keyboard-Windows.zip -DestinationPath .`).
3. Open the extracted folder and double-click **`medha-6.exe`** (or `setup.exe`).
4. If prompted by User Account Control (UAC), click **Yes**. The setup wizard will copy compiled DLL files to `%SystemRoot%\System32\` and register `medhA` in the Windows registry.
5. Click **Close** when installation succeeds.

### Activating the Layout in Windows Settings
1. Open **Settings** (`Win + I`) -> **Time & Language** -> **Language & Region**.
2. Click **Add a language**, search for **Sanskrit** (or **Hindi**), and click **Next** -> **Install**.
3. Click the **...** menu next to Sanskrit -> **Language options** -> **Keyboards** -> **Add a keyboard**.
4. Select **`medhA`** (or `Sanskrit2003` / `medhA-6`) from the list.

### Toggling Between Keyboards
- **`Win + Spacebar`**: Opens visual input switcher overlay.
- **`Left Alt + Left Shift`**: Toggles instantly between English and `medhA` Sanskrit layouts.

---

### Legacy Windows Setup (Windows XP, Vista, Windows 7)

#### In Windows Vista & Windows 7:
1. Double-click `medha-6.exe` (or `setup.exe`) to install.
2. Open Microsoft Word, Notepad, or any application.
3. Press **`Left Shift + Left Alt`** together to toggle to `medhA` Devanagari input.

#### In Windows XP:
1. Enable Unicode Complex Script Support:
   * Open **Control Panel** -> **Regional and Language Options**.
   * Select the **Languages** tab.
   * Check **"Install files for complex script and right-to-left languages (including Indic)"**. Click **Apply** (you may need the Windows XP installation CD).
2. Add Language:
   * Click **Details...** -> **Add**.
   * Choose **Hindi** or **Sanskrit** as input language.
   * Under **Keyboard layout/IME**, select **`medhA`** (or `Sanskrit2003`). Click **OK**.
3. Under **Preferences**, click **Language Bar** and configure shortcuts (`Left Alt + Left Shift`).

---

## 7. Recommended Unicode Fonts

To ensure crisp rendering of complex Devanagari conjuncts, ligatures, and Vedic accents in Windows applications (Word, Notepad, TeX), install high-quality Devanagari Unicode typefaces such as:
- **Sanskrit2003** ([sanskritweb.net](http://www.sanskritweb.net/itrans/sans2003.zip))
- **Adishila / Siddhanta**
- **Noto Serif Devanagari** / **Gargi** / **Chandas**

---

## 8. Typing Formatting Reference

| Action | Key Combination | Devanagari Output |
| :--- | :--- | :--- |
| **Virama / Halanta** | `,` (comma) | **्** (e.g. `k` + `,` + `t` -> **क्त**) |
| **Anusvara** | `.` (period) | **ं** |
| **Visarga** | `/` (slash) | **ः** |
| **Single Danda** | `Shift + /` | **।** |
| **Double Danda** | `Shift + .` | **॥** |
| **Zero-Width Joiner (ZWJ)** | `Ctrl + Shift + 1` | **र्‌क** (Marathi half-Ra) |
| **Zero-Width Non-Joiner (ZWNJ)** | `Ctrl + Shift + 2` | **क्‌त** (Explicit Virama form) |

---

## 9. Uninstallation & Re-installation

To remove `medhA` from Windows:
1. Open **Settings** -> **Apps** -> **Installed Apps** (or Control Panel -> Programs and Features).
2. Select **medhA Keyboard Layout** and click **Uninstall**.
3. For full multi-platform uninstallation guidance, see **[UNINSTALLATION_GUIDE.md](../UNINSTALLATION_GUIDE.md)**.

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
