# medhA Sanskrit Keyboard Layout – The Definitive Guide & Multi-Platform Manual

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**Published on**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)  
**GitHub Repository**: [github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

---

## 1. What is medhA?

**`medhA`** is a high-efficiency, phonetically intuitive Devanagari keyboard layout developed by **lalitaalaalitah** for Sanskrit, Hindi, Marathi, Nepali, and other languages written in the Devanagari script.

Unlike cumbersome traditional layouts, `medhA` maps Devanagari characters according to their **phonetic acoustic similarity** to standard QWERTY keys, making typing instant and natural for anyone accustomed to an English keyboard.

### Supported Languages & Scripts
`medhA` supports full Devanagari typography for:
- **Primary Languages**: Sanskrit (Classical & Vedic), Hindi, Marathi, Nepali.
- **Regional & Historical Languages**: Newari, Maithili, Bhojpuri, Konkani, Marwari, Magahi, Gujari, Pahari (Garhwali & Kumaoni), Bhili, Santhali, Tharu, Sindhi, Sherpa, Kashmiri, and historical Devanagari-written Gujarati.

---

## 2. Phonetic Design Philosophy & Scheme

The `medhA` layout design relies on three core principles:

1. **Phonetic Key Sound Matching**: Devanagari letters are placed on QWERTY keys matching their primary phonetic sound:
   - `a` -> **ा** (Matra AA) / **अ** (Vowel A)
   - `k` -> **क** (Ka) / **ख** (Kha)
   - `g` -> **ग** (Ga) / **घ** (Gha)
   - `t` -> **त** (Ta) / **ट** (Tta)
   - `d` -> **द** (Da) / **ड** (Dda)
   - `b` -> **ब** (Ba) / **भ** (Bha)
2. **Frequency-Based Shift Placement**: Sanskrit does not distinguish between uppercase and lowercase letters. `medhA` leverages the `Shift` key to map less frequent aspirated stops, vocalic vowels, and punctuation without sacrificing typing speed:
   - Unshifted -> Most frequent character (e.g., `k` -> **क**)
   - Shifted -> Aspirated variant or full vowel (e.g., `Shift + k` -> **ख**)
3. **Ligature & Form Control**: Provides explicit control over half-letters, complex ligatures, and Vedic accents.

---

## 3. Special Characters & Advanced Devanagari Formatting

### 3.1 Virama / Halanta, Anusvara & Visarga
- **Virama / Halanta (्)**: Type `,` (comma). Used to suppress inherent vowels and construct conjunct consonants (e.g., `k` + `,` + `t` -> **क्त**).
- **Anusvara (ं)**: Type `.` (period).
- **Visarga (ः)**: Type `/` (slash).
- **Single Danda (।)**: Type `Shift + /`.
- **Double Danda (॥)**: Type `Shift + .`.

### 3.2 Zero-Width Joiner (ZWJ) & Zero-Width Non-Joiner (ZWNJ)
- **Zero-Width Joiner (ZWJ)**: Forces half-consonants to remain in half-form without forming complex ligatures. Also used to write Marathi and Newari half-Ra (**र्‌क** = `r` + `,` + `ZWJ` + `k`).
- **Zero-Width Non-Joiner (ZWNJ)**: Displays consonants with a visible Virama symbol (**क्‌त** = `k` + `,` + `ZWNJ` + `t`) instead of merging them into ligatures. Essential for readers who prefer clean, un-entangled consonant representations.

### 3.3 Vedic Accents (Svaras)
`medhA` includes native support for Vedic text composition:
- **Udatta (॑)**: `U+0951` (Devanagari Stress Sign Datta)
- **Anudatta (॒)**: `U+0952` (Devanagari Stress Sign Anudatta)
- **Swarita / Triple Udatta (᳚)**: `U+1CDA` / `U+0951`

---

## 4. Multi-Platform Installation Guides

### 4.1 macOS Installation
1. Download **`medhA-keyboard-macOS-v1.7.dmg`** from [GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Double-click the DMG and drag **`medhA-macOSX-v_1.7.bundle`** into the **`Keyboard Layouts`** shortcut folder (links to `/Library/Keyboard Layouts`).
3. Go to **System Settings** -> **Keyboard** -> **Input Sources**, click **+**, and add **`medhA-macOSX-v7`**.

#### Homebrew & Nix on macOS
- **Homebrew Cask**: `brew install lalitaalaalitah/tap/medha-keyboard`
- **Nix Flake**: Add `inputs.medhA-keyboard.packages.aarch64-darwin.default` to your `nix-darwin` configuration.

![medhA 1.7 DMG Installer](../screenshots/medhA_macOS/medhA_1.7_Installer.png)
![medhA 1.7 Installed in System Settings](../screenshots/medhA_macOS/medhA_1.7_Installed.png)

---

### 4.2 Linux Installation (Debian, Ubuntu, Pop!_OS, Arch, Manjaro, Fedora, NixOS)
1. Download `medhA-keyboard-Linux.tar.gz` and extract it:
   ```bash
   tar -xvf medhA-keyboard-Linux.tar.gz
   cd Linux
   sudo ./install.sh
   ```
2. **Desktop Activation**:
   - **GNOME (Ubuntu / Debian / Pop!_OS / Fedora)**: Settings -> Keyboard -> Input Sources -> Add **Sanskrit (medhA)**.
   - **KDE Plasma (Arch / Manjaro)**: System Settings -> Keyboard -> Layouts -> Add **sa**.
   - **CLI Test**: `setxkbmap -layout 'us,sa'`
   - **NixOS**:
     ```nix
     services.xserver.xkb.extraLayouts.medhA = {
       description = "medhA Sanskrit Keyboard Layout";
       languages = [ "sa" ];
       symbolsFile = ./Linux/sa;
     };
     ```

---

### 4.3 Windows Installation (Windows 10 / 11)
1. Download `medhA-keyboard-Windows.zip`.
2. Extract the archive and run `medha-6.exe`.
3. Switch input layouts using `Win + Space` or `Alt + Shift`.

---

## 5. Official Visual Keymaps

Captured directly from the macOS Keyboard Viewer for version 1.7:

### 5.1 Default (Unshifted) State
![medhA 1.7 Keyboard Viewer Normal](../screenshots/medhA_macOS/medhA_1.7_normal.png)

### 5.2 Shifted State
![medhA 1.7 Keyboard Viewer Shift](../screenshots/medhA_macOS/medhA_1.7_shift.png)

### 5.3 CapsLock State
![medhA 1.7 Keyboard Viewer CapsLock](../screenshots/medhA_macOS/medhA_1.7_CapsLock.png)

---

## 6. Open Source & Release Downloads

All source code, keyboard layouts, packaging scripts, and Nix expressions are available under the open-source MIT license on GitHub:

- **GitHub Repository**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)
- **Latest Releases**: [https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases)
- **Author Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)
