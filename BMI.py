# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:20:24 2023

@author: amrit
"""

height = input('Enter the height (in m): \n')
weight = input('Enter the weight (in kg): \n')

new_height = float(height)
new_weight = float(weight)

bmi = new_weight/ pow(new_height,2)

new_bmi = int(bmi)

print(f'Your BMI is {new_bmi}')