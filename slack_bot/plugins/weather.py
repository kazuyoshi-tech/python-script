from slackbot.bot import respond_to

import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

def get_weather():
    city = 'Tokyo'
    WHEATHER_KEY = os.environ['WHEATHER_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={WHEATHER_KEY}"

    response = requests.get(url)
    return response.json()


# テスト用実行関数
if __name__ == "__main__":
    get_weather()

#@respond_to('^(今日|明日|明後日)の天気$')
@respond_to('天気')
#def whether_1(message, group):
def whether_1(message):
    data = get_weather()
    text = f"都市：{data['name']}\n 天候：{data['weather'][0]['main']}\n 温度：{str(data['main']['temp'])}度\n"
    message.reply(text)