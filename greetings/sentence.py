import pandas as pd
from datetime import datetime
import random
import requests
import json
import os
from send_email.config import config


random.seed(datetime.now())
print(datetime.now())

BASEDIR = os.path.join(os.path.dirname(__file__), os.pardir)
# 这里的路径原来存在问题,现在改好了


def get_sentence():
    raw_data = pd.read_csv(BASEDIR + '/example_greetings/words.csv', sep=',', header=None)
    length = raw_data.shape[0]
    # print(raw_data)
    idx = random.randint(0, length-1)
    random_sentence = raw_data.iloc[idx, 1]
    return random_sentence


def chp():
    url = r'https://chp.shadiao.app/api.php'
    respon = requests.get(url)
    content = respon.text
    return content


def zaoan():
    print(BASEDIR)
    # with open(BASEDIR + '/example_greetings/example.json', 'r', encoding='utf-8') as f:
    #     respon = json.load(f)

    APIKEY = config.APIKEY
    url = 'http://api.tianapi.com/txapi/zaoan/index?key={}'.format(APIKEY)
    res = requests.get(url)
    respon = json.loads(res.text)

    status = respon.get("code")
    if status:
        # body中包含有一个list, 其第一个元素才是内容
        content = respon.get("newslist")[0].get("content")
        with open(BASEDIR + '/example_greetings/zaoan.txt', 'a+', encoding='utf-8') as fout:
            fout.write(content + '\n')
        print("--> Cache content to " + BASEDIR + '/example_greetings/zaoan.txt')
    else:
        content = "System Error! But say Good Morning"

    return content


def wanan():
    pass


if __name__ == "__main__":
    pass
    # sentence = zaoan()
    # print(sentence)

