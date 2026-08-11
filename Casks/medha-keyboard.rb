cask "medha-keyboard" do
  version "1.7"
  sha256 :no_check

  url "https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases/download/v#{version}/medhA-keyboard-macOS.dmg"
  name "medhA Keyboard Layout"
  desc "Sanskrit keyboard layout for macOS"
  homepage "https://www.lalitaalaalitah.com"

  artifact "medhA-macOSX-v_1.7.bundle", target: "/Library/Keyboard Layouts/medhA-macOSX-v_1.7.bundle"

  zap trash: "~/Library/Preferences/com.apple.HIToolbox.plist"
end
