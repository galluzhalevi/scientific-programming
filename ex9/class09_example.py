import numpy as np
from numpy import pi, sin
from numpy.fft import fft
import matplotlib.pyplot as plt


dt = 1.0 / 2000
t = np.arange(0, 10, dt)

x = 3 * sin(2 * pi * t) + sin(8 * pi * t) + 0.5 * sin(14 * pi * t)

plt.subplot(1, 2, 1)
plt.plot(t, x, 'r', label="Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")


plt.subplot(1, 2, 2)
y = fft(x)
N = len(y)
n = np.arange(N)
freq = (2 * pi * n) / (N * dt)

plt.plot(freq, np.abs(y), 'b', label="Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, 50)
plt.tight_layout()

plt.show()
