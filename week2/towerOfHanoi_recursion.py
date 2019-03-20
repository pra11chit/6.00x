#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 00:47:01 2019

@author: pratikchitode@gmail.com
"""

#Tower of Hanoi Problem by recursion

def print_tower(fro,to):
    print("Move"+str(fro)+"to"+str(to))


def tower(fro,to,spare,n):
    if n==1:
        print_tower(fro,to)
        
    else:
        tower(fro,spare,to,n-1)   
        tower(fro,to,spare,1)
        tower(spare,to,fro,n-1)
print(tower('P1','P2','P3',4))
        