import numpy as np
import matplotlib . pyplot as plt


steps = 1e-2 
t = np. arange (-5, 10 + steps , steps ) 
N=len (t)

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
    return y # 
ym= np. zeros ([5, N] )
ym[0,:]= ramp(t,0,1) 
ym[1,:]= ramp(t,-3,-1) 
ym[2,:]= 5 * step (t,-3) 
ym[3,:]= -2 * step (t,-6)
ym[4,:]= ramp(t,-6,-2) 

y= [sum(x) for x in zip(*ym)]


plt. figure ( figsize = (10 , 7))
plt. plot (t, y)
plt. grid ()
plt. ylabel ('y(t)')
plt. xlabel ('t')
plt. title (' Task 3)')

plt. show ()