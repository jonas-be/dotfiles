# Dotfiles
Here are my personal dotfiles, which I use for my system configuration. 
They are currently set up on Fedora, but the differences between distributions should be minimal.

## To install

### Starship
Cross-shell prompt, highly configurable
 - ``curl -sS https://starship.rs/install.sh | sh``
 - Paste to `.bashrc` 
    - ``eval "$(starship init bash)"``

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

