# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?h_r=next-challenge&h_v=zen

This challenge taken from website. 

@author: Ahmet Sefa Altundal
"""
import numpy
N,M = map(int,input().split())
l = []
for i in range(N):
    l.append(list(map(int,input().split())))
l = numpy.array(l)
print(l.mean(axis=1))
print(l.var(axis=0))
print(float(format(l.std(),".11f")))