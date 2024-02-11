# Dotfiles
Here are my personal dotfiles, which I use for my system configuration. 
They are currently set up on Fedora, but the differences between distributions should be minimal.

## To install

### Install Hyprland and dependencies
 - [Hyprland via fedora copr](https://copr.fedorainfracloud.org/coprs/solopasha/hyprland)
 - ``waybar``

### Playerctl
Used to controll media playback, such as play or pause
 - ``playerctl``

### Dunst
Notification deamon
 - ``dunst``

### Grim and Slurp
Used to take screenshots with an area selector
 - ``slurp``
 - ``grim``

### Wl-clipboard
 Wayland clipbaord util
  - ``wl-clipboard``

### Wdisplays
Helper for settings with displays etc. on wayland
 - ``wdisplays``

### Swaylock
Used to lock the screen
 - ``swaylock``

### xdg-desktop-portal-hyprland
Used for screen sharing
 - ``xdg-desktop-portal-hyprland``

### Alacritty
Used as terminal emulator
 - ``Alacritty``

### Zsh
Used instead of bash
 - ``zsh``
 - ``sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"``

### Fonts
 - ``nerd-fonts-sf-mono`` (AUR)
 - ``apple-fonts`` (AUR)

### Powerlevel10k
 - ``git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k``
 - Override `ZSH_THEME` in `.zshrc` 
   - ``ZSH_THEME="powerlevel10k/powerlevel10k"``
