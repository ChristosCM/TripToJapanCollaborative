# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:41:03 2017

@author: Chris
"""
import matplotlib.pyplot as plt
def satisfy():
    satisfy=[]
    for i in range (0, 5):
        print 'From 1 to 3 how much did you like the trip?'
        x=input(':')
        satisfy.append(x)
    c1=0
    c2=0
    c3=0
    for i in range (0,5):
        if satisfy[i]==1 :
            c1=c1+1
        elif satisfy[i]==2:
            c2=c2+1
        elif satisfy[i]==3:
            c3=c3+1
    print satisfy
    plt.hist(satisfy)
    plt.savefig('graph1.png')