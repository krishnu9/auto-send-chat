import os, time
from datetime import datetime, timedelta
import pyautogui as pg
from apscheduler.schedulers.background import BackgroundScheduler

now = datetime.now()
runat = datetime(2020,8,10,8,4,20,00,now.tzinfo)
delta = (runat - now).total_seconds()
# delta = 1

def sendMessage(message, x, y):
    pg.moveTo(x,y, duration=0.25)
    pg.click()
    pg.write(message, interval=0.01)
    pg.press('enter')
    print('Sent message!')

x_pos = 1416
y_pos = 759

message = "Krishnu Binod Pradhan, 716EC5073 joined the class today at 8:04 AM, 10 August."

scheduler = BackgroundScheduler()
dd = datetime.now() + timedelta(seconds=delta)
scheduler.add_job(sendMessage, 'date',run_date=dd, args=[message, x_pos, y_pos])


# sendMessage(message, x_pos, y_pos)

scheduler.start()
print('waiting...')
try:
    # keeps the main thread alive.
    while True:
        time.sleep(0.2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()