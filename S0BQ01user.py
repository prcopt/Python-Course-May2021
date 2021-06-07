""" S0BQ01User
This file make use of function defined in another module (S0BQ01).

Write a Python function, that asks the user if he wants to continue. 
It should print “continue” and return True, if the user types in a yes,
irrespective of the case in which “yes” is typed. 

Import this function in any of your earlier exercises and 
run that exercise in a loop as long as the user enters “No”

"""
from math import pi
import S0BQ01

def cyl_vol(r):
    v = 4/3*pi*r**3
    return v

def get_number(text):
    n = float(input(text))
    return n

# Main starts from here
wish = True
while wish:
    rad_i = get_number("Enter Inner radius of sphere:")
    rad_o = get_number("Enter Outer radius of sphere:")
    sph_vol_o = (4/3)*pi*rad_o**3 # outter volume of sphere
    sph_vol_i = (4/3)*pi*rad_i**3 # inner volume of sphere

    mat_vol = sph_vol_o - sph_vol_i
    mat_vol *= (1-0.05) # remove a loss of 5%

    cyl_dia = 3.0
    cyl_ht = (4*mat_vol)/(pi*cyl_dia**2)
    print("Cylinder height: ",cyl_ht)
    wish = S0BQ01.get_YesNo()
