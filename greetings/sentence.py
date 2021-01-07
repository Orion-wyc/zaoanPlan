import pandas as pd
from datetime import datetime
import random
import requests
import json
import os


random.seed(datetime.now())
print(datetime.now())
APIKEY = "f7a5bb131995362ea64588cf27bb36b7"
BASEDIR = os.path.abspath('..')


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
    # with open(BASEDIR + '/example_greetings/example.json', 'r', encoding='utf-8') as f:
    #     respon = json.load(f)

    url = 'http://api.tianapi.com/txapi/zaoan/index?key={}'.format(APIKEY)
    res = requests.get(url)
    respon = json.loads(res.text)

    status = respon.get("code")
    if status:
        # body中包含有一个list, 其第一个元素才是内容
        content = respon.get("newslist")[0].get("content")
    else:
        content = "System Error! But say Good Morning"

    return content


def wanan():
    pass


if __name__ == "__main__":
    sentence = zaoan()
    print(sentence)

