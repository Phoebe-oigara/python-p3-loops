#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

def square_integers(int_list):
    squared_integers  = []

    for int in int_list:
        squared_integers.append(int ** 2)
    return squared_integers

def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n% 3 == 0:
            print ("Fizz")
        elif n % 5 == 0:
            print ("Buzz")
        else:
            print(n)
