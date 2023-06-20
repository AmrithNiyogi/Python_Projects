# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:00:44 2023

@author: amrit
"""

import random as r

name_string = input('Enter the names separated by a comma(,).\n')
names = name_string.split(",")

num_items = len(names)

random_choice = r.randint(0, num_items-1)
person_paying = names[random_choice]

print(f'{person_paying} will buy the meal today')