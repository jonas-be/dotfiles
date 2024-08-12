#!/bin/bash

# Define the entries
entries="Logout\nSleep\nRestart\nPower Off"

# Display the menu and capture the selection
selection=$(echo -e $entries | wofi --dmenu --prompt="Power Menu")

# Execute a command based on the selection
case $selection in
    "Logout")
        # Command for Logout
        hyprctl dispatch exit
        ;;
    "Sleep")
        # Command for Sleep
        systemctl suspend
        ;;
    "Restart")
        # Command for Restart
        systemctl reboot
        ;;
    "Power Off")
        # Command for Power Off
        systemctl poweroff
        ;;
    *)
        # Default case if no valid option is selected
        notify-send "Invalid selection"
        ;;
esac

