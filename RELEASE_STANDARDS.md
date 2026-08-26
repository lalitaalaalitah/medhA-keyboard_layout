# medhA Keyboard Layout Release & Homebrew Tap Standards
=========================================================
Author       : lalitaalaalitah
Website      : https://www.lalitaalaalitah.com
GitHub       : https://github.com/lalitaalaalitah
Version      : 1.0.0
Description  : Specification for versioning, release packaging, tag naming, and Homebrew Cask sync.

---

## 1. Naming Conventions

### 1.1 Git Tags
- Git tags MUST strictly follow the semantic versioning format with a `v` prefix:
  `vX.Y.Z` (e.g. `v1.7.5`, `v1.8.0`)
- Pre-releases or release candidates MUST use `-rc.N` or `-beta.N` suffix:
  `vX.Y.Z-rc.1`

### 1.2 Asset Filenames
Release artifacts uploaded to GitHub Releases MUST use dynamic, versioned filenames:
- **macOS DMG**: `medhA-keyboard-macOS-v{VERSION}.dmg` (e.g. `medhA-keyboard-macOS-v1.7.5.dmg`)
- **macOS Legacy Alias DMG**: `medhA-keyboard-macOS.dmg`
- **Linux Archive**: `medhA-keyboard-Linux-v{VERSION}.tar.gz`
- **Windows Archive**: `medhA-keyboard-Windows-v{VERSION}.zip`
- **All Platforms Bundle**: `medhA-keyboard-All-Platforms-v{VERSION}.zip`

---

## 2. Homebrew Tap Integration Rules

### 2.1 Cask File Location
- Source Repository: `medhA-keyboard_layout/Casks/medha-keyboard.rb`
- Distribution Tap Repository: `homebrew-tap/Casks/medha-keyboard.rb` (in `lalitaalaalitah/homebrew-tap`)

### 2.2 Cask URL Pattern
The Homebrew Cask `url` MUST dynamically reference `version` variable:
```ruby
cask "medha-keyboard" do
  version "1.7.5"
  sha256 "EXACT_SHA256_HASH"

  url "https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases/download/v#{version}/medhA-keyboard-macOS-v#{version}.dmg"
  name "medhA Keyboard Layout"
  desc "Sanskrit keyboard layout for macOS"
  homepage "https://www.lalitaalaalitah.com"

  artifact "medhA.bundle", target: "/Library/Keyboard Layouts/medhA.bundle"

  zap trash: "~/Library/Preferences/com.apple.HIToolbox.plist"
end
```

> [!IMPORTANT]
> Never hardcode version strings like `v1.7.dmg` inside the `url` property in `medha-keyboard.rb`.

### 2.3 Checksum Requirements
- Official release casks MUST provide an explicit `sha256` hash (SHA-256 of `medhA-keyboard-macOS-v{VERSION}.dmg`).
- `:no_check` is reserved only for temporary local developer testing.

---

## 3. Standard Release Procedure Workflow

1. **Update Code / Bundles**:
   Ensure all keyboard bundle updates are placed in `MacOS/`, `Linux/`, and `Windows/`.

2. **Package Release Artifacts Locally**:
   ```bash
   python3 scripts/package_keyboards.py --app-version 1.7.5 --platform all
   ```

3. **Compute SHA256 Checksum**:
   ```bash
   shasum -a 256 dist/medhA-keyboard-macOS-v1.7.5.dmg
   ```

4. **Update Casks**:
   Update `version` and `sha256` in both:
   - `medhA-keyboard_layout/Casks/medha-keyboard.rb`
   - `homebrew-tap/Casks/medha-keyboard.rb`

5. **Commit & Push Repository Changes**:
   ```bash
   git add .
   git commit -m "Release v1.7.5: Update packaging script, casks, and documentation"
   git push origin master
   ```

6. **Create Tag & Trigger GitHub Action**:
   ```bash
   git tag -f v1.7.5
   git push origin v1.7.5 --force
   ```

7. **Push to Homebrew Tap**:
   ```bash
   cd /Volumes/Cablet_WD_2TB_20251206/05_Development/Github/14_DevelopmentEnvs/03_PackageManagers/00_Homebrew/homebrew-tap
   git add .
   git commit -m "medha-keyboard 1.7.5"
   git push origin main
   ```
