# -*- coding: utf-8 -*-
from flask import Flask
from flask import *
from orehayaru import get_tweet

app = Flask(__name__)

@app.route('/')
def index():
    a = get_tweet(0)
    while(a == 1):
        a = get_tweet(0)
    return render_template("main.html", name=a)


@app.route('/tweet')
def b():
    return "helloo"
  


