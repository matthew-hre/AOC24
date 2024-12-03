let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    packages = [
      pkgs.black
      (pkgs.python3.withPackages (python-pkgs: [
        python-pkgs.requests
      ]))
    ];
  }
