import numpy as np
import matplotlib . pyplot as plt
import math
import scipy . signal as sig


steps = 1e-2 # Define step size
t = np. arange (-10, 10 + steps , steps ) 
w0 = 2 * math.pi *0.25 

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
    y =  np.cos(w0 *t) * step (t)
    return y

def conv(fu1, fu2):
    conf1 = len (fu1 )
    conf2 = len (fu2 )
    f1E = np. append (fu1 , np. zeros ((1 , conf2 -1) ))
    f2E = np. append (fu2 , np. zeros ((1 , conf1 -1) ))
    Value = np. zeros (f1E . shape )
    for i in range ( conf2 + conf1 - 2):
        Value [i] = 0
        for j in range ( conf1 ):
            if(i - j + 1 > 0):
                Value [i] += f1E [j]* f2E [i - j + 1]
    return Value

y1 = conv(h1(t),step (t)) #user-created convolution
Y1 = sig.convolve(h1(t),step (t)) #Built-in convolution

y2 = conv(h2(t),step (t)) #user-created convolution
Y2 = sig.convolve(h2(t),step (t)) #Built-in convolution

y3 = conv(h3(t),step (t)) #user-created convolution
Y3 = sig.convolve(h3(t),step (t)) #Built-in convolution

t = np.linspace(-10, 10, len(y1))


plt. figure ( figsize = (10 , 7))
plt. subplot (2, 1, 1)
plt. plot (t, y1)
plt. grid ()
plt. ylabel ('y1(t)')
plt. title (' First responce')
plt. subplot (2, 1, 2)
plt. plot (t, Y1)
plt. grid ()
plt. ylabel ('Y1(t)')
plt. xlabel ('t')

plt. figure ( figsize = (10 , 7))
plt. subplot (2, 1, 1)
plt. plot (t, y2)
plt. grid ()
plt. ylabel ('y2(t)')
plt. title (' Second responce')
plt. subplot (2, 1, 2)
plt. plot (t, Y2)
plt. grid ()
plt. ylabel ('Y2(t)')
plt. xlabel ('t')

plt. figure ( figsize = (10 , 7))
plt. subplot (2, 1, 1)
plt. plot (t, y3)
plt. grid ()
plt. ylabel ('y3(t)')
plt. title (' Third responce')
plt. subplot (2, 1, 2)
plt. plot (t, Y3)
plt. grid ()
plt. ylabel ('Y3(t)')
plt. xlabel ('t')

#hand Calculated step responce
y1c = 0.5 * (1 - np.exp(-2*t)) * (step (t) - step (t-3)) + 0.5 * step (t-3)
y2c = (t-2) * (step (t-2) - step (t-6)) + 4 * step (t-6)
y3c = np.cos(w0 *t) * step (t) / w0

plt. figure ( figsize = (10 , 7))
plt. subplot (3, 1, 1)
plt. plot (t, y1c)
plt. grid ()
plt. ylabel ('y1c(t)')
plt. title (' Step Respnoce (Hand Calculated)')
plt. subplot (3, 1, 2)
plt. plot (t, y2c)
plt. grid ()
plt. ylabel ('y2c(t)')
plt. subplot (3, 1, 3)
plt. plot (t, y3c)
plt. grid ()
plt. ylabel ('y3c(t)')
plt. xlabel ('t')

plt. show ()
