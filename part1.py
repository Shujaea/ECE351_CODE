import numpy as np
import matplotlib . pyplot as plt


steps = 1e-2 # Define step size
t = np. arange (-5, 10 + steps , steps ) 

# user defined function
def step (t,tn): 
    y = np. zeros (t. shape ) 
    for i in range ( len (t)): 
        if t[i] >= -tn:  
            y[i] = 1
    return y 

def ramp (t, tn, m): 
    y = np. zeros (t. shape ) 
    for i in range ( len (t)): 
        if t[i] >= -tn:  
            y[i] = m * (t[i] + tn)
    return y 

X1 = 5 * step (t,-3) 
X2 = ramp(t, 0, 2)
plt. figure ( figsize = (10 , 7))
plt. subplot (2, 1, 1)
plt. plot (t, X1)
plt. grid ()
plt. ylabel ('X1(t)')
plt. xlabel ('t')
plt. title (' X1 = 5u(t-3)')

plt. subplot (2, 1, 2)
plt. plot (t, X2)
plt. grid ()
plt. ylabel ('X2(t)')
plt. xlabel ('t')
plt. title (' X2 = 2r(t)')
plt. show ()