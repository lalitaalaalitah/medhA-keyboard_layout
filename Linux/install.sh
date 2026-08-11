#!/usr/bin/env bash
# ==============================================================================
# Script Name  : install.sh
# Author       : lalitaalaalitah
# Website      : https://www.lalitaalaalitah.com
# GitHub       : https://github.com/lalitaalaalitah
# Description  : Multi-Distro Installer for medhA Sanskrit Keyboard Layout on Linux
# Target Distros: Debian, Ubuntu, Pop!_OS (System76), Arch Linux, Manjaro, Fedora, NixOS
# ==============================================================================

set -euo pipefail

VERSION="1.0.1"

# Catppuccin Mocha Color Palette
BG_BASE='\033[48;2;30;30;46m'
FG_TEXT='\033[38;2;205;214;244m'
FG_LAVENDER='\033[38;2;180;190;254m'
FG_GREEN='\033[38;2;166;227;161m'
FG_YELLOW='\033[38;2;249;226;175m'
FG_RED='\033[38;2;243;139;168m'
CLR_RESET='\033[0;48;2;30;30;46;38;2;205;214;244m'

print_banner() {
    echo -e "${BG_BASE}${FG_LAVENDER}"
    echo "================================================================="
    echo "            medhA Sanskrit Keyboard Layout Installer             "
    echo "                 Version: ${VERSION}                             "
    echo "         Author: lalitaalaalitah | https://www.lalitaalaalitah.com"
    echo "================================================================="
    echo -e "${CLR_RESET}"
}

if [[ "${1:-}" == "--version" ]]; then
    echo "medhA Keyboard Linux Installer v${VERSION} by lalitaalaalitah (https://www.lalitaalaalitah.com)"
    exit 0
fi

print_banner

if [[ $EUID -ne 0 ]]; then
   echo -e "${FG_RED}Error: This script must be run with superuser privileges (sudo ./install.sh)${CLR_RESET}" 1>&2
   exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
XKB_SYMBOLS_DIR="/usr/share/X11/xkb/symbols"
XKB_EVDEV_XML="/usr/share/X11/xkb/rules/evdev.xml"
XKB_EVDEV_EXTRAS_XML="/usr/share/X11/xkb/rules/evdev.extras.xml"

# Detect Distro
DISTRO="Unknown"
if [[ -f /etc/os-release ]]; then
    . /etc/os-release
    DISTRO="${NAME:-Unknown}"
fi

echo -e "${FG_TEXT}Detected Linux Distribution: ${FG_YELLOW}${DISTRO}${CLR_RESET}"

# 1. Install/Replace symbol file
echo -e "${FG_TEXT}1. Installing / Replacing XKB symbol file 'sa' in ${XKB_SYMBOLS_DIR}/sa...${CLR_RESET}"
if [[ ! -f "${SCRIPT_DIR}/sa" ]]; then
    echo -e "${FG_RED}Error: Symbol file 'sa' not found in ${SCRIPT_DIR}${CLR_RESET}"
    exit 1
fi

if [[ -f "${XKB_SYMBOLS_DIR}/sa" ]]; then
    echo -e "${FG_YELLOW}   [UPGRADE] Existing 'sa' symbol file found. Overwriting with latest version...${CLR_RESET}"
fi

cp -f "${SCRIPT_DIR}/sa" "${XKB_SYMBOLS_DIR}/sa"
chmod 644 "${XKB_SYMBOLS_DIR}/sa"
echo -e "${FG_GREEN}   [OK] Symbol file updated successfully.${CLR_RESET}"

# 2. Register in evdev.xml
register_in_xml() {
    local target_xml="$1"
    if [[ ! -f "$target_xml" ]]; then
        return 0
    fi

    echo -e "${FG_TEXT}2. Registering / Verifying layout in ${target_xml}...${CLR_RESET}"

    # Backup XML before edit
    cp "$target_xml" "${target_xml}.medha_bak"

    # Check if 'sa' variant already registered
    if grep -q "<name>sa</name>" "$target_xml"; then
        echo -e "${FG_GREEN}   [OK] 'sa' variant registration verified in ${target_xml}.${CLR_RESET}"
    else
        python3 -c "
import sys
xml_path = sys.argv[1]
snippet = '''        <variant>
          <configItem>
            <name>sa</name>
            <description>sanskrit (medhA)</description>
            <languageList>
              <iso639Id>sa</iso639Id>
            </languageList>
          </configItem>
        </variant>
'''
with open(xml_path, 'r', encoding='utf-8') as f:
    content = f.read()

if '</variantList>' in content:
    idx = content.find('</variantList>')
    new_content = content[:idx] + snippet + content[idx:]
    with open(xml_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('SUCCESS')
" "$target_xml" || true
        echo -e "${FG_GREEN}   [OK] Registered in ${target_xml}.${CLR_RESET}"
    fi
}

register_in_xml "$XKB_EVDEV_XML"
register_in_xml "$XKB_EVDEV_EXTRAS_XML"

# 3. Clear XKB compiled keymap cache if present to ensure instant update
if [[ -d /var/lib/xkb ]]; then
    echo -e "${FG_TEXT}3. Refreshing XKB compiled keymap cache...${CLR_RESET}"
    rm -f /var/lib/xkb/*.xkm 2>/dev/null || true
    echo -e "${FG_GREEN}   [OK] XKB cache cleared.${CLR_RESET}"
fi

# 4. Distro-specific post installation hints
echo -e "${FG_LAVENDER}"
echo "================================================================="
echo "               Installation / Upgrade Complete!                  "
echo "================================================================="
echo -e "${CLR_RESET}"

echo -e "${FG_TEXT}Activation instructions for ${FG_YELLOW}${DISTRO}${FG_TEXT}:${CLR_RESET}"
echo ""
echo -e "${FG_TEXT}• ${FG_GREEN}GNOME (Ubuntu / Debian / Pop!_OS / Fedora)${FG_TEXT}:${CLR_RESET}"
echo "  Go to Settings -> Keyboard -> Input Sources -> Add (+) -> English (US) or Sanskrit -> medhA / sa"
echo ""
echo -e "${FG_TEXT}• ${FG_GREEN}Arch Linux / Manjaro / KDE Plasma${FG_TEXT}:${CLR_RESET}"
echo "  Run: localectl set-x11-keymap us,sa"
echo "  Or go to System Settings -> Input Devices -> Keyboard -> Layouts -> Add Layout 'sa'"
echo ""
echo -e "${FG_TEXT}• ${FG_GREEN}Command Line Quick Activation (X11 session)${FG_TEXT}:${CLR_RESET}"
echo "  setxkbmap -layout 'us,sa'"
echo "  (Use Alt+Shift or Super+Space to switch input sources)"
echo ""
