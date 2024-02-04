# Scipy is a great library for scientific computing!!! 
# I used a lot the theilslopes function :) for a more robust slope computation.

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


x = np.linspace(-5, 5, num=150)
y = x + np.random.normal(size=x.size)
y[11:15] += 10  # add outliers
y[-5:] -= 7

res = stats.theilslopes(y, x, 0.90, method='separate')
lsq_res = stats.linregress(x, y)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'b.')
ax.plot(x, res[1] + res[0] * x, 'r-')
ax.plot(x, res[1] + res[2] * x, 'r--')
ax.plot(x, res[1] + res[3] * x, 'r--')
ax.plot(x, lsq_res[1] + lsq_res[0] * x, 'g-')
plt.show()



from scipy import stats

# Calculate the mode of a dataset
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mode = stats.mode(data)

# Perform t-test for comparing means of two samples
sample1 = [1, 2, 3, 4, 5]
sample2 = [3, 4, 5, 6, 7]
t_stat, p_value = stats.ttest_ind(sample1, sample2)

from scipy import linalg

# Solve a system of linear equations
coefficients = np.array([[2, 3], [1, -1]])
constants = np.array([23, -3])
solution = linalg.solve(coefficients, constants)

# Calculate the determinant of a matrix
matrix = np.array([[1, 2], [3, 4]])
determinant = linalg.det(matrix)

from scipy import signal

# Create a simple signal
t = np.linspace(0, 1, 1000, endpoint=False)
frequency = 5
signal_data = np.sin(2 * np.pi * frequency * t)

# Apply a butterworth filter to the signal
b, a = signal.butter(4, 0.2, 'low')
filtered_signal = signal.filtfilt(b, a, signal_data)


from scipy.optimize import minimize

# Define an objective function for optimization
def objective_function(x):
    return x[0]**2 + x[1]**2

# Minimize the objective function
initial_guess = [1, 1]
result = minimize(objective_function, initial_guess, method='Nelder-Mead')



from scipy import interpolate

# Create an interpolation function
x = np.arange(0, 10)
y = np.sin(x)
f = interpolate.interp1d(x, y, kind='cubic')

# Interpolate new points
x_new = np.arange(0, 9, 0.1)
y_new = f(x_new)


from scipy.stats import norm, poisson

# Generate random numbers from a normal distribution
mean = 0
std_dev = 1
random_numbers = norm.rvs(loc=mean, scale=std_dev, size=1000)

# Calculate the probability density function (PDF) of a poisson distribution
mu = 3
x = np.arange(0, 10)
pdf_values = poisson.pmf(x, mu)

from scipy.integrate import quad

# Define the function to integrate
def integrand(x):
    return x**2

# Perform definite integration
result, error = quad(integrand, 0, 1)

from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

# Generate a simple signal
t = np.linspace(0, 1, 1000, endpoint=False)
frequency = 10
signal_data = np.sin(2 * np.pi * frequency * t)

# Perform Fourier Transform
frequency_domain_signal = fft(signal_data)

# Inverse Fourier Transform
reconstructed_signal = ifft(frequency_domain_signal)

from scipy.sparse import csr_matrix

# Create a sparse matrix
data = np.array([1, 2, 3])
row_indices = np.array([0, 1, 2])
col_indices = np.array([1, 2, 0])
sparse_matrix = csr_matrix((data, (row_indices, col_indices)), shape=(3, 3))

# Perform matrix-vector multiplication
vector = np.array([1, 2, 3])
result = sparse_matrix.dot(vector)

from scipy import ndimage
import matplotlib.pyplot as plt

# Read and process an image
image = plt.imread('image.png')
blurred_image = ndimage.gaussian_filter(image, sigma=3)

from scipy import signal
import matplotlib.pyplot as plt

# Create a simple signal
t = np.linspace(0, 1, 1000, endpoint=False)
frequency = 5
signal_data = np.sin(2 * np.pi * frequency * t)

# Apply a low-pass filter to the signal
b, a = signal.butter(4, 0.2, 'low')
filtered_signal = signal.filtfilt(b, a, signal_data)

# Plot the original and filtered signals
plt.plot(t, signal_data, label='Original Signal')
plt.plot(t, filtered_signal, label='Filtered Signal')
plt.legend()
plt.show()

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the ODE system
def odes(t, y):
    dydt = [y[1], -y[0]]
    return dydt

# Solve the ODE system
sol = solve_ivp(odes, [0, 10], [1, 0], t_eval=np.linspace(0, 10, 100))

# Plot the solution
plt.plot(sol.t, sol.y[0])
plt.xlabel('Time')
plt.ylabel('Solution')
plt.show()

from scipy import signal
import matplotlib.pyplot as plt

# Generate a random signal
t = np.linspace(0, 1, 1000, endpoint=False)
signal_data = np.sin(2 * np.pi * 5 * t) + np.random.normal(size=1000)

# Perform spectral analysis using Welch's method
frequencies, power_spectrum = signal.welch(signal_data, fs=1000)

# Plot the power spectrum
plt.semilogy(frequencies, power_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density')
plt.show()

from scipy.optimize import linprog

# Define the objective function and constraints for linear programming
c = [-1, 4]  # Coefficients of the objective function
A = [[-3, 1], [1, 2]]  # Coefficients of the inequality constraints
b = [6, 4]  # Right-hand side of the inequality constraints

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b)




