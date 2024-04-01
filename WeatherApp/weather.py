# 调用方法
from datetime import datetime
import os
# import pytz
import requests
import math

API_KEY = 'cac422a5f22d9582971ee52de1e16ece'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None

    city_temp_dict = data["main"]
    city_sys_dict = data["sys"]

    temp_min = city_temp_dict["temp_min"]
    temp_max = city_temp_dict["temp_max"]
    temp_cur = city_temp_dict["temp"]
    temp_feel = city_temp_dict["feels_like"]
    date_day = datetime.now().day
    date_month = datetime.now().month
    date_year = datetime.now().year

    data_date = str(date_year) + "年" + str(date_month).zfill(2) + "月" + str(date_day).zfill(2) + "日"
    data_dict = {
        "city_name": city,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "date": data_date,
        "temp_cur": temp_cur,
        "temp_feel": temp_feel
    }
    data_dict = {
        1: [city, temp_min, temp_max, data_date, temp_cur, temp_feel]
    }
    t1 = data_dict.get("city_name")
    return data_dict
    # print(data)



# if __name__ == '__main__':
#     input_str = 'BeiJing'
#     query_api(input_str)