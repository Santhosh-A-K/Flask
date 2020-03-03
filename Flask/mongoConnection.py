# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:02:35 2020

@author: santhosh
"""

from pymongo import MongoClient




def mongoConnect(host,port):
    client=None
    try:
        client = MongoClient(host,port)#'localhost', 27017
        print("Connected Successfully")
    except:
        print("Error in connecting to Database")
    finally:
        return client
    
