cask "medha-keyboard" do
  version "1.7.5"
  sha256 "6d101a9c78d0b77154bd3032632a9aa014057c9cae294eae79cef3468780e1ff"

  url "https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases/download/v#{version}/medhA-keyboard-macOS-v#{version}.dmg"
  name "medhA Keyboard Layout"
  desc "Sanskrit keyboard layout for macOS"
  homepage "https://www.lalitaalaalitah.com"

  artifact "medhA.bundle", target: "/Library/Keyboard Layouts/medhA.bundle"

  zap trash: "~/Library/Preferences/com.apple.HIToolbox.plist"
end


