# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:00:24 2019

@author: gylk
"""

import requests
import json

url = "https://data.cdrc.ac.uk/dataset/7c80cf31-5bf5-4714-9647-d3ca47779fa3/resource/0c43c412-23cc-4a04-afc0-b01ac367e127/download/c11qs415ukoa.csv"

r = requests.get(url).json