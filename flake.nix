{
  description = "medhA Sanskrit Keyboard Layout Flake for NixOS and macOS";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        packages.default = pkgs.callPackage ./default.nix { };
        packages.medhA-keyboard = self.packages.${system}.default;

        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3
            zip
            gzip
          ];
        };
      }
    ) // {
      # NixOS Module helper overlay / layout definition
      nixosModules.default = { config, lib, pkgs, ... }: {
        services.xserver.xkb.extraLayouts.medhA = {
          description = "medhA Sanskrit Keyboard Layout";
          languages = [ "sa" ];
          symbolsFile = ./Linux/sa;
        };
      };
    };
}
