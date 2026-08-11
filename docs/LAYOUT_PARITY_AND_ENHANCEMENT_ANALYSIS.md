# [TODO] Layout Parity & Character Mapping Enhancement Analysis

**Author**: `lalitaalaalitah`  
**Website**: https://www.lalitaalaalitah.com  
**GitHub Repository**: https://github.com/lalitaalaalitah/medhA-keyboard_layout  
**Status**: TODO / Design Specification Draft for Next Major Release  

---

## 1. Executive Summary

The `medhA` keyboard layout provides an intuitive Sanskrit typing interface across macOS, Linux, and Windows. However, historical development of the three platform editions has led to minor differences in character availability, modifier assignments (AltGr vs Option vs Ctrl-Shift), and Vedic accent placements.

This document serves as the exhaustive audit of existing character mappings and outlines the enhancement roadmap to achieve **100% layout parity** and **enhanced Vedic Unicode coverage** in a future release.

---

## 2. Comprehensive Character Audit Matrix (Current Status)

### 2.1 Core Consonants & Vowels (Common Across Platforms)

| Key | Default (Unshifted) | Shifted | Unicode Points | Description |
| :--- | :--- | :--- | :--- | :--- |
| `a` | ा (Matra AA) | अ (Short A) | `U+093E`, `U+0905` | Vowel A / Matra |
| `,` | ् (Virama/Halanta) | आ (Long AA) | `U+094D`, `U+0906` | Virama / Vowel AA |
| `i` | षि (Matra I) | इ (Short I) | `U+093F`, `U+0907` | Vowel I / Matra |
| `e` | ी (Matra II) | ई (Long II) | `U+0940`, `U+0908` | Vowel II / Matra |
| `u` | ु (Matra U) | ू (Long UU) | `U+0941`, `U+0942` | Vowel U / Matra |
| `1` | १ (Numeral 1) | उ (Short U) | `U+0967`, `U+0909` | Numeral 1 / Vowel U |
| `2` | २ (Numeral 2) | ऊ (Long UU) | `U+0968`, `U+090A` | Numeral 2 / Vowel UU |
| `r` | र (Ra) | ऋ (Vocalic R) | `U+0930`, `U+090B` | Consonant Ra / Vowel R |
| `k` | क (Ka) | ख (Kha) | `U+0915`, `U+0916` | Guttural Stops |
| `g` | ग (Ga) | घ (Gha) | `U+0917`, `U+0918` | Guttural Mediae |
| `m` | म (Ma) | ङ (Nga) | `U+092E`, `U+0919` | Nasals |
| `c` | च (Ca) | छ (Cha) | `U+091A`, `U+091B` | Palatal Stops |
| `j` | ज (Ja) | झ (Jha) | `U+091C`, `U+091D` | Palatal Mediae |
| `;` | ञ (Nya) | — | `U+091E` | Palatal Nasal |
| `t` | त (Ta) | ट (Tta) | `U+0924`, `U+091F` | Dental / Retroflex Stop |
| `d` | द (Da) | ड (Dda) | `U+0926`, `U+0921` | Dental / Retroflex Mediae |
| `n` | न (Na) | ण (Nna) | `U+0928`, `U+0923` | Dental / Retroflex Nasal |
| `p` | प (Pa) | — | `U+092A` | Labial Stop |
| `f` | फ (Pha) | — | `U+092B` | Labial Aspirate |
| `b` | ब (Ba) | भ (Bha) | `U+092C`, `U+092D` | Labial Mediae |
| `s` | स (Sa) | श (Sha) | `U+0938`, `U+0936` | Sibilants |
| `x` | ष (Ssha) | — | `U+0937` | Retroflex Sibilant |
| `h` | ह (Ha) | — | `U+0939` | Glottal |
| `.` | ं (Anusvara) | ॥ (Double Danda) | `U+0902`, `U+0965` | Anusvara / Punctuation |
| `/` | ः (Visarga) | । (Danda) | `U+0903`, `U+0964` | Visarga / Danda |

---

## 3. Discrepancies & Platform Parity Analysis

### 3.1 AltGr / Option Layer Mapping Discrepancies
- **Linux (`sa`)**:
  - Leverages Level 3 AltGr modifier for Vedic Accents (`U+0951`, `U+0952`, `U+1CDA`, `U+1CF2`, `U+1CF5`, `U+1CF6`).
  - Includes Jihvamuliya (`U+1CF5` / `U+1CF4`) and Upadhmaniya (`U+1CF6`).
- **macOS (`medhA-macOSX-v_1.7.bundle`)**:
  - **Empirical Finding**: Option (`⌥`) and Shift+Option (`⇧⌥`) keys currently produce no output in macOS v1.7.
  - **Action Required**: Map Option and Shift+Option layers in macOS `keylayout` XML to mirror Linux AltGr Vedic accents (`U+0951`, `U+0952`, `U+1CDA`, etc.) during the upcoming Version 8.0.0 alignment.
- **Windows (`medha-6.exe`)**:
  - Uses AltGr / Shift+AltGr layer for extended diacritics.

---

## 4. Enhanced Vedic & Devanagari Unicode Expansion Plan [TODO]

To make `medhA` the premier layout for classical and Vedic Sanskrit typography across all OS platforms, the following additions will be incorporated in the next version:

### Proposed Additional Unicode Characters
1. **Vedic Svaras (Accents)**:
   - `U+0951` (॑ Devanagari Stress Sign Datta)
   - `U+0952` (॒ Devanagari Stress Sign Anudatta)
   - `U+1CD0` (᳐ Vedic Tone Karshana)
   - `U+1CD2` (᳒ Vedic Tone Precharya)
   - `U+1CDA` (᳚ Vedic Tone Triple Udatta)
   - `U+1CF2` (ᳲ Vedic Sign Ardhavisarga)
2. **Vedic Nasal Signs**:
   - `U+1CF5` (ᳵ Vedic Sign Jihvamuliya)
   - `U+1CF6` (ᳶ Vedic Sign Upadhmaniya)
   - `U+A8F3` (ꣳ Devanagari Sign Candrabindu Virama)
3. **Special Numerals & Symbols**:
   - Standardizing Devanagari digits `०-९` (`U+0966`-`U+096F`) across Shift/AltGr rows on all 3 platforms.
   - Adding `U+093D` (ऽ Avagraha) on `-` key across all platforms.

---

## 5. Action Items for Next Version Bump

- [ ] Align XML keymaps in macOS `medhA.keylayout`, Linux XKB `sa`, and Windows layout project.
- [ ] Verify keyboard viewer preview images across macOS, Linux (GNOME/KDE), and Windows.
- [ ] Test typing of complex Vedic texts (e.g. Rigveda/Yajurveda samhita texts) using the unified layout.
