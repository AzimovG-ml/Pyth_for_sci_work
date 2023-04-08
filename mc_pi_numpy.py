#Numpy Pi Calc With MC
#Name: Azimov Genero    Date: 2/18
#UserId: kce2ue
#Homework #: 5
#Problem #: 2
#
#Program Name: mc_pi_numpy.py
#

#imports
import sys
import numpy as np
import time

#global variables
coord_amount=0
pi=0

#ensure valid user input at CL
#to use for rows of array
#won't except decimal values

def input_valid():
    global coord_amount
    if len(sys.argv)==2:
        try:
            '.' not in sys.argv[1]
            int(sys.argv[1])>0
            coord_amount=int(sys.argv[1])
        except:
            print("You must enter one non-zero, non-negative integer as a command line argument.")
    elif len(sys.argv)>2:
        print("You must enter only one non-zero, non-negative integer as a command line argument.")
    else:
        ("You must enter one non-zero, non-negative integer as a command line argument.")

#summate square of coord
#then sqrt pythag
#comp with bool
#count in, total from CL
#div in by total rows
#mult by area of square for circ area

def circ_area():
    global coord_amount, pi
    coord=np.random.rand(coord_amount,2)
    coord_squared=np.square(coord)
    coord_squared_sum=np.sum(coord_squared,axis=1)
    bool_with_rad=(np.sqrt(coord_squared_sum))<=1
    within_circ_quad= np.count_nonzero(bool_with_rad)
    ratio=(within_circ_quad/coord_amount)
    pi=ratio*4

#time circ_area
#print statement
#after stop time

def print_val():
    global coord_amount, pi
    start=time.time()
    circ_area()
    end=time.time()
    duration=end-start
    print(f"Using {coord_amount} MC points, pi is estimated to be {pi}.")
    print(f"This estimate took {duration} seconds to calculate.")

#input valid first
#only run if valid
input_valid()
if coord_amount!=0:
    print_val()
else:
    print("Please enter your comand-line argument appropriately next time.")

#LIST METHOD USING MC_PI.PY TOOK 13 TIMES AS LONG ROUGHLY