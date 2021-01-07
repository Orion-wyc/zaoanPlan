import schedule
from send_email import mail
from greetings import sentence
from .configuration import configs

# 建议发送
def send():
    content = sentence.zaoan()
    mail.send_email(content)


# 定时某一时刻发送
def send_email(send_time):
    print("schedule")
    schedule.every().day.at(configs[send_time]).do(send)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    content = sentence.zaoan()
    print(content)
    send_email()
    print("Bye~ System Closed!")