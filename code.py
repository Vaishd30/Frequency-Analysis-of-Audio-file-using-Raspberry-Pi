import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
# Open the audio file
audio_file = wave.open('audio_file.wav', 'r')
# Get the number of frames and framerate
num_frames = audio_file.getnframes()
framerate = audio_file.getframerate()
# Read in the audio data
audio_data = audio_file.readframes(num_frames)
# Convert the audio data to a numpy array
audio_data = np.frombuffer(audio_data, dtype=np.int16)
# Calculate the Fourier transform of the audio data
fft_data = np.fft.fft(audio_data)
# Get the frequency bins
freq_bins = np.fft.fftfreq(len(fft_data), 1.0/framerate)
# Plot the frequency spectrum
plt.plot(freq_bins, np.abs(fft_data))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
# Find the peak frequency and amplitude
peak_idx = np.argmax(np.abs(fft_data))
peak_freq = freq_bins[peak_idx]
peak_amp = np.abs(fft_data[peak_idx])
# Display the fundamental frequency
print('Fundamental frequency:', peak_freq, 'Hz')
# Find the harmonics
harmonics = []
for i in range(2, 10):
 harmonic_freq = i * peak_freq
 harmonic_idx = np.argmin(np.abs(freq_bins - harmonic_freq))
 harmonic_amp = np.abs(fft_data[harmonic_idx])
 if harmonic_amp > 0.1 * peak_amp:
 harmonics.append(harmonic_freq)
 print('Harmonic', i, 'frequency:', harmonic_freq, 'Hz')
 plt.axvline(harmonic_freq, color='r')
plt.show()