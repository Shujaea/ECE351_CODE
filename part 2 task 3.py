import numpy as np
import matplotlib . pyplot as plt


steps = 1e-2 
t = np. arange (-5, 10 + steps , steps ) 


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

y= ramp(t,0,1) + ramp(t,-3,-1) + 5 * step (t,-3) -2 * step (t,-6) + ramp(t,-6,-2)

#Task 1
yf = np.flip(y)
tf = np.flip(-t)
plt. figure ( figsize = (10 , 7))
plt. subplot (2, 1, 1)
plt. plot (t, y)
plt. grid ()
plt. ylabel ('y(t)')
plt. title (' time reverse signal')
plt. subplot (2, 1, 2)
plt. plot (tf, yf)
plt. grid ()
plt. ylabel ('y(-t)')
plt. xlabel ('t')


#Task 2
td = t + 4
tdf = np.flip(-td)
plt. figure ( figsize = (10 , 7))
plt. subplot (3, 1, 1)
plt. plot (t, y)
plt. grid ()
plt. ylabel ('y(t)')
plt. title ('time shifting signal')
plt. subplot (3, 1, 2)
plt. plot (td, y)
plt. grid ()
plt. ylabel ('y(t-4)')
plt. subplot (3, 1, 3)
plt. plot (tdf, yf)
plt. grid ()
plt. ylabel ('y(-t-4)')
plt. xlabel ('t')

#Task 3
t1 = t*2
t2 = t/2
plt. figure ( figsize = (10 , 7))
plt. subplot (3, 1, 1)
plt. plot (t, y)
plt. grid ()
plt. ylabel ('y(t)')
plt. title (' time scale signal')
plt. subplot (3, 1, 2)
plt. plot (t1, y)
plt. grid ()
plt. ylabel ('y(t/2)')
plt. subplot (3, 1, 3)
plt. plot (t2, y)
plt. grid ()
plt. ylabel ('y(2t)')
plt. xlabel ('t')

#Task 4
yd = np.diff(y)
t3 = np. arange (-5, 10  , steps )
plt. figure ( figsize = (10 , 7))
plt. subplot (2, 1, 1)
plt. plot (t, y)
plt. grid ()
plt. ylabel ('y(t)')
plt. title (' derivative signal')
plt. subplot (2, 1, 2)
plt. plot (t3 , yd)
plt. grid ()
plt. ylabel ('diff y(t)')
plt. xlabel ('t')

plt. show ()