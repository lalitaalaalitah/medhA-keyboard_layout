# medhA Sanskrit Keyboard Layout for Windows (Definitive Guide & Setup)

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**Original Articles**:  
- [medhA-6 Unicode Sanskrit Layout Detailed Guide](https://eng.lalitaalaalitah.com/medha-keyboard-layout-sanskrit/medha-6-unicode-sanskrit-keyboard-layou/)  
- [medhA - Unicode Sanskrit Keyboard Layout for Windows](https://code.lalitaalaalitah.com/medha-6-unicode-sanskrit-keyboard-layou/)  
- [medhA Keyboard Layout Sanskrit Overview](https://eng.lalitaalaalitah.com/medha-keyboard-layout-sanskrit)  
- [Scheme for medhA 3](https://eng.lalitaalaalitah.com/scheme-for-medha-3)  
- [medhA 3 in Single Bundle](https://code.lalitaalaalitah.com/medha-3-in-single-bundle/)  
- [देवनागरी लिपि – मेधा (Hindi Language User Guide)](https://shaastrapriyaah.lalitaalaalitah.com/blog-post_28-4/)  
**Published on**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)  
**GitHub Repository**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

> 📌 **Website Publication Source**: This page is the dedicated Windows installation guide published on **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)**. For the canonical living Master Guide, see **[MEDHA_KEYBOARD_MASTER_GUIDE.md](../MEDHA_KEYBOARD_MASTER_GUIDE.md)**.

---

## 1. What is medhA for Windows & What is Its Purpose?

**`medhA`** is a keyboard-layout program (a software utility) for Microsoft Windows that maps [Devanagari](http://en.wikipedia.org/wiki/Devanagari) script letters to your conventional English QWERTY keyboard. It is designed to make you able to write [Sanskrit](http://en.wikipedia.org/wiki/Sanskrit), Hindi, Marathi, Nepali, and all other languages written in the Devanagari script natively on Windows OS (starting from Windows XP through Windows 11).

Unlike cumbersome traditional typewriter layouts (such as InScript), `medhA` integrates seamlessly into Windows as a native input method without requiring third-party background resident programs.

---

## 2. Supported Languages & Regional Scripts

Devanagari is used to write numerous classical, modern, and regional languages. With `medhA` keyboard layouts, you can write all of these in full Devanagari script:
- **Primary Languages**: Sanskrit (Classical & Vedic), Hindi, Marathi, Nepali.
- **Regional & Historical Languages**: Newari, Magahi, Maithili, Bhojpuri, Gujari, Pahari (Garhwali & Kumaoni), Konkani, Marwari, Bhili, Santhali, Tharu.
- **Occasionally Devanagari-written**: Sindhi, Sherpa, and Kashmiri. Formerly, Devanagari was used to write Gujarati as well.

---

## 3. Development History & Sound-Based Design Scheme

`medhA` for Windows was originally developed using **MSKLC** ([Microsoft Keyboard Layout Creator](http://msdn.microsoft.com/en-us/goglobal/bb964665)). 

### Phonetic Acoustic Matching Principle
Devanagari letters are kept strictly according to sound. That means a Sanskrit letter similar to an English letter in sound is mapped on the same key:
- **`अ`** is kept with **`a`**
- **`ब`** is kept with **`b`**
- Both **`द`** and **`ड`** are similar to **`d`** in sound, so they are kept on the same key **`d`**.
- Similarly, **`ब`**, **`भ`**, and **`b`** share a key; **`क`**, **`ख`**, and **`k`** share a key; and so on.

### Frequency-Based Shift Placement & Sanskrit's Case Advantage
Even after completing the sound-matching process, some letters remained in the bag. These remaining letters were mapped according to **frequency of use**. 

When two letters are assigned to the same physical key, the more frequently used or more phonetically similar letter is assigned directly to the unshifted keypress, while the less used or less similar letter is assigned to the **`Shift`** key layer.

> *Thanks to Sanskrit for not having a distinction between small and capital letters!* In an English keyboard, capital and small letters share the same key, requiring `Shift` or `Caps Lock` to switch between them. `medhA` utilizes this exact mechanism for Sanskrit letters sharing a key. One letter is used directly, and to use the secondary letter, you switch in the exact same way with `Shift` or `CapsLock`.

---

## 4. Advantages of the Sound-Based Scheme

Keeping letters according to sound is the key to making the keyboard intuitive and easy to use. 

### Why Sound Mapping Solves Keycap Invisibility
Even after mapping Devanagari characters to a keyboard, the primary obstacle is that **we do not see Devanagari characters printed on our physical keycaps**, making their use difficult. Users are traditionally forced to remember arbitrary key positions—a major problem if there is no logical clue to the mapping style.

Mapping according to sound solves this completely:
* Anyone who uses Sanskrit and English is already familiar with the phonetic sounds of both languages.
* Once you understand the sound-matching method adapted during mapping, remembering the position of letters becomes simple and natural without needing physical key stickers or on-screen cheat sheets.
* For visual guidance, keyboard layout diagrams are provided showing direct letters (unshifted) and secondary letters requiring the `Shift` key.

---

## 5. Evolution of medhA 3 & medhA 6

Older versions of `medhA` worked fine and remain the base of this keyboard layout series. However, as typing needs expanded, version updates introduced powerful new layers while strictly retaining the core phonetic mapping:

### 5.1 Special Typographic Controls in medhA 3:
- **`Ctrl + Shift + 1`**: Zero-Width Joiner (**ZWJ**)
- **`Ctrl + Shift + 2`**: Zero-Width Non-Joiner (**ZWNJ**)
- **`Ctrl + Shift + 3`**: Vedic Udatta (**॑** - `U+0951`)
- **`Ctrl + Shift + 4`**: Vedic Anudatta (**॒** - `U+0952`)
- **`Ctrl + Shift + 5`**: Vedic Swarita / Triple Udatta (**᳚** - `U+1CDA` / `U+0951`)

### 5.2 AltGr Layer & Symbol Enhancements in medhA 6:
Version 6 of `medhA` for Unicode Sanskrit built directly upon `medhA 3`, maintaining 100% phonetic sound continuity while introducing dedicated **AltGr (Right Alt)** key combinations:
- **Punctuation & Currency without Layout Switching**:
  - **Full Stop (`.`)**: `AltGr + .`
  - **Comma (`,`)**: `AltGr + ,`
  - **Indian Rupee Sign (`₹`)**: `AltGr + Shift + 4` / `AltGr + R`
  - **Exclamation Mark (`!`)**: `AltGr + !`
- **Direct AltGr Devanagari & Vedic Character Mappings**:
  - **`AltGr + a`**: Zero-Width Joiner (**ZWJ**)
  - **`AltGr + b`**: Zero-Width Non-Joiner (**ZWNJ**) / Dviswarita (**द्विस्वरित - ᳚**)
  - **`AltGr + z`**: Chandrabindu Virama (**चन्द्रबिन्दु विराम**)
  - **`AltGr + x`**: Vedic Udatta (**उदात्त - ॑**)
  - **`AltGr + c`**: Vedic Anudatta (**अनुदात्त - ॒**)
  - **`AltGr + v`**: Yojaka / Hyphen (**योजक - ⸗ / -**)
  - **`AltGr + n`**: Vedic Triswarita (**त्रिस्वरित - ᳛ / ᳚**)
- **Single Executable Package**: Distributed as a direct installer executable (**`medha-6.exe`**) available in the repository under [`Windows/`](https://github.com/lalitaalaalitah/medhA-keyboard_layout/tree/master/Windows).

---

## 6. How To Use Special Combinations & Linguistic Rationale

> 🇮🇳 **Hindi Language Guide (हिन्दी माध्यम)**: A dedicated user guide in Hindi detailing Devanagari character input, संयुक्ताक्षर (conjunct consonants), and Marathi/Nepali half-Ra typing is available at **[देवनागरी लिपि – मेधा (शास्त्राप्रियाः)](https://shaastrapriyaah.lalitaalaalitah.com/blog-post_28-4/)**.

### 6.1 Zero-Width Joiner (ZWJ - `Ctrl + Shift + 1` or `AltGr + a`)
The Zero-Width Joiner is a non-visible formatting character used to write half-letters:
- **Half-Letter Typing**: `k` + `,` (Virama) + `Ctrl+Shift+1` (or `AltGr+a`) + `t` = **क + ् + ZWJ + त = क्‌त**
- **Special Use (Newari & Marathi Half-Ra)**: Used to write Newari or Marathi half-Ra (**र्‌क**):
  - `r` + `,` (Virama) + `ZWJ` + `k` = **र्‌क**

### 6.2 Zero-Width Non-Joiner (ZWNJ - `Ctrl + Shift + 2` or `AltGr + b`)
The Zero-Width Non-Joiner is used to write consonants with a visible Virama/Halanta symbol (**क्‌त**):
- **Explicit Virama Typing**: `k` + `,` (Virama) + `Ctrl+Shift+2` (or `AltGr+b`) + `t` = **क + ् + ZWNJ + त = क्‌त**

### 6.3 Standard Ligature (Default)
If you do not use ZWJ or ZWNJ, typing consonants with Virama forms standard merged ligatures:
- **Standard Ligature**: `k` + `,` (Virama) + `t` = **क + ् + त = क्त**

### 6.4 Vedic Accents (Udatta, Anudatta, Swarita)
- **Udatta (॑)**: `Ctrl + Shift + 3` or `AltGr + x`
- **Anudatta (॒)**: `Ctrl + Shift + 4` or `AltGr + c`
- **Swarita / Triswarita**: `Ctrl + Shift + 5` or `AltGr + n`

### Who Should Use ZWJ & ZWNJ?
Unicode fonts (such as *Sanskrit2003*) support many complex ligatures. Some of these ligatures are very rarely used, and many readers find them strange or difficult to read. Those who do not want to use complex ligatures can use the Zero-Width Joiner or Non-Joiner to keep all combining consonants clear and visible in a simple way. (For more technical details on Unicode joining behavior, see [Unicode Standard Joining Rules](https://unicode.org/standard/where/)).

---

## 7. Self-Guided Testing & Keyboard Practice Workflow

To quickly familiarize yourself with `medhA-6` on Windows:

1. **Install Software**: Download `medhA-keyboard-Windows.zip` and double-click `medha-6.exe`.
2. **Open Document Editor**: Launch MS Word, Notepad, or LibreOffice Writer.
3. **Toggle Input Language**: Press **`Ctrl + Shift`** (or **`Left Alt + Left Shift`**) to switch the active keyboard layout to Sanskrit/medhA.
4. **Test Key Layers Systematically**:
   - **Test Unshifted Layer**: Press each letter key directly and observe the printed letter (`k` -> क, `g` -> ग, `t` -> त, `d` -> द).
   - **Test Shift Layer**: Hold down **`Shift`** and press each key. Observe the aspirated consonants and full vowels (`Shift+k` -> ख, `Shift+g` -> घ).
   - **Test AltGr Layer**: Press **`AltGr`** (the Alt key on the right-hand side of the keyboard) and press keys (`AltGr + .` -> `.`, `AltGr + ,` -> `,`, `AltGr + x` -> `॑`, `AltGr + c` -> `॒`).
   - **Test Shift + AltGr Layer**: Hold **`Shift + AltGr`** and test additional signs.
5. **Compare with Layout Pictures**: Compare the text on your screen with the official layout images. Remembering key positions is easy because sound matching aligns letters naturally!

---

## 8. Software Format Evolution & Download Instructions

### Historical Format Note
* Early versions of `medhA` were compressed in [.iso](http://en.wikipedia.org/wiki/ISO_image) format and hosted on Google Groups (which is now defunct).
* Downloading the `.iso` file required opening tools like WinRAR, 7-Zip, or [PowerISO](http://www.poweriso.com/download.htm) to extract `setup.exe`.
* *(If downloads failed or opened unorganized text in old browsers, users were advised to right-click and choose "Save linked content".)*

### Modern Executable (.exe) Format
* This has been upgraded! Modern releases package everything into a single-click executable (**`medha-6.exe`** / **`setup.exe`** inside `medhA-keyboard-Windows.zip`).
* A simple double-click on the `.exe` file installs the keyboard for you automatically—much easier than before!

> 📥 **Download Link**: Download `medhA-keyboard-Windows.zip` / `medha-6.exe` directly from **[GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases)** or **[code.lalitaalaalitah.com](https://code.lalitaalaalitah.com/medha-6-unicode-sanskrit-keyboard-layou/)**.

---

## 9. System Requirements & Windows Compatibility

`medhA` is fully compatible across all versions of Microsoft Windows (32-bit, 64-bit, and ARM64 architecture):
- **Modern Windows**: Windows 11, Windows 10
- **Legacy Windows**: Windows 8.1, Windows 8, Windows 7, Windows Vista, Windows XP

---

## 10. Step-by-Step Installation & Setup

### Modern Windows (Windows 10 & 11)

1. Download **`medhA-keyboard-Windows.zip`** from [GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Right-click `medhA-keyboard-Windows.zip` and select **Extract All...** (or run PowerShell: `Expand-Archive -Path medhA-keyboard-Windows.zip -DestinationPath .`).
3. Open the extracted folder and double-click **`medha-6.exe`** (or `setup.exe`).
4. Wait for confirmation of successful installation. The setup wizard copies DLL files to `%SystemRoot%\System32\` and registers `medhA`. Click **Close**.

### Activating the Layout in Windows Settings
1. Open **Settings** (`Win + I`) -> **Time & Language** -> **Language & Region**.
2. Click **Add a language**, search for **Sanskrit** (or **Hindi**), and click **Next** -> **Install**.
3. Click **...** (Options) next to Sanskrit -> **Keyboards** -> **Add a keyboard**.
4. Select **`medhA`** (or `Sanskrit2003` / `medhA-6`) from the layout list.

### Switching Between Keyboards
- **`Win + Spacebar`**: Opens visual input switcher overlay.
- **`Left Alt + Left Shift`**: Toggles instantly between English and `medhA` Sanskrit layouts.

---

### Legacy Windows Setup (Windows XP, Vista, Windows 7)

#### In Windows Vista & Windows 7:
1. Double-click `medha-6.exe` (or `setup.exe`) to install.
2. Open MS Office, Notepad, or any editor software.
3. Press **`Left Shift + Left Alt`** together to switch to `medhA` Devanagari input.

#### In Windows XP:
1. Enable Unicode Complex Script Support:
   * Open **Control Panel** -> **Date, Time, Language, and Regional Options**.
   * Click on the **Languages** tab.
   * Check **"Install files for complex script and right to left languages"**. Click **Apply** (insert Windows XP CD if prompted).
2. Add Keyboard & Language:
   * Press **Details...** button.
   * Click **Add**, choose **Hindi** or **Sanskrit** (or any language written in Devanagari).
   * Under **Keyboard layout/IME**, select **`medhA`** (or `Sanskrit2003`). Click **OK**.
   * Ensure English or your desired default layout is set as primary.
3. Language Bar Preferences:
   * Under **Preferences**, press the **Language Bar** button and choose your desired options.
   * Exit Control Panel and start typing in `medhA` using **`Left Shift + Left Alt`**. (Change font to a desired Unicode font in Notepad or Word).
   * *(For visual snapshots of legacy XP setup, refer to historical guides at [Azhagi Unicode Setup](http://www.azhagi.com/uniset.html) and [Muhammadanism XP Unicode Setup](http://www.muhammadanism.org/Unicode/WindowsXP.htm)).*

---

## 11. Recommended Unicode Fonts

To ensure proper rendering of complex Devanagari conjuncts, ligatures, and Vedic accents in Windows applications (Word, Notepad, TeX), install a high-quality [Unicode font](http://en.wikipedia.org/wiki/Unicode_typeface). The primary recommended Devanagari Unicode font is:

- **Adishila** (Primary Recommended Font, available at [adishila.com/fonts](https://adishila.com/fonts/))
- **Sanskrit2003** ([sanskritweb.net](http://www.sanskritweb.net/itrans/sans2003.zip))
- **Siddhanta** / **Noto Serif Devanagari** / **Gargi** / **Chandas**

---

## 12. Complete Typing Reference Table

| Action / Character | Key Combination | Devanagari Output |
| :--- | :--- | :--- |
| **Virama / Halanta** | `,` (comma) | **्** (e.g. `k` + `,` + `t` -> **क्त**) |
| **Anusvara** | `.` (period) | **ं** |
| **Visarga** | `/` (slash) | **ः** |
| **Single Danda** | `Shift + /` | **।** |
| **Double Danda** | `Shift + .` | **॥** |
| **Zero-Width Joiner (ZWJ)** | `Ctrl + Shift + 1` / `AltGr + a` | Half-consonant / **र्‌क** (Marathi & Newari half-Ra) |
| **Zero-Width Non-Joiner (ZWNJ)** | `Ctrl + Shift + 2` / `AltGr + b` | **क्‌त** (Explicit Virama form) |
| **Chandrabindu Virama** | `AltGr + z` | **ꣳ / 🛑** (Chandrabindu Virama) |
| **Vedic Udatta** | `Ctrl + Shift + 3` / `AltGr + x` | **॑** (`U+0951`) |
| **Vedic Anudatta** | `Ctrl + Shift + 4` / `AltGr + c` | **॒** (`U+0952`) |
| **Yojaka / Hyphen** | `AltGr + v` | **⸗ / -** |
| **Vedic Dviswarita** | `AltGr + b` | **᳚** |
| **Vedic Swarita / Triswarita** | `Ctrl + Shift + 5` / `AltGr + n` | **᳛ / ᳚** |
| **Full Stop** | `AltGr + .` | **.** |
| **Comma** | `AltGr + ,` | **,** |
| **Exclamation Mark** | `AltGr + !` | **!** |
| **Indian Rupee Sign** | `AltGr + Shift + 4` / `AltGr + R` | **₹** |

---

## 13. Uninstallation & Re-installation

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
