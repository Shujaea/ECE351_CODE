
import pandas as pd
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import control as con 
import scipy.fftpack

def FFT(x, fs):
    N = len(x) 
    X_fft = scipy.fftpack.fft(x) 
    X_fft_shifted = scipy.fftpack.fftshift(X_fft) 
    freq = np.arange(-N/2, N/2) * fs/N 
    X_mag = np.abs(X_fft_shifted)/N
    X_phi = np.angle(X_fft_shifted)
    for n in range(len(X_phi)):
        if np.abs(X_mag[n]) < 1e-10:
            X_phi[n] = 0
    return freq, X_mag, X_phi

def make_stem(ax, x, y, color = 'k', style = 'solid', label ='', linewidths = 2.5,** kwargs):
    ax.axhline(x[0], x[-1], 0, color = 'r')
    ax.vlines(x, 0, y, color = color, linestyles = style, label = label, linewidths = linewidths)
    ax.set_ylim([1.05*y.min(), 1.05*y.max()])

#Get a noisy signal
X = pd.read_csv('NoisySignal.csv')
t = X['0'].values
Signal = X['1'].values

plt.figure(figsize = (7, 5))
plt.plot(t, Signal)
plt.xlabel('t (s)')
plt.ylabel('Amp(V)')
plt.grid()
plt.title('Noisy Signal')
     
fs = 1/(t[1]-t[0])
Sig_F, Sig_Mag, Sig_Phi = FFT(Signal, fs)
	
fig, ax = plt.subplots(figsize=(7, 3))

make_stem(ax, Sig_F, Sig_Mag)
plt.ylabel('Magnitude')
plt.xlabel('F(Hz)')
plt.title("Frequency Responce of The Noisy Signal")

fig, ax = plt.subplots(figsize=(7, 3))
make_stem(ax, Sig_F, Sig_Mag)
plt.xlim(0, 1800)
plt.ylabel('Magnitude')
plt.xlabel('F(Hz)')
plt.title("Frequency Responce of Low Frequency Noise")

fig, ax = plt.subplots(figsize =(7, 3))
make_stem(ax, Sig_F, Sig_Mag)
plt.xlim(1790, 2010)
plt.ylabel('Magnitude')
plt.xlabel('F(Hz)')
plt.title("Frequency Responce of Position Signal")


fig, ax = plt.subplots(figsize =(7, 3))
make_stem(ax, Sig_F, Sig_Mag)
plt.xlim(40000, 60000)
plt.ylabel('Magnitude')
plt.xlabel('Freq(Hz)')
plt.title("Frequency Responce of High Frequency Noise")

#Filter Paramaters
R = 3e3
L = 0.8
C = 9e-9
Filter_Num = [R/L, 0]
Filter_Den = [1, R/L, 1/(L*C)]

step = 0.5
w = np.arange(100, 6e5+step, step)

plt.figure(figsize = (7, 4))
sys = con.TransferFunction(Filter_Num, Filter_Den)
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, Plot = True)

plt.figure(figsize = (7, 4))
sys = con.TransferFunction(Filter_Num, Filter_Den)
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, Plot = True)
plt.xlim(0, 1800)

plt.figure(figsize = (7, 4))
sys = con.TransferFunction(Filter_Num, Filter_Den)
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, Plot = True)
plt.xlim(1600, 2200)

plt.figure(figsize = (7, 4))
sys = con.TransferFunction(Filter_Num, Filter_Den)
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, Plot = True)
plt.xlim(40000, 60000)

F_Num, F_Den = sig.bilinear(Filter_Num, Filter_Den, fs=fs)
Filtered_Sig = sig.lfilter(F_Num, F_Den, Signal)

Sig_F, Sig_Mag, Sig_Phi = FFT(Filtered_Sig, fs)

plt.figure(figsize = (7, 3))
plt.subplot(1, 1, 1)
plt.plot(t, Filtered_Sig)
plt.xlabel('t(s)')
plt.ylabel('Amp (V)')
plt.title('Filtered  Signal')
plt.grid()

fig, ax = plt.subplots(figsize=(7, 3))
make_stem(ax, Sig_F, Sig_Mag)
plt.title("Frequency Responce of the Filtered Signal")
plt.ylabel('Magnitude')
plt.xlabel('F(Hz)')

fig, ax = plt.subplots(figsize=(7, 3))
make_stem(ax, Sig_F, Sig_Mag)
plt.title("Frequency Responce of the Filtered Low Frequency Noise")
plt.ylabel('Magnitude')
plt.xlabel('F(Hz)')
plt.xlim(0, 1800)

fig, ax = plt.subplots(figsize =(7, 3))
make_stem(ax, Sig_F, Sig_Mag)
plt.title("Frequency Responce of the Filtered Position Signal")
plt.ylabel('Magnitude')
plt.xlabel('F(Hz)')
plt.xlim(1790, 2010)

fig, ax = plt.subplots(figsize =(7, 3))
make_stem(ax, Sig_F, Sig_Mag)
plt.title("Frequency Responce of the Filtered High Frequency Noise")
plt.ylabel('Magnitude')
plt.xlabel('Freq(Hz)')
plt.xlim(40000, 60000)
plt.show()



