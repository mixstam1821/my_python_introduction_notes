# Xarray makes our life much more easier! it is ideal if you work with NetCDF files.
import xarray as xr
import numpy as np
import pandas as pd
# Create a 1D DataArray with labeled coordinates
data = np.random.rand(5)
time = pd.date_range('2023-01-01', periods=5)
da = xr.DataArray(data, coords={'time': time}, dims=['time'])

# Open a NetCDF file as a Dataset
ds = xr.open_dataset('path/to/file.nc')

# Access and manipulate variables in the dataset
temperature = ds['temperature']
temperature_anomaly = temperature - temperature.mean(dim='time')

# Resample a time series to a lower frequency
monthly_data = da.resample(time='1M').mean()

# Aggregate data over a specific dimension
monthly_average = ds.mean(dim='time')

# Interpolate missing values in a 1D DataArray
filled_data = da.interpolate_na(dim='time')

# Extrapolate data beyond the existing coordinates
extended_data = da.interp(time=pd.date_range('2023-01-01', periods=10))

# Group data by a specific coordinate and calculate the mean within each group
grouped_mean = ds.groupby('month').mean(dim='time')

# Plot the data using xarray's built-in plotting capabilities
ds['temperature'].plot()

# Merge multiple datasets along a common dimension
combined_ds = xr.merge([ds1, ds2])

# Concatenate datasets along a new dimension
concatenated_ds = xr.concat([ds1, ds2], dim='new_dim')

# Select data based on specific coordinates or indices
selected_data = ds.sel(time='2023-01-01')

# Slice data based on coordinate ranges
sliced_data = ds.sel(time=slice('2023-01-01', '2023-01-10'))

# Apply a custom function to the dataset
def custom_function(x):
    return x ** 2

result = xr.apply_ufunc(custom_function, ds)

# Apply a custom function along a specific dimension
result = ds.reduce(custom_function, dim='time')

# Save the dataset to a NetCDF file
ds.to_netcdf('output_file.nc')

# Read and work with geospatial data using xarray and rasterio
import rasterio
import xarray as xr

with rasterio.open("path/to/raster.tif") as src:
    data = src.read()
    spatial_coords = {'x': src.coords['x'], 'y': src.coords['y']}
    da = xr.DataArray(data, coords=spatial_coords, dims=['y', 'x'])


