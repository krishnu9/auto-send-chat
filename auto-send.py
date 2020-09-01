import os
import time
from datetime import datetime, timedelta
import pyautogui as pg
from apscheduler.schedulers.background import BackgroundScheduler
from mouse_pos import get_mouse_pos

pg.FAILSAFE = False

now = datetime.now()
runat = datetime(2020, 8, 31, 8, 0, 10, 00, now.tzinfo)
delta = (runat - now).total_seconds()
# delta = 2
print("Remaining Time: ", delta//3600, "Hr ", (delta %
                                               3600)//60, "Min ", (delta % 3600) % 60, "Sec")


def sendMessage(message, x, y):
    pg.moveTo(x, y, duration=0.25)
    pg.click()
    pg.write(message, interval=0.01)
    pg.press('enter')
    print('Sent message!')


# Maximized coordinates
x_pos = 1200
y_pos = 977
# pg.moveTo(x_pos, y_pos, duration=0.25)

# x_pos, y_pos = get_mouse_pos()
print("Mouse at: ", x_pos, y_pos)

message = "Krishnu Binod Pradhan, 716EC5073 joined the class today at 8:00 AM, 31 August."

scheduler = BackgroundScheduler()
dd = datetime.now() + timedelta(seconds=delta)
scheduler.add_job(sendMessage, 'date', run_date=dd,
                  args=[message, x_pos, y_pos])

# Old function call (not required anymore)
# sendMessage(message, x_pos, y_pos)

scheduler.start()
print('waiting...')
try:
    # keeps the main thread alive.
    while True:
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
