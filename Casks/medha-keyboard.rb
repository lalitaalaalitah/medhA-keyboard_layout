cask "medha-keyboard" do
  version "1.7"
  sha256 :no_check

  url "https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases/download/v#{version}.4/medhA-keyboard-macOS-v#{version}.dmg"
  name "medhA Keyboard Layout"
  desc "Sanskrit keyboard layout for macOS"
  homepage "https://www.lalitaalaalitah.com"

  artifact "medhA.bundle", target: "/Library/Keyboard Layouts/medhA.bundle"

  zap trash: "~/Library/Preferences/com.apple.HIToolbox.plist"
end
