cask "medha-keyboard" do
  version "1.7"
  sha256 :no_check # Updated with release artifact sha256 checksum

  url "https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases/download/v#{version}/medhA-keyboard-macOS.zip"
  name "medhA Keyboard Layout"
  desc "Sanskrit keyboard layout for macOS"
  homepage "https://www.lalitaalaalitah.com"

  artifact "macOS/medhA-macOSX-v_1.7.bundle", target: "/Library/Keyboard Layouts/medhA-macOSX-v_1.7.bundle"

  zap trash: "~/Library/Preferences/com.apple.HIToolbox.plist"
end
