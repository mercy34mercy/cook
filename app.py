# -*- coding: utf-8 -*-
from flask import Flask
from test import get_tweet

app = Flask(__name__)

@app.route('/')
def index():
    a = get_tweet()
    return a


@app.route('/tweet')
def b():
    return "helloo"
  


