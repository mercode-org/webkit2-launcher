{ stdenv
, gobject-introspection
, gnome3
, python3
, wrapGAppsHook
}:

stdenv.mkDerivation {
  pname = "webkit2-launcher";
  version = "0.0.1";

  src = ./.;

  buildInputs = [
    gnome3.gtk3
    gnome3.glib
    gnome3.webkitgtk
    gobject-introspection
    (python3.withPackages( ps: with ps;[ pygobject3 ] ))
    wrapGAppsHook
  ];

  installPhase = ''
    mkdir -p $out/{lib,bin}
    cp -r launcher/ $out/lib/webkit2-launcher
    cp -r example/ $out/lib/example
    ln -s $out/lib/webkit2-launcher/__init__.py $out/bin/webkit2-launcher
  '';
}
