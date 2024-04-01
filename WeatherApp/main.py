# -*- coding: utf-8 -*-

# 调用方法
import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)


@app.route('/weather')
def index():
    # query_api("Toronto")
    # return render_template(
    #     'weather.html',
    #     data=[{'name': 'Toronto'}, {'name': 'Montreal'}, {'name': 'Calgary'},
    #           {'name': 'Ottawa'}, {'name': 'Edmonton'}, {'name': 'Mississauga'},
    #           {'name': 'Winnipeg'}, {'name': 'Vancouver'}, {'name': 'Brampton'},
    #           {'name': 'Quebec'}])
    return render_template('weather.html')
    # return query_api("Toronto")


@app.route("/getDataByCity", methods=['POST', 'GET'])
def getDataByCity():
    city = request.form.get("city")
    data = query_api(city)

    # city_temp = data["main"]
    # city_sys = data["sys"]
    #
    # temp_min = city_temp["temp_min"]

    # env = Environment(loader=FileSystemLoader('templates'))
    # template = env.get_template('temp1.html')
    # html = template.render(data_dict=data, error="error")
    # return data
    return render_template('result.html', data_dict=data)


if __name__ == '__main__':
    app.run(debug=True)
    # getDataByCity()