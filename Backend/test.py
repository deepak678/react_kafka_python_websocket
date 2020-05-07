# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:37:53 2020

@author: v-deeman
"""
from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers=['13.82.142.57:9092'])

for msg in consumer:
    print(msg.value)