# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:26:46 2020

@author: santhosh
"""

import logging
logging.basicConfig(filename='app.log', filemode='a',level=logging.DEBUG)


from flask import Flask,redirect,url_for,request,render_template
from  mongoConnection import mongoConnect


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect/mongo/',methods=['POST','GET'])
def connectToMongo():
    logging.info('For this you must change the level and add a handler.')
    if request.method=='POST':
        host=request.form['host']
        port=request.form['port']
    elif request.method=='GET':
        host=request.args.get('host')
        port=request.args.get('port')
    con=mongoConnect(host,int(port))
    print(con)
    return render_template('index.html')
    
if __name__=='__main__':
    app.run(port=5000,debug=True,use_reloader=False)