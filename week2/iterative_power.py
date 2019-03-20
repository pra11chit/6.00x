#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 00:27:43 2019

@author: pratikchitode@gmail.com
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result=1 #clever use
    while exp>0:
        result*=base
        exp-=1
    return result
