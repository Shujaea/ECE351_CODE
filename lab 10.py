import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import control as con 

steps = 1 # Define step size
w = np. arange (1e3, 1e6 + steps , steps ) 

def Hs(R,L,C,w):
    
    Mag = (w/(R*C))/(np.sqrt((1/(L*C)-(w**2))**2+(w/(R*C))**2))
    Phase = 90-np.arctan((w/(R*C))/(1/(L*C)-(w**2)))*(180/np.pi)
    for i in range(len(Phase)):
        if (Phase[i] > 90):
            Phase[i] = Phase[i] - 180
    return Mag, Phase

#Task 1
R = 1000
L = 27e-3
C = 100e-9
Mag, Phase = Hs(R,L,C,w)
MagDB = 20*np.log10(Mag)
#Magnitude Plot   
plt.figure(figsize = (7, 5))
plt.subplot(2, 1, 1)
plt.semilogx(w, MagDB)
plt.grid()
plt.title('H(jw) by Hand')
plt.ylabel('Mag (dB)')
#Phase Plot
plt.subplot(2, 1, 2)
plt.semilogx(w, Phase)
plt.grid()
plt.xlabel('w (rad/s)')
plt.ylabel('Phase (deg)')

#Task 2
num = [0, 1/(R*C), 0]
den = [1, 1/(R*C), 1/(L*C)]

W2, Mag2, Phase2 = sig.bode((num,den), w)
plt.figure(figsize = (7, 5))
plt.subplot(2, 1, 1)
plt.semilogx(w, Mag2)
plt.grid()
plt.title('H(jw) built-in')
plt.ylabel('Mag (dB)')

plt.subplot(2, 1, 2)
plt.semilogx(w, Phase2)
plt.grid()
plt.xlabel('w(rad/s)')
plt.ylabel('Phase (deg)')

#Task 3
f = w/(2*np.pi)
plt.figure(figsize = (7, 5))
sys = con.TransferFunction(num, den)
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, Plot = True)

#Part 2
#Task 1
fm = 50000
fs = 2*fm
steps = 1/fs
t =np.arange(0, 0.01+steps, steps)

x = np.cos(2*np.pi*100*t) + np.cos(2*np.pi*3024*t) + np.sin(2*np.pi*50000*t)
plt.figure(figsize = (7, 5))
plt.plot(t, x)
plt.grid()
plt.title('Input Signal')
plt.ylabel('x(t)')
plt.xlabel('t(s)')

#Task 2
znum, zden = sig.bilinear(num, den, fs)
#Task 3
y = sig.lfilter(znum, zden, x)
#Task4
plt.figure(figsize = (7, 5))
plt.plot(t, y)
plt.grid()
plt.title('Output Signal')
plt.ylabel('y(t)')
plt.xlabel('t(s)')

plt.show()