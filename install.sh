#!/bin/bash

sudo pacman -S --needed --noconfirm git base-devel python python-yaml

# Install yay
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si --noconfirm
yay -Y --gendb
yay -Syu --devel
yay -Y --devel --save

cd ~
git clone https://github.com/jonas-be/dotfiles.git
cd dotfiles

python install-pkgs.py
echo 'Now use "python dotcopy.py [get | put] <entry>" to get or put dotfile from or in this repo, localy'
