import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

plt.style.use("ggplot")


# ----------------------------- Prob 2c -------------------------------- #
freq_b, vinout_b = np.loadtxt('prob2c_fc_not.txt', delimiter=',', unpack=True, skiprows=1) # Data, where R_b = 100Ohm

plt.axvline(x=1e6, color='black', linestyle='--', label=r'$f_c$', linewidth=0.7)
plt.axhline(y=-3, color='black', linestyle='dashdot', label=r'$-3$ dB', linewidth=0.7)
plt.plot(freq_b, vinout_b, label=r'$|H_b(\omega)|$')
plt.xlabel('Frequency [Hz]')
plt.xscale('log')
plt.ylabel('Decibels [dB]')
plt.yticks(np.arange(-21, 6, 3))
plt.ylim(-21, 6)
plt.xlim(1e4, 1.5e7)
plt.title(r"Amplitude Response of $|H_b(\omega)|$)")
plt.legend()
plt.show()


"""Plots the frequency response of the two filters with R_a=R_b = 100 Ohm."""
# Read in the data
freq, vinout_1, vinout_2 = np.loadtxt('prob2c_and_d.txt', delimiter=',', unpack=True, skiprows=1) # Data, where R_b = 100Ohm

# Plot the data
plt.axvline(x=1e6, color='black', linestyle='--', label=r'$f_c$', linewidth=0.7)
plt.axhline(y=-3, color='black', linestyle='dashdot', label=r'$-3$ dB', linewidth=0.7)
plt.plot(freq, vinout_1, label=r'$|H_a(\omega)|$')
plt.plot(freq, vinout_2, label=r'$|H_b(\omega)|$', color = "teal")
plt.xlabel('Frequency [Hz]')
plt.xscale('log')
plt.ylabel('Decibels [dB]')
plt.yticks(np.arange(-20, 17, 3))
plt.ylim(-20, 18)
plt.xlim(1e4, 1.5e7)
plt.title(r"Amplitude Response of $|H_a(\omega)|$ and $|H_b(\omega)|$)")
plt.legend()
plt.show()

# ----------------------------- Prob 2d -------------------------------- #

freq_80, vinout_80 = np.loadtxt('prob2d_r80.txt', delimiter=',', unpack=True, skiprows=1) # Data, where R_b = 100Ohm
freq_120, vinout_120 = np.loadtxt('prob2d_r120.txt', delimiter=',', unpack=True, skiprows=1) # Data, where R_b = 100Ohm

plt.axvline(x=1e6, color='black', linestyle='--', label=r'$f_c$', linewidth=0.7)
plt.axhline(y=-3, color='black', linestyle='dashdot', label=r'$-3$ dB', linewidth=0.7)
plt.plot(freq_120, vinout_120, label=r'$|H_b(\omega)|$ with $R_b = 120 \Omega$')
plt.plot(freq, vinout_2, label=r'$|H_a(\omega)|$ with $R_b = 100 \Omega$')
plt.plot(freq_80, vinout_80, label=r'$|H_b(\omega)|$ with $R_b = 80 \Omega$')
plt.xlabel('Frequency [Hz]')
plt.xscale('log')
plt.ylabel('Decibels [dB]')
plt.yticks(np.arange(-25, 5, 3))
plt.ylim(-25, 5)
plt.xlim(1e4, 1.5e7)
plt.title(r"Amplitude responses $|H_b(\omega)$| with $R_b \pm20\%$")
plt.legend()
plt.show()


plt.axvline(x=1e6, color='black', linestyle='--', label=r'$f_c$', linewidth=0.7)
plt.axhline(y=-3, color='black', linestyle='dashdot', label=r'$-3$ dB', linewidth=0.7)
plt.plot(freq_120, vinout_120, label=r'$|H_b(\omega)|$ with $R_b = 120 \Omega$')
plt.plot(freq, vinout_2, label=r'$|H_b(\omega)|$ with $R_b = 100 \Omega$')
plt.plot(freq_80, vinout_80, label=r'$|H_b(\omega)|$ with $R_b = 80 \Omega$')
plt.plot(freq, vinout_1, label=r'$|H_a(\omega)|$')
plt.xlabel('Frequency [Hz]')
plt.xscale('log')
plt.ylabel('Decibels [dB]')
plt.yticks(np.arange(-25, 5, 3))
plt.ylim(-25, 5)
plt.xlim(1e4, 1.5e7)
plt.title(r"Frequency Response of $H_a(\omega)$ and $H_b(\omega)$)")
plt.legend()
plt.show()