from send_email.plan import send_email
from threading import Thread
from .configuration import send_time


def main():
    t = Thread(target=send_email,args=(send_time, ))
    t.start()
    print("-->Running <zaoan> Plan")