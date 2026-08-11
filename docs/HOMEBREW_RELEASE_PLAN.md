# Homebrew Cask Release Strategy & Evaluation Plan

**Author**: `lalitaalaalitah`  
**Website**: https://www.lalitaalaalitah.com  
**GitHub Repository**: https://github.com/lalitaalaalitah/medhA-keyboard_layout  

---

## 1. Requirements & Feasibility Analysis

Homebrew Casks allow Mac users to install macOS `.bundle` keyboard layouts directly into `/Library/Keyboard Layouts` or `~/Library/Keyboard Layouts`.

### Requirements Checklist for Homebrew
1. **GitHub Release Release Asset**: The `.zip` or `.dmg` asset containing `medhA-macOSX-v_1.7.bundle` must be published under a GitHub release (e.g. `v1.7` or `v8.0.0`).
2. **SHA-256 Checksum**: Every released `.zip` artifact has a unique SHA-256 checksum that is specified in the Cask formula.
3. **Target Directory**: Homebrew Cask supports installing keyboard layouts directly using the `artifact` stanza targeting `/Library/Keyboard Layouts/`.

---

## 2. Option A: Publishing via Custom Tap (`lalitaalaalitah/homebrew-tap`) [RECOMMENDED]

Creating a personal tap repository `homebrew-tap` under `github.com/lalitaalaalitah/homebrew-tap` is the most straightforward and flexible approach.

### Setup Steps for Custom Tap:
1. Create a public repository named `homebrew-tap` on GitHub (`https://github.com/lalitaalaalitah/homebrew-tap`).
2. Copy `Casks/medha-keyboard.rb` into `Casks/medha-keyboard.rb` inside the `homebrew-tap` repository.
3. Users can then install the medhA keyboard with a single command:
   ```bash
   brew install lalitaalaalitah/tap/medha-keyboard
   ```

---

## 3. Option B: Submitting to Official `homebrew/cask`

To be included in official Homebrew core casks (`brew install medha-keyboard`):
1. Must have a minimum number of stars/watchers or established user base.
2. Must follow Homebrew Cask audit guidelines (`brew audit --cask medha-keyboard`).
3. Must pass automated CI checks on Homebrew's repository.

---

## 4. Maintenance Workflow

Whenever a new version of `medhA-keyboard_layout` is tagged and released on GitHub:
1. GitHub Actions automatically generates `medhA-keyboard-macOS.zip`.
2. Compute sha256 checksum:
   ```bash
   shasum -a 256 dist/medhA-keyboard-macOS.zip
   ```
3. Update `version` and `sha256` in `Casks/medha-keyboard.rb` in `homebrew-tap`.
