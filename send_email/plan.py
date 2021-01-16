import schedule
from send_email import mail
from greetings import sentence
from send_email.config import config


# 建议发送
def send():
    content = sentence.zaoan()
    mail.send_email(content)


# 定时某一时刻发送
def send_email():
    send_time = config.send_time

    print("schedule")
    schedule.every().day.at(send_time["test"]).do(send)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    # content = sentence.zaoan()
    # print(content)
    config = config.config
    print(config)
    # send_email()
    print("Bye~ System Closed!")