# webkit2-launcher

Webkit2 Launcher is, as the name says, a very simple launcher for webapps

<!-- dev docs https://lazka.github.io/pgi-docs/ -->

# Usage

In your package.json add the object launcher. It can have the following properties:

- `main`, **required**, path: Relative path to your app's main HTML document
- `title`, string: App title to use
- `width`, integer: Initial window width in pixel **requires `height`**
- `minWidth`, integer: Minimal window width in pixel
- `height`, integer: Initial window height in pixel **requires `width`**
- `minHeight`, integer: Minimal window height in pixel
- `iconPath`, path: Taskbar icon path to use
- `icon`, string: Taskbar icon name to use

# Development

If you're not on nixOS/merOS, install nix first

```sh
curl -L https://nixos.org/nix/install | sh
```

Afterwards launch the nix-shell for development

```sh
nix-shell
```

Now you can start webkit2-launcher by running

```sh
webkit2-launcher
```
