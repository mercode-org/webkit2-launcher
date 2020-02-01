{ stdenv
, gobject-introspection
, gnome3
, python3
}:

stdenv.mkDerivation {
  pname = "webkit2-launcher";
  version = "0.0.1";
  
  buildInputs = [
    gnome3.gtk3
    gnome3.glib
    gnome3.webkitgtk
    gobject-introspection
    (python3.withPackages( ps: with ps;[ pygobject3 ] ))
  ];
}
