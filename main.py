from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
curdate = today.strftime('%Y年%m月%d日')
city = os.environ['CITY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
user1_id = os.environ["USER1_ID"]
template_id = os.environ["TEMPLATE_ID"]


def get_weather():
#   url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
#   res = requests.get(url).json()
#   weather = res['data']['list'][0]
#   return weather['weather'], math.floor(weather['temp']), math.floor(weather['low']), math.floor(weather['high']), weather['wind'], weather['province']
    url = "https://www.yiketianqi.com/free/day?appid=36612533&appsecret=2TX26ggS&unescape=1&cityid=" + city
    res = requests.get(url).json()
    weather = res
    return weather['wea'], weather['tem'], weather['tem_day'], weather['tem_night'], weather['win'], weather['city'], weather['city']

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)

wea, temperature, high, low, wind, province, cityname = get_weather()
data = {"curdate":{"value":curdate},"weather":{"value":wea},"temperature":{"value":temperature},"province":{"value":province},"city":{"value":cityname},"low":{"value":low},"low":{"value":low},"high":{"value":high},"wind":{"value":wind},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
res1 = wm.send_template(user1_id, template_id, data)

print(res)
print(res1)
