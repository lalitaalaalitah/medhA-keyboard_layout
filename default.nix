{
  pkgs ? import <nixpkgs> { },
}:

pkgs.stdenv.mkDerivation {
  pname = "medha-keyboard-layout";
  version = "1.7.5";

  src = ./.;

  installPhase = ''
    runHook preInstall

    # Install XKB layout for Linux
    mkdir -p $out/share/X11/xkb/symbols
    if [ -f Linux/sa ]; then
      cp Linux/sa $out/share/X11/xkb/symbols/sa
    fi

    # Install macOS bundle if on darwin / for darwin consumers
    mkdir -p $out/Library/Keyboard\ Layouts
    if [ -d MacOS/medhA.bundle ]; then
      cp -r MacOS/medhA.bundle $out/Library/Keyboard\ Layouts/medhA.bundle
    elif [ -d MacOS/medhA_1.7_working.bundle ]; then
      cp -r MacOS/medhA_1.7_working.bundle $out/Library/Keyboard\ Layouts/medhA.bundle
    fi

    runHook postInstall
  '';

  meta = with pkgs.lib; {
    description = "medhA Sanskrit keyboard layout for Linux, macOS, and Windows";
    homepage = "https://www.lalitaalaalitah.com";
    license = licenses.mit;
    platforms = platforms.unix;
    maintainers = [ "lalitaalaalitah" ];
  };
}
