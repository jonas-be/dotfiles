# Dotfiles

## Pre-requisites

- This repository checked out
- yay installed

## To install

1. Install packages using the ``install-pkgs.sh`` script.
2. Copy dotfiles using the ``dotcopy.sh`` script 
(use the params `get` or `put` followed by the entry onf the config.ini)

## Things to install manually

### Oh My Zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Powerlevel10k

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k```
