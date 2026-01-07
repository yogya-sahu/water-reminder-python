import time 
from plyer import notification

while True:
    print("please drink some water")
    notification.notify(title="please drink some water",
                        message="its time please drink some water")
    time.sleep(60*60)
