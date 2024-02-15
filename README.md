# Dotfiles

## Pre-requisites

- Arch Linux
- This repository checked out
- yay installed
- python installed
- python-yaml installed

You can do this all at once by running the following command:

```bash
curl -sSL https://raw.githubusercontent.com/jonas-be/dotfiles/main/pre-install.sh | bash
```

## Install

After satisfying the pre-requisites, you can install the dotfiles by running the following command:

```bash
python install.py
```

Then select what you want to install, by following the instructions of the program.

## Things to install/configure manually

```bash
# Oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## What it does?

### install.py

This script asks you which groups of packages you want to install.
After you agreed with your selection, it will install the packages (with pacman and yay) and copy the dotfiles using `dotcopy.py`.

In the `pkgs.yaml` you can specify which packages and dotfiles should be installed.

Each group can have:

- `pkgs` arch packages
- `aurs` aur packages
- `dotfiles` dotfiles entries from the `config.ini` file

Example:
```yaml
nvim:
  pkgs:
    - clang
    - neovim
  dotfiles:
    - nvim

hypr:
  aurs:
    - hyprland
    - xdg-desktop-portal-hyprland
```

### dotcopy.py

This script can copy dotfiles from the repo to their correct places on the host system by using the `put` option.
It can also copy dotfiles from the host system to the repo by using the `get` option.

In the `config.ini` file, you can specify which files should be copied to which location.

```ini
# Example for a file
[zshrc]
source = .zshrc
destination = ~/.zshrc
file = true

# Example for a directory
[nvim]
source = .config/nvim
destination = ~/.config/nvim/
```

The usage is as follows:

```bash
# Copy dotfiles from the repo to the host system
python dotcopy.py put <entry>
# Copy dotfiles from the host system to the repo
python dotcopy.py get <entry>
```

## Special thanks

 - [Aylur](https://github.com/Aylur) for making ags and his dotfiles *(my ags config are currently almost copy paste)*
