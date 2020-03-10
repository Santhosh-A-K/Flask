# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:02:35 2020

@author: santhosh
"""

from pymongo import MongoClient




def mongoConnect(host,port,dbName):
    client=None
    db=None

    try:
        client = MongoClient(host,port)#'localhost', 27017
        print("Connected Successfully")
        dbList=client.list_database_names()
        if dbName in dbList:
            db=client[dbName]
        else:
            print("No database is available")
    except:
        print("Error in connecting to Database")
    finally:
        return db
    
