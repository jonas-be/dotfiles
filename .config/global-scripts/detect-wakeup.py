# Shoutout ChatGPT
import os
import sys
import termios
import tty
import time
import select

# Function to get the current cursor coordinates using `hyprctl`
def get_cursor_coords():
    return os.popen("hyprctl cursorpos").read().strip()

# Function to check for any key press
def is_key_pressed():
    if select.select([sys.stdin], [], [], 0)[0]:
        sys.stdin.read(1)  # Read the key press (not storing it since any key will exit)
        return True
    return False

def main():
    # Set terminal to cbreak mode to catch keypresses
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)

    try:
        last_coords = get_cursor_coords()
        print("Monitoring for mouse movement or any key press...")

        while True:
            # Check current cursor position
            current_coords = get_cursor_coords()

            # Exit if mouse moved or any key was pressed
            if current_coords != last_coords or is_key_pressed():
                break

            # Update the last known cursor position
            last_coords = current_coords

            # Sleep for a short time to reduce CPU usage
            time.sleep(0.1)

    finally:
        # Restore terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    print("Exiting script...")

if __name__ == "__main__":
    main()
