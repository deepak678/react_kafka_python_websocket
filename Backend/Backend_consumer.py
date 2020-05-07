# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:15:23 2020

@author: v-deeman
"""
    from config import consumer

messages=[]
for msg in consumer:
    print(msg.value.decode())
    messages.append(msg.value)
    
    
