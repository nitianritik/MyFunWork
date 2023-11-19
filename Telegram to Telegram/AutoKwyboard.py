import time
import keyboard
import os

def open_telegram():
    path_to_telegram = r"C:\Users\ritik\AppData\Roaming\Telegram Desktop\Telegram.exe"
    
    try:
        os.startfile(path_to_telegram)
        print("Telegram is now opening...")
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(1)

def press_alt_tab():
    keyboard.press_and_release("alt+tab")
    time.sleep(1)  # Adjust the delay if needed

def press_ctrl_v():
    keyboard.press_and_release("ctrl+v")
    time.sleep(1)  # Adjust the delay if needed

def main():
    try:
      while 1:
        # print("Switching to the desired window...")
        # press_alt_tab()

        open_telegram()


        print("Pasting content...")
        press_ctrl_v()

        keyboard.press_and_release("enter")
        time.sleep(.5)


        print("Switching back to the original window...")
        press_alt_tab()

        time.sleep(600)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
