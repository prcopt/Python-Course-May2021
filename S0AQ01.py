""" S0AQ01
A melting furnace converts a hollow sphere into a solid cylinder of 3cm diameter with a 5% loss. 
Write a program that finds out the length of the solid cylinder when
the inner and external radii of the hollow sphere are known

Volume of sphere = 4/3 * pi * r * r * r
Volume of cylinder = pi * r * r * height

"""
from math import pi
def cyl_vol(r):
    v = 4/3*pi*r**3
    return v

def get_number(text):
    n = float(input(text))
    return n

# Main starts from here
rad_i = get_number("Enter Inner radius of sphere:")
rad_o = get_number("Enter Outer radius of sphere:")
sph_vol_o = (4/3)*pi*rad_o**3 # outter volume of sphere
sph_vol_i = (4/3)*pi*rad_i**3 # inner volume of sphere

mat_vol = sph_vol_o - sph_vol_i
mat_vol *= (1-0.05) # remove a loss of 5%

cyl_dia = 3.0
cyl_ht = (4*mat_vol)/(pi*cyl_dia**2)
print("Cylinder height: ",cyl_ht)

