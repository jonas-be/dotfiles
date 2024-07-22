#!/bin/bash

# Check if a window name was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <window_name>"
    exit 1
fi

# Get the window address of the specified window name
window_address=$(hyprctl clients -j | jq -r --arg name "$1" '.[] | select(.class == $name) | .address')

# If the window was found, focus it
if [ -n "$window_address" ]; then
    hyprctl dispatch focuswindow address:$window_address
else
    echo "Window with name '$1' not found."
fi

