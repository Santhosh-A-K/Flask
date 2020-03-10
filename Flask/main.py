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
    return render_template('index.html',check=False)

@app.route('/connect/mongo/',methods=['POST','GET'])
def connectToMongo():
    logging.info('For this you must change the level and add a handler.')
    if request.method=='POST':
        host=request.form['host']
        port=request.form['port']
        dbName=request.form['dbName']
    elif request.method=='GET':
        host=request.args.get('host')
        port=request.args.get('port')
        dbName=request.args.get('dbName')
    con=mongoConnect(host,int(port),dbName)
    print(con)
    if con==None:
        return render_template('index.html',check=True)
    else:
        return render_template('columns.html')
    
    





if __name__=='__main__':
    app.run(port=5000,debug=True,use_reloader=False)