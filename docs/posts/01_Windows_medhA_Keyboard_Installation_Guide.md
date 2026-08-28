# medhA Sanskrit Keyboard Layout for Windows (Definitive Guide & Setup)

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**Original Articles**:  
- [medhA - Unicode Sanskrit Keyboard Layout for Windows](https://code.lalitaalaalitah.com/medha-6-unicode-sanskrit-keyboard-layou/)  
- [medhA 3 in Single Bundle](https://code.lalitaalaalitah.com/medha-3-in-single-bundle/)  
**Published on**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)  
**GitHub Repository**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

> 📌 **Website Publication Source**: This page is the dedicated Windows installation guide published on **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)**. For the canonical living Master Guide, see **[MEDHA_KEYBOARD_MASTER_GUIDE.md](../MEDHA_KEYBOARD_MASTER_GUIDE.md)**.

---

## 1. What is medhA for Windows & What is Its Purpose?

**`medhA`** is a lightweight, high-efficiency keyboard layout program for Microsoft Windows that maps [Devanagari](https://en.wikipedia.org/wiki/Devanagari) script characters to your conventional English QWERTY keyboard. It enables scholars, researchers, developers, and students to write [Sanskrit](https://en.wikipedia.org/wiki/Sanskrit), Hindi, Marathi, Nepali, Newari, Maithili, Bhojpuri, Konkani, and other Devanagari-script languages naturally and rapidly.

Unlike cumbersome traditional typewriter layouts (such as InScript), `medhA` integrates seamlessly into Windows as a native input method without requiring third-party background software or resident applications.

---

## 2. Supported Languages & Regional Scripts

`medhA` supports full Devanagari typography for:
- **Primary Languages**: Sanskrit (Classical & Vedic), Hindi, Marathi, Nepali.
- **Regional & Historical Languages**: Newari, Maithili, Bhojpuri, Konkani, Marwari, Magahi, Gujari, Pahari (Garhwali & Kumaoni), Bhili, Santhali, Tharu, Sindhi, Sherpa, Kashmiri, and historical Devanagari-written Gujarati.

---

## 3. Development History & Sound-Based Design Scheme

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

## 4. Evolution of medhA 3 & Special Typographic Controls

While older versions of `medhA` handled basic consonants and matras, **`medhA 3`** introduced critical special control combinations for advanced Devanagari typography and Vedic texts:

### Key Combinations Introduced in medhA 3:
* **`Ctrl + Shift + 1`**: Zero-Width Joiner (**ZWJ**)
* **`Ctrl + Shift + 2`**: Zero-Width Non-Joiner (**ZWNJ**)
* **`Ctrl + Shift + 3`**: Vedic Udatta (**॑** - `U+0951`)
* **`Ctrl + Shift + 4`**: Vedic Anudatta (**॒** - `U+0952`)
* **`Ctrl + Shift + 5`**: Vedic Swarita / Triple Udatta (**᳚** - `U+1CDA` / `U+0951`)

---

## 5. Typographic Formatting & Linguistic Rationale

### 5.1 Zero-Width Joiner (ZWJ - `Ctrl + Shift + 1`)
Used to write half-consonants without allowing them to merge into complex ligatures:
- **Half-Letter Typing**: `k` + `,` + `Ctrl+Shift+1` + `t` = **क्‌त**
- **Special Use (Marathi & Newari Half-Ra)**: Used to compose the distinctive Marathi and Newari half-Ra (**र्‌क**):
  - Typing `r` + `,` (Virama) + `Ctrl+Shift+1` (ZWJ) + `k` = **र्‌क**

### 5.2 Zero-Width Non-Joiner (ZWNJ - `Ctrl + Shift + 2`)
Used to render consonants with an explicit, visible Virama/Halanta symbol (**क्‌त**):
- **Explicit Virama Typing**: `k` + `,` + `Ctrl+Shift+2` + `t` = **क्‌त**

### 5.3 Default Conjunct Ligatures
Without ZWJ or ZWNJ, typing consonants separated by Virama produces standard merged ligatures:
- **Standard Ligature**: `k` + `,` + `t` = **क्त**

### Why Use ZWJ & ZWNJ?
Many Unicode fonts (such as *Sanskrit2003*) include hundreds of complex historical ligatures. Some of these ligatures are rare, intricate, and difficult for modern readers to parse. Using ZWJ or ZWNJ allows readers and publishers to display clean, simple, un-entangled consonant combinations where every letter remains clear and legible.

---

## 6. Software Format Evolution & Download Details

* **Historical Note**: Early versions of `medhA` were compressed in `.iso` format and hosted on Google Groups (requiring extraction tools like WinRAR, 7-Zip, or PowerISO).
* **Modern Executable Format**: Modern releases are compiled into a direct, single-click Windows executable installer package (**`medha-6.exe`** / **`setup.exe`** inside `medhA-keyboard-Windows.zip`).

> 📥 **Latest Version Download**: Download `medhA-keyboard-Windows.zip` directly from **[GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases)** or **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com/medha-6-unicode-sanskrit-keyboard-layou/)**.

---

## 7. System Requirements & Windows Compatibility

`medhA` is compatible across all modern and legacy versions of Microsoft Windows (32-bit, 64-bit, and ARM64 architecture):
- **Modern Windows**: Windows 11, Windows 10
- **Legacy Windows**: Windows 8.1, Windows 8, Windows 7, Windows Vista, Windows XP

---

## 8. Step-by-Step Installation & Setup

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

## 9. Recommended Unicode Fonts

To ensure crisp rendering of complex Devanagari conjuncts, ligatures, and Vedic accents in Windows applications (Word, Notepad, TeX), install high-quality Devanagari Unicode typefaces such as:
- **Sanskrit2003** ([sanskritweb.net](http://www.sanskritweb.net/itrans/sans2003.zip))
- **Adishila / Siddhanta**
- **Noto Serif Devanagari** / **Gargi** / **Chandas**

---

## 10. Complete Typing Reference Table

| Action / Character | Key Combination | Devanagari Output |
| :--- | :--- | :--- |
| **Virama / Halanta** | `,` (comma) | **्** (e.g. `k` + `,` + `t` -> **क्त**) |
| **Anusvara** | `.` (period) | **ं** |
| **Visarga** | `/` (slash) | **ः** |
| **Single Danda** | `Shift + /` | **।** |
| **Double Danda** | `Shift + .` | **॥** |
| **Zero-Width Joiner (ZWJ)** | `Ctrl + Shift + 1` | Half-consonant / **र्‌क** (Marathi half-Ra) |
| **Zero-Width Non-Joiner (ZWNJ)** | `Ctrl + Shift + 2` | **क्‌त** (Explicit Virama form) |
| **Vedic Udatta** | `Ctrl + Shift + 3` | **॑** (`U+0951`) |
| **Vedic Anudatta** | `Ctrl + Shift + 4` | **॒** (`U+0952`) |
| **Vedic Swarita** | `Ctrl + Shift + 5` | **᳚** (`U+1CDA`) |

---

## 11. Uninstallation & Re-installation

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
