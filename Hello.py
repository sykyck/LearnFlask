# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 02:37:33 2024

@author: Vaibhav Sharma
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()