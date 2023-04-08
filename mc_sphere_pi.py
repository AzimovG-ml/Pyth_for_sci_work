#Numpy Volume Calc With MC
#Name: Azimov Genero    Date: 2/21
#UserId: kce2ue
#Homework #: 5
#Problem #: 3
#
#Program Name: mc_sphere.py
#

#imports
import sys
import numpy as np
import time
import math

#global variables
coord_amount=0
rad=0
vol=0
expected_vol=0

#ensure valid user input at CL
#to use for rows of array
#won't except decimal values in coord_amount
#will accept any input convertable into float value that doesn't equal 0.0
#for the radius value

def input_valid():
    global coord_amount,rad
    if len(sys.argv)==3:
        #first command line MC, non-zero, non-negative, integer
        try:
            '.' not in sys.argv[1]
            int(sys.argv[1])>0
            coord_amount=int(sys.argv[1])
        except:
            print("You must enter your first command line argument as a non-zero, non-negative integer.")
        #second command line can be decimal, non-negative, non-zero
        try:
            float(sys.argv[2])!=0.0
            rad=float(sys.argv[2])
        except:
            print("Your second command line argument must be a real-number, that isn't negative or zero..")
    elif len(sys.argv)>3:
        print("Too many command line arguments.")
    else:
        print("Insufficient command line arguments.")

#summate square of coord
#then sqrt pythag
#comp with bool
#count in, total from CL
#ratio in/total
#vol equals ratio times cube vol

def sphere_vol(): 
    global coord_amount, rad,vol,expected_vol
    scale=rad
    coord=rad*np.random.rand(coord_amount,3)
    coord=coord.reshape(coord_amount,3)
    coord_squared=np.square(coord)
    coord_squared_sum=np.sum(coord_squared,axis=1)
    bool_within_sphere=(np.sqrt(coord_squared_sum))<=rad
    within_sphere_quad= np.count_nonzero(bool_within_sphere)
    ratio=(within_sphere_quad/coord_amount)
    vol=(ratio*((2*rad)**3))
    expected_vol=(math.pi)*(4/3)*(rad**3)

#time circ_vol
#print statement
#after stop time
#state rows and radius
#state time
#comp to expected vol, 4/3*pi*r^3

def print_val():
    global coord_amount, rad, vol, expected_vol
    start=time.time()
    sphere_vol()
    end=time.time()
    duration=end-start
    print(f"Using {coord_amount} MC points and a radius of {rad}, the volume is estimated to be {vol}.")
    print(f"The expected volume was {expected_vol}, a difference of {abs((expected_vol)-(vol))}.")
    print(f"This estimate took {duration} seconds to calculate.")

#input valid first
#only run if valid
input_valid()
if coord_amount!=0 and rad!=0:
    print_val()
else:
    print("Please enter your comand-line arguments appropriately next time.")

#REGARDING NTH DIMENSIONS
#assuming (2*rad)**n=volume of cube of nth-dimension
#use a coordinate for each dimension when generating boolean of whether points of n dimensions fall within nth-dimension sphere
#evaluate this by squaring each dimensional coordinate, adding, and then square rooting the sum. finally see if<=rad
#(points evaluated should have 'random' coordinates from 0.0 to float(rad))
#divide within points by all points
#multiply ratio by vol of nth dimension cube

#e.g., let's say our radius of the circumscribed sphere is 2
#let's assume its in the 4th dimension and points are described by (x,y,z,t)
#so square each, add, and then take sqrt- sqrt(x**2+y**2+z**2+t**2)<=2
#evaluate each row in this manner
#find ratio of those evaluated inside vs all rows
#multiply by 4**4 (A cube with edge lengths of 4 in the fourth dimension.)
