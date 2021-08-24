# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/np-concatenate/problem

This challenge taken from website. 

@author: Ahmet Sefa Altundal
"""
import numpy as np
first,second,d = map(int,input().split())
def create_array(length):  
    array = []
    for i in range(length):
        array.append(list(map(int,input().split())))
    return np.array(array)
array_1 = create_array(first)
array_2 = create_array(second)
print (np.concatenate((array_1, array_2)))
  
