# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 21:34:45 2023

@author: amrit
"""

year = int(input('Enter the year to check: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")