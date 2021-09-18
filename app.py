# -*- coding: utf-8 -*-
from flask import Flask
from orehayaru import get_tweet

app = Flask(__name__)

@app.route('/')
def index():
    a = get_tweet(0)
    while(a == 1):
        a = get_tweet(0)

    return a


@app.route('/tweet')
def b():
    return "helloo"
  


