#!/bin/sh

# Check if oh-my-zsh is already installed
if [ -d "$HOME/.oh-my-zsh" ]; then
	echo "~/.oh-my-zsh directory exists. Exiting script."
	exit 0
fi

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
