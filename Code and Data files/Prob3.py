import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

plt.style.use('ggplot')

# ----------------------------- Prob 3c -------------------------------- #

def prob_3c():
    freq_3c, vinout_3c = np.loadtxt('prob3c.txt', delimiter=',', unpack=True, skiprows=1) # Data, where R_b = 100Ohm

    plt.axhline(y=17, color='black', linestyle='dashdot', label=r'$-3$ dB', linewidth=0.7)
    plt.axvline(x=1e6, color='black', linestyle='--', label=r'$\omega_0$', linewidth=0.7) 
    plt.plot(freq_3c, vinout_3c)
    plt.xlabel('Frequency [Hz]')
    plt.xscale('log')
    plt.ylabel('Decibels [dB]')
    plt.yticks(np.arange(-13, 24, 3))
    plt.ylim(-13, 22)                                              
    plt.title(r"Frequency Response of circuit (b)")
    plt.legend()
    plt.show()


# ----------------------------- Prob 3d -------------------------------- #

def prob_3d():
    time_1, vin_3d_1, vout_3d_1 = np.loadtxt('prob3d.txt', delimiter=',', unpack=True, skiprows=1) # Data, where R_b = 100Ohm
    time_2, vin_3d_2, vout_3d_2 = np.loadtxt('prob3d_ink_updown_V.txt', delimiter=',', unpack=True, skiprows=1) # Data, where R_b = 100Ohm

    plt.axvline(x=1e-6, color='black', linestyle='--', linewidth=0.7)
    plt.plot(time_1, vin_3d_1, label=r'$V_{in}$')
    plt.plot(time_1, vout_3d_1, label=r'$V_{out}$')
    plt.ylim(-1, 0.140)
    plt.yticks(np.arange(-1, 0.2, 0.1))
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.title(r".tran simulation with a step response circuit (b)")
    plt.legend()
    plt.show()

    #plt.axvline(x=2.21e-6, color='black', linestyle='--', linewidth=0.7)
    plt.plot(time_2, vin_3d_2, label=r'$V_{in}$')
    plt.plot(time_2, vout_3d_2, label=r'$V_{out}$')
    plt.ylim(-1, 0.140)
    plt.yticks(np.arange(-1, 0.2, 0.1))
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.title(r".tran simulation with a step response circuit (b)")
    plt.legend()
    plt.show()

# ----------------------------- Prob 3e -------------------------------- #

def prob_3e():
    freq_3e, vinout_3e = np.loadtxt('prob3e.txt', delimiter=',', unpack=True, skiprows=1) # Data, where R_b = 100Ohm

    plt.axhline(y=17, color='black', linestyle='dashdot', label=r'$-3$ dB', linewidth=0.7)
    plt.axvline(x=1e6, color='black', linestyle='--', label=r'$f_c$' ,linewidth=0.7)
    plt.axvline(x=1e4, color='black', linestyle='--',  linewidth=0.7)
    plt.plot(freq_3e, vinout_3e, label=r'$H(\omega)$')
    plt.xlabel('Frequency [Hz]')
    plt.xscale('log')
    plt.ylabel('Decibels [dB]')
    plt.title(r"band-pass filter")
    plt.legend()
    plt.show()

def prob_3f():
    time_3f, vin_3f, vout_3f = np.loadtxt('prob3f_timedomain.txt', delimiter=',', unpack=True, skiprows=1) # Data, where R_b = 100Ohm

    freq_3f, vinout_3f, phase_3f = np.loadtxt('prob3f_freq_domain.txt', delimiter=',', unpack=True) # Data, where R_b = 100Ohm
    
    plt.plot(time_3f, vin_3f, label=r'$V_{in}$')
    plt.plot(time_3f, vout_3f, label=r'$V_{out}$')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.xscale('log')
    plt.title(r"Time domain")
    plt.legend()
    plt.show()
    
    plt.axhline(y=-64.875, color='teal', linestyle='dashdot', label=r'Max value', linewidth=0.7)
    plt.axhline(y=-64.875-3, color='black', linestyle='dashdot', label=r'$-3$ dB', linewidth=0.7)
    plt.axvline(x=1e6, color='black', linestyle='--', label=r'$f_c$' ,linewidth=0.7)
    plt.axvline(x=1e4, color='black', linestyle='--',  linewidth=0.7)
    plt.plot(freq_3f, vinout_3f)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Decibels [dB]')
    plt.xscale('log')
    plt.title(r"Fourier domain")
    plt.legend()
    plt.show()
    
    

if __name__ == "__main__":
    #prob_3c()
    #prob_3d()
    #prob_3e()
    prob_3f()