# -*- coding: utf-8 -*-
from flask import Flask
from flask import *
from orehayaru import get_tweet
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['POST','GET'])
def index():
    place = 0
    if request.method == 'POST':
        place = request.json['place'] 
    elif request.method == 'GET':
        place = 0

    a,b = get_tweet(place)

    


    while(a == 1):
        a,b = get_tweet(0)
    



    #return render_template("main.html", name=a)

    jsonify = ({
        "data":[]
    })

    for i in range(len(a)):
        print(a[i])
        add_data={
            "url":a[i],
            "tweet":b[i]
        }
        jsonify["data"].append(add_data)

    print(jsonify)
    
    
    return jsonify


@app.route('/tweet',methods = ["POST","GET"] )
def b():
    return "helloo"
  


