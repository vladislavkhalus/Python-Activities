# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
array = []
pelidrome_input = input("Input word to check for pelidrome ")
divide2 = len(pelidrome_input)
input_size = len(pelidrome_input)
counter = 0
for j in range(input_size):
    array.append(pelidrome_input[j])
size_array = len(array)
for i in range(divide2):
    if array[i] != array[size_array-1-i]:
        counter = counter + 1
if counter == 0:
    print("It's a pelidrome\n")
else:
    print("It's not a pelidrome\n")
