# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:16:46 2020

@author: v-deeman
"""

from flask import Flask
from kafka import KafkaProducer
from flask_cors import CORS
from kafka import KafkaConsumer

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='192.168.0.103:9092')
consumer = KafkaConsumer('test', bootstrap_servers=['192.168.0.103:9092'])
cors=CORS(app)