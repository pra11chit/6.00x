#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 00:36:43 2019

@author: pratikchitode@gmail.com

"""

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

