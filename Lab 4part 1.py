import numpy as np
import matplotlib . pyplot as plt
import math


steps = 1e-2 # Define step size
t = np. arange (-10, 10 + steps , steps ) 

# user defined function
def step (t): 
    y = np. zeros (t. shape ) 
    for i in range ( len (t)): 
        if t[i] >= 0:  
            y[i] = 1
        else:
            y[i] = 0
    return y 

def ramp (t): 
    y = np. zeros (t. shape ) 
    for i in range ( len (t)): 
        if t[i] >= 0:  
            y[i] = t[i]
        else:
            y[i] = 0
    return y 

def h1(t):
    y = np.exp(-2*t) *(step (t) - step (t-3))
    return y

def h2(t):
    y = step (t-2) - step (t-6)
    return y

def h3(t):
    y =  np.cos(2 * math.pi *0.25 *t) * step (t)
    return y

plt. figure ( figsize = (10 , 7))
plt. subplot (3, 1, 1)
plt. plot (t, h1(t))
plt. grid ()
plt. ylabel ('h1(t)')
plt. title (' Task 1')
plt. subplot (3, 1, 2)
plt. plot (t, h2(t))
plt. grid ()
plt. ylabel ('h2(t)')
plt. subplot (3, 1, 3)
plt. plot (t, h3(t))
plt. grid ()
plt. ylabel ('h3(t)')
plt. xlabel ('t')

plt. show ()