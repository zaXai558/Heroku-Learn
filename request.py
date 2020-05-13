# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:07:55 2020

@author: Asus
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'TV':2, 'radio':9, 'newspaper':6})

print(r.json())