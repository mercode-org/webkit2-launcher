{ stdenv
, fetchurl
, python3
, gtk3
, glib
, gobject-introspection
, wrapGAppsHook
, callPackage
, glib-networking
, gnome3
}:

python3.pkgs.buildPythonApplication rec {
  name = "webkit2-launcher-${version}";
  version = "0.0.1";

  src = ./.;

  buildInputs = [
    gnome3.gtk3
    gnome3.glib
    gnome3.webkitgtk
    glib-networking
    gobject-introspection

    wrapGAppsHook
  ];

  propagatedBuildInputs = with python3.pkgs; [
    pygobject3
  ];

  doCheck = false;

  meta = with stdenv.lib; {
    description = "A very simple launcher for webapps";
    homepage = https://os.mercode.org;
    license = licenses.gpl2;
    maintainers = with maintainers; [ mkg20001 ];
  };
}
