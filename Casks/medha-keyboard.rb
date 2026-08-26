cask "medha-keyboard" do
  version "1.7.5"
  sha256 "625f53889478135166662b892063d38e18a55434f7022bf707542bc674a946c3"

  url "https://github.com/lalitaalaalitah/medhA-keyboard_layout/releases/download/v#{version}/medhA-keyboard-macOS-v#{version}.dmg"
  name "medhA Keyboard Layout"
  desc "Sanskrit keyboard layout for macOS"
  homepage "https://www.lalitaalaalitah.com"

  artifact "medhA.bundle", target: "/Library/Keyboard Layouts/medhA.bundle"

  zap trash: "~/Library/Preferences/com.apple.HIToolbox.plist"
end

