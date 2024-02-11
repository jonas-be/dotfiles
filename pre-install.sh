#!/bin/bash
# This script checks out the repo and install the basic tools needed to install the dotfiles
# You can run this script with the following command:
# curl -sSL https://raw.githubusercontent.com/jonas-be/dotfiles/main/pre-install.sh | bash

sudo pacman -S --needed --noconfirm git base-devel python python-yaml

# Install yay
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si --noconfirm
yay -Y --gendb
yay -Syu --devel
yay -Y --devel --save

cd ..
git clone https://github.com/jonas-be/dotfiles.git
cd dotfiles

echo 'Now run "python install.py" and select the groups you want to install'
