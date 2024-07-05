#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter - 1
        print("Happy New Year")

def square_integers(int_list):
    # code goes here!
   int_list = [value * 2 for value in int_list]
   return int_list


def fizzbuzz():
    # code goes here!
    for num in range (1, 101):
        if (num % 3 == 0) and (num % 5 == 0):
            print("FrizzBuzz")
        elif (num % 3 == 0):
            print("Frizz")
        elif (num % 5 == 0):
            print("Buzz")
        else:
            print(num)



