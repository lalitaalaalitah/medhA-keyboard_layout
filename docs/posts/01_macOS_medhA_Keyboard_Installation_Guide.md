# Installing & Mastering medhA Sanskrit Keyboard Layout on macOS

**Author**: `lalitaalaalitah`  
**Website**: [https://www.lalitaalaalitah.com](https://www.lalitaalaalitah.com)  
**Published on**: [code.lalitaalaalitah.com](https://code.lalitaalaalitah.com)  
**Repository**: [github.com/lalitaalaalitah/medhA-keyboard_layout](https://github.com/lalitaalaalitah/medhA-keyboard_layout)  

---

## Introduction

The **`medhA` Sanskrit Keyboard Layout** is an intuitive, phonetically structured input layout designed for fast, accurate typing of Sanskrit, Hindi, and classical Devanagari texts. On macOS, `medhA` integrates natively into Apple's Text Input Services, giving you system-wide Devanagari typing across Xcode, VS Code, TextEdit, Pages, and terminal emulators.

This guide details the three installation methods on macOS, activation steps, and complete keymap visual references for version 1.7.

---

## 1. Installation Methods on macOS

### Method A: Drag-and-Drop Installation via DMG Disk Image (Recommended)

1. Download **`medhA-keyboard-macOS-v1.7.dmg`** from the [GitHub Releases](https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases).
2. Double-click the DMG to mount it.
3. Drag **`medhA-macOSX-v_1.7.bundle`** directly into the **`Keyboard Layouts`** shortcut folder (which links to `/Library/Keyboard Layouts`).

![medhA 1.7 DMG Installer](/Volumes/Cablet_WD_2TB_20251206/05_Development/Github/24_Keyboards/01_medhA-keyboard_layout/docs/screenshots/medhA_macOS/medhA_1.7_Installer.png)

---

### Method B: Homebrew Cask

If you use Homebrew, you can install `medhA` with a single command:

```bash
brew install lalitaalaalitah/tap/medha-keyboard
```

---

### Method C: Declarative Nix Setup (`nix-darwin`)

For users managing macOS with `nix-darwin` or Home Manager:

```nix
# In your flake.nix inputs:
inputs.medhA-keyboard.url = "github:lalitaalaalitah/medhA-keyboard_layout";

# In system configuration:
environment.systemPackages = [ inputs.medhA-keyboard.packages.aarch64-darwin.default ];
```

---

## 2. Enabling the Keyboard in System Settings

Once installed, enable the keyboard source in macOS:

1. Open **System Settings** -> **Keyboard**.
2. Under **Input Sources**, click **Edit...** (or **+**).
3. Select **Sanskrit** or **English (US)**.
4. Add **`medhA-macOSX-v7`**.

![medhA 1.7 Installed in System Settings](/Volumes/Cablet_WD_2TB_20251206/05_Development/Github/24_Keyboards/01_medhA-keyboard_layout/docs/screenshots/medhA_macOS/medhA_1.7_Installed.png)

---

## 3. Layout Maps & Keymaps

Below are the official visual layouts captured directly from macOS Keyboard Viewer for version 1.7.

### 3.1 Unshifted / Normal Layout State

The default unshifted state places matras (vowel signs) and primary consonants in intuitive QWERTY-aligned positions.

![medhA 1.7 Keyboard Viewer Normal](/Volumes/Cablet_WD_2TB_20251206/05_Development/Github/24_Keyboards/01_medhA-keyboard_layout/docs/screenshots/medhA_macOS/medhA_1.7_normal.png)

---

### 3.2 Shifted Layout State

Holding **`Shift`** accesses full vowels (अ, आ, इ, ई, उ, ऊ, ऋ, ॠ), aspirated consonants (ख, घ, छ, झ, ठ, ढ, थ, ध, फ, भ), and double danda (॥).

![medhA 1.7 Keyboard Viewer Shift](/Volumes/Cablet_WD_2TB_20251206/05_Development/Github/24_Keyboards/01_medhA-keyboard_layout/docs/screenshots/medhA_macOS/medhA_1.7_shift.png)

---

### 3.3 CapsLock Layout State

Turning on **`CapsLock`** locks the layout into uppercase / Shifted Devanagari mappings for extended typing sessions.

![medhA 1.7 Keyboard Viewer CapsLock](/Volumes/Cablet_WD_2TB_20251206/05_Development/Github/24_Keyboards/01_medhA-keyboard_layout/docs/screenshots/medhA_macOS/medhA_1.7_CapsLock.png)

---

### 3.4 CapsLock + Shift Layout State

Combining **`CapsLock + Shift`** reverts key mappings dynamically back to unshifted matra/consonant states.

![medhA 1.7 Keyboard Viewer CapsLock Shift](/Volumes/Cablet_WD_2TB_20251206/05_Development/Github/24_Keyboards/01_medhA-keyboard_layout/docs/screenshots/medhA_macOS/medhA_1.7_CapsLock_Shift.png)

---

## 4. Typing Conjuncts & Sanskrit Formatting

- **Virama / Halanta (्)**: Type `,` (comma) to join consonants into conjuncts (e.g., `k` + `,` + `t` -> `क्त`).
- **Anusvara (ं)**: Type `.` (period).
- **Visarga (ः)**: Type `/` (slash).
- **Single Danda (।)**: Type `Shift + /`.
- **Double Danda (॥)**: Type `Shift + .`.

---

## 5. Technical Note & Upcoming Version 8.0.0

During testing of macOS v1.7, it was noted that the **`Option (⌥)`** key layer is unmapped on macOS v1.7, while the Linux `sa` edition uses AltGr for Vedic accents (`U+0951`, `U+0952`, `U+1CDA`). 

This mapping will be fully aligned in the upcoming **Version 8.0.0** release across macOS, Linux, and Windows!
