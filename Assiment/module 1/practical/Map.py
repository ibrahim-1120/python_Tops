# Write a Python program to apply the map() function to square a list of numbers.

def square(a):
    return a*a

num={1,2,3,4,5,6,7}

k=list(map(square,num))

print(k)


# Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

def list(num):
    if not num:
        return 1
    p = reduce(lambda x,y:x*y,num)

    return p

print()

#  Write a Python program that filters out even numbers using the filter() function.


def even(number):
    return number%2==0


numbers=[1,2,3,4,5,6,7,8,9]

i=filter(even,numbers)


print(f"{i}")