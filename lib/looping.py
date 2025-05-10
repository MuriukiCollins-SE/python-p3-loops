#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    for i in range(len(int_list)):
        int_list[i] = int_list[i] ** 2
    return int_list

def fizzbuzz():
    for i in range(1, 101):  # Corrected 'fori' to 'for'
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)