import sys
import time
import pyjokes
import schedule
from notifypy import Notify


def job():
    notification = Notify()
    notification.title = "Funny Joke"
    notification.message = pyjokes.get_joke()
    notification.send()


def run_forever():
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule.every(30).minutes.do(job)


if __name__ == '__main__':
    try:
        job()
        run_forever()
    except KeyboardInterrupt:
        print("GoodBye!")
        sys.exit(0)

