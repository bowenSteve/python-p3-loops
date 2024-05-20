#!/usr/bin/env python3

def happy_new_year():
    i=1
    while i<=10:
        print(i)
        print("Happy New Year!")
        i+=1

def square_integers(int_list):
    return [list*list for list in int_list]

def fizzbuzz():
    i=1
    while i<=100:
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)
        i+=1