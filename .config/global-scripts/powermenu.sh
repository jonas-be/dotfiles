#!/bin/bash

# Define the entries
entries="Logout\nSleep\nRestart\nPower Off"

# Display the menu and capture the selection
selection=$(echo -e $entries | wofi --dmenu --prompt="Power Menu")

# Execute a command based on the selection
case $selection in
    "Logout")
        # Command for Logout
        echo "hyprctl dispatch exit"
        ;;
    "Sleep")
        # Command for Sleep
        echo "systemctl suspend"
        ;;
    "Restart")
        # Command for Restart
        echo "systemctl reboot"
        ;;
    "Power Off")
        # Command for Power Off
        echo "systemctl poweroff"
        ;;
    *)
        # Default case if no valid option is selected
        notify-send "Invalid selection"
        ;;
esac

