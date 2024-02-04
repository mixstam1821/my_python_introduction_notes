# Numpy speeds up python computations, calling C, C++ and Fortran!!

import numpy as np
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)

arr = np.arange(1, 10, 2)  # Output: array([1, 3, 5, 7, 9])

zearr = np.zeros(5)  # Output: array([0., 0., 0., 0., 0.])

zeros_arr = np.zeros((2, 3))  # Output: array([[0., 0., 0.], [0., 0., 0.]])
ones_arr = np.ones((3, 2))  # Output: array([[1., 1.], [1., 1.], [1., 1.]])

arr = np.linspace(0, 10, 5)  # Output: array([ 0.,  2.5,  5.,  7.5, 10.])

arr = np.array([[1, 2, 3], [4, 5, 6]])

rand_arr = np.random.rand(3, 2)  # Output: array([[0.12345679, 0.98765432], [0.34567891, 0.56790123], [0.23456789, 0.87654321]])

randn_arr = np.random.randn(2, 4)  # Output: array([[-0.12457869,  0.98765432, -1.34567891,  0.56790123], [ 0.23456789, -0.87654321,  1.01234567, -2.12345679]])

arr = np.arange(8)
reshaped_arr = arr.reshape(2, 4)

arr = np.array([[1, 2], [3, 4]])
mean = np.mean(arr)  # Output: 2.5

arr = np.array([[1, 2], [3, 4]])
total_sum = np.sum(arr)  # Output: 10

arr = np.array([[1, 2], [3, 4]])
max_val = np.max(arr)  # Output: 4
min_val = np.min(arr)  # Output: 1

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
max_idx = np.argmax(arr)  # Output: 5
min_idx = np.argmin(arr)  # Output: 1

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(arr1, arr2)  # Output: array([[19, 22], [43, 50]])

arr = np.array([[1, 2], [3, 4]])
transposed_arr = np.transpose(arr)  # Output: array([[1, 3], [2, 4]])

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
vertical_stack = np.vstack((arr1, arr2))  # Output: array([[1, 2, 3], [4, 5, 6]])
horizontal_stack = np.hstack((arr1, arr2))  # Output: array([1, 2, 3, 4, 5, 6])

arr = np.array([1, 2, 3])
exp_arr = np.exp(arr)  # Output: array([ 2.71828183,  7.3890561 , 20.08553692])

arr = np.array([1, np.e, np.e**2])
log_arr = np.log(arr)  # Output: array([0., 1., 2.])




arr = np.array([[1, 2, 3], [4, 5, 6]])
mean = np.mean(arr)  # Output: 3.5
arr = np.array([[1, 2, 3], [4, 5, 6]])
median = np.median(arr)  # Output: 3.5
arr = np.array([[1, 2, 3], [4, 5, 6]])
std_dev = np.std(arr)  # Output: 1.707825127659933
arr = np.array([[1, 2, 3], [4, 5, 6]])
variance = np.var(arr)  # Output: 2.9166666666666665
arr = np.array([[1, 2, 3], [4, 5, 6]])
percentile_50 = np.percentile(arr, 50)  # Output: 3.5


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
correlation_matrix = np.corrcoef(arr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
covariance_matrix = np.cov(arr)

data = np.array([1, 2, 1])
hist, bin_edges = np.histogram(data, bins=[0, 1, 2, 3])

arr = np.array([[1, np.nan, 3], [4, 5, 6]])
mean = np.nanmean(arr)  # Output: 3.8


arr = np.array([[1, np.nan, 3], [4, 5, 6]])
std_dev = np.nanstd(arr)  # Output: 1.7204650534085253


arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2  # Broadcasting the smaller array arr2 to match the shape of arr1
# Output: array([[11, 22, 33],
#                [14, 25, 36]])

random_int = np.random.randint(1, 10)  # Generate a random integer between 1 and 10
random_normal = np.random.normal(0, 1, size=(3, 3))  # Generate random samples from a normal distribution



matrix = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(matrix)  # Compute the inverse of the matrix
eigenvalues, eigenvectors = np.linalg.eig(matrix)  # Compute the eigenvalues and eigenvectors of the matrix


signal = np.array([1, 2, 3, 4])
fft_result = np.fft.fft(signal)  # Compute the discrete Fourier transform of the signal


data = np.ma.masked_array([1, 2, 3, -1, 5], mask=[0, 0, 0, 1, 0])  # Create a masked array with a masked value
mean = np.mean(data)  # Compute the mean, ignoring the masked value

arr = np.array([1, 2, 3, 4])
result = np.exp(arr)  # Element-wise exponentiation without explicit looping
# Output: array([ 2.71828183,  7.3890561 , 20.08553692, 54.59815003])

import numpy as np

# Read data from a CSV file into a NumPy array
data = np.genfromtxt('data.csv', delimiter=',')


import numpy as np

# Read data from a text file into a NumPy array
data = np.loadtxt('data.txt')

