# All documentation and comments are written by AI

import numpy as np
import pandas as pd
from numpy.fft import fft
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from music21 import pitch


# Function to convert frequency to musical note. Written by AI
def frequency_to_note(frequency):
    """
    Convert a given frequency to a musical note.

    Parameters:
    frequency (float): The frequency to convert.

    Returns:
    string: The musical note corresponding to the frequency.
    """
    p = pitch.Pitch()
    p.frequency = frequency
    return p.nameWithOctave


# Load the music data
data = pd.read_csv('music.csv', delimiter=',').to_numpy()

N = data.shape[0]  # Number of data points
dt = 0.1 / N  # Time step
t = np.arange(0, 10, dt)  # Time array

x = data[:, 0]  # Time data
y = data[:, 1]  # Amplitude data

# Plot the original signal
plt.subplot(1, 2, 1)
plt.plot(x, y, 'g', label="Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Compute and plot the Fourier spectrum
plt.subplot(1, 2, 2)
fourier = fft(y)  # Fourier transform
fourier_spectrum = np.abs(fourier) / N  # Spectrum
n = np.arange(N)  # Array of data point indices
freq = n / (N * dt)  # Frequency array

plt.plot(freq, fourier_spectrum, 'b', label="Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(200, 400)  # Limit the x-axis to the range 200-400 Hz

# Find the peaks in the spectrum
peaks, _ = find_peaks(fourier_spectrum, height=0.4)
plt.plot(freq[peaks[:]], fourier_spectrum[peaks[:]], 'rx')

# Print the frequency, note, and magnitude of the top 3 peaks. Written by AI
for peak in peaks[:3]:
    note = frequency_to_note(freq[peak])
    print(f"Frequency: {freq[peak]:.2f} Hz, Note: {note}, Magnitude: {fourier_spectrum[peak]:.2f}")

plt.show()  # Display the plots


# Output
# Frequency: 260.00 Hz, Note: C4, Magnitude: 0.48
# Frequency: 330.00 Hz, Note: E4, Magnitude: 0.99
# Frequency: 390.00 Hz, Note: G4, Magnitude: 0.48