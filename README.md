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
 - Waybar ``sudo dnf install waybar``

### Playerctl
Used to controll media playback, such as play or pause
 - ``sudo dnf install playerctl``

### Dunst
Notification deamon
 - ``sudo dnf install dunst``

### Grim and Slurp
Used to take screenshots with an area selector
 - ``sudo dnf install slurp``
 - ``sudo dnf install grim``

### Swaylock
Used to lock the screen
 - ``sudo dnf install swaylock``
