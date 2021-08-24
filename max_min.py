# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/np-min-and-max/problem

This challenge taken from website. 

@author: Ahmet Sefa Altundal
"""

import numpy
N,M = map(int,input().split())
l = []
for i in range(N):
    l.append(list(map(int,input().split())))
l = numpy.array(l)
print(l.min(axis=1).max())