import pyautogui as pg
import time


def get_mouse_pos():
    print("Place the cursor on the text-area after 5 seconds...")
    time.sleep(5)
    x, y = pg.position()
    return x, y


if __name__ == "__main__":
    x, y = get_mouse_pos()
    print(x, y)
