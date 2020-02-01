# webkit2-launcher

Webkit2 Launcher is, as the name says, a very simple launcher for webapps

# Usage

It takes a tiny JSON file


width Integer (optional) - Window's width in pixels. Default is 800.
height Integer (optional) - Window's height in pixels. Default is 600.
x Integer (optional) - (required if y is used) Window's left offset from screen. Default is to center the window.
y Integer (optional) - (required if x is used) Window's top offset from screen. Default is to center the window.
useContentSize Boolean (optional) - The width and height would be used as web page's size, which means the actual window's size will include window frame's size and be slightly larger. Default is false.
center Boolean (optional) - Show window in the center of the screen.
minWidth Integer (optional) - Window's minimum width. Default is 0.
minHeight Integer (optional) - Window's minimum height. Default is 0.
maxWidth Integer (optional) - Window's maximum width. Default is no limit.
maxHeight Integer (optional) - Window's maximum height. Default is no limit.
resizable Boolean (optional) - Whether window is resizable. Default is true.
movable Boolean (optional) - Whether window is movable. This is not implemented on Linux. Default is true.
minimizable Boolean (optional) - Whether window is minimizable. This is not implemented on Linux. Default is true.
maximizable Boolean (optional) - Whether window is maximizable. This is not implemented on Linux. Default is true.
closable Boolean (optional) - Whether window is closable. This is not implemented on Linux. Default is true.
focusable Boolean (optional) - Whether the window can be focused. Default is true. On Windows setting focusable: false also implies setting skipTaskbar: true. On Linux setting focusable: false makes the window stop interacting with wm, so the window will always stay on top in all workspaces.
alwaysOnTop Boolean (optional) - Whether the window should always stay on top of other windows. Default is false.
fullscreen Boolean (optional) - Whether the window should show in fullscreen. When explicitly set to false the fullscreen button will be hidden or disabled on macOS. Default is false.
fullscreenable Boolean (optional) - Whether the window can be put into fullscreen mode. On macOS, also whether the maximize/zoom button should toggle full screen mode or maximize window. Default is true.
title String (optional) - Default window title. Default is "Electron". If the HTML tag <title> is defined in the HTML file loaded by loadURL(), this property will be ignored.
icon (NativeImage | String) (optional) - The window icon. On Windows it is recommended to use ICO icons to get best visual effects, you can also leave it undefined so the executable's icon will be used.

