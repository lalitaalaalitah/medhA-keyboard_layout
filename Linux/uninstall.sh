#!/usr/bin/env bash
# ==============================================================================
# Script Name  : uninstall.sh
# Author       : lalitaalaalitah
# Website      : https://www.lalitaalaalitah.com
# GitHub       : https://github.com/lalitaalaalitah
# Description  : Uninstaller for medhA Sanskrit Keyboard Layout on Linux
# ==============================================================================

set -euo pipefail

VERSION="1.0.0"

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
    echo "            medhA Sanskrit Keyboard Layout Uninstaller           "
    echo "                 Version: ${VERSION}                             "
    echo "         Author: lalitaalaalitah | https://www.lalitaalaalitah.com"
    echo "================================================================="
    echo -e "${CLR_RESET}"
}

if [[ "${1:-}" == "--version" ]]; then
    echo "medhA Keyboard Linux Uninstaller v${VERSION} by lalitaalaalitah (https://www.lalitaalaalitah.com)"
    exit 0
fi

print_banner

if [[ $EUID -ne 0 ]]; then
   echo -e "${FG_RED}Error: This script must be run with superuser privileges (sudo ./uninstall.sh)${CLR_RESET}" 1>&2
   exit 1
fi

XKB_SYMBOLS_SA="/usr/share/X11/xkb/symbols/sa"

if [[ -f "$XKB_SYMBOLS_SA" ]]; then
    echo -e "${FG_TEXT}Removing ${XKB_SYMBOLS_SA}...${CLR_RESET}"
    rm -f "$XKB_SYMBOLS_SA"
    echo -e "${FG_GREEN}   [OK] Removed symbol file.${CLR_RESET}"
fi

echo -e "${FG_YELLOW}Note: If evdev.xml backup exists (.medha_bak), you can restore it if desired.${CLR_RESET}"
echo -e "${FG_GREEN}medhA keyboard uninstalled successfully.${CLR_RESET}"
