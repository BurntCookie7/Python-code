from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

keyboard.press(Key.alt)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.release(Key.alt)