# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# This program is used to get the pelidrome of a word, it can also be used
# to get the pelidrome of a sentence too.
# A pelidrome is when the word or a sentence is divided in two,
# the letters or words reflect each other.
# Examples are madam, Rotor, Sator Arepo Tenet Opera Rotas, level, kayak,
# Able was I ere I saw Elba, reer, deed, ect..


Array = []
Pelidrome_input = input("Input word or a sentence to check for pelidrome: ")
Divide2 = len(Pelidrome_input)
Input_size = len(Pelidrome_input)
counter = 0
for j in range(Input_size):
    Array.append(Pelidrome_input[j])
size_array = len(Array)
for i in range(Divide2):
    if Array[i].lower() != Array[size_array-1-i].lower():
        counter = counter + 1
if counter == 0:
    print("It's a pelidrome\n")
else:
    print("It's not a pelidrome\n")
