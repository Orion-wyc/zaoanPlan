from send_email.plan import send_email
from threading import Thread


def main():
    t = Thread(target=send_email, args=())
    t.start()
    print("-->Running <zaoan> Plan")