# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 11:54:47 2022

@author: Ian Ah
"""
#Question Number 2
I = 2

i = 2.0

D = 10j

d = "2 Cool for School"

V = True

type(I)
type(i)
type(D)
type(d)
type(V)

#Question Number 3
A = [2,2.0,10j,"2 Cool for School",True]

#Question Number 4
B = "I like pie more than cake."

B[:6]

B[7:15]

B[16:25]

B[:6]+B[10:15]+B[20:25]

#Question Number 5
def Foobar_function (multiple: int) ->int: 
    """This function allows the user to input an integer and return either 
    foo, bar, or foobar depending if it is a multiple of 3, 5, or 15.
    >>> 9
    foo
    >>> 10
    bar
    >>> 15
    foobar
    """
    
    if (multiple % 15 == 0 and multiple % 5 == 0 and multiple % 3 == 0):
       return print("foobar")
    elif (multiple % 15 == 0):
        return print("foobar")
    elif (multiple % 5 == 0):
        return print("bar")
    elif (multiple % 3 == 0):
        return print("foo")
    elif (multiple > 0):
        return print("Not a multiple of 3,5, or 15")

Foobar_function(10)


