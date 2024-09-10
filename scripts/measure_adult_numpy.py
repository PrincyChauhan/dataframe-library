from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import time
import numpy as np
import pandas as pd  # Import pandas for JSON and HDF5 operations

# Initialize CSVHandler for energy measurement logging
csv_handler = CSVHandler('numpy_adult.csv')

def sleep():
    time.sleep(30)

@measure_energy(handler=csv_handler)
def load_csv(path):
    return np.genfromtxt(path, delimiter=',', dtype=None, encoding='utf-8')

@measure_energy(handler=csv_handler)
def save_csv(array, path):
    # Convert the array to a string format to ensure all data types are handled correctly
    np.savetxt(path, array, delimiter=',', fmt='%s')

@measure_energy(handler=csv_handler)
def load_json(path):
    return pd.read_json(path)

@measure_energy(handler=csv_handler)
def save_json(df, path):
    return df.to_json(path, orient='records')

@measure_energy(handler=csv_handler)
def load_hdf(path):
    return pd.read_hdf(path)

@measure_energy(handler=csv_handler)
def save_hdf(df, path, key):
    return df.to_hdf(path, key=key, mode='w')

###------------------------------------------###

# Handling missing data 
@measure_energy(handler=csv_handler)
def replace_nan(array, value=0):
    # Loop through each column and check if it's numeric
    for i in range(array.shape[1]):
        try:
            # Convert the column to float (if possible) and apply np.isnan()
            array[:, i] = np.where(np.isnan(array[:, i].astype(float)), value, array[:, i])
        except ValueError:
            # If conversion to float fails, skip the column
            continue
    return array

###------------------------------------------###

# Statistical Operations using NumPy

@measure_energy(handler=csv_handler)
def calculate_sum(array):
    # Filter numeric data by checking if elements can be converted to float
    numeric_data = np.array([array[:, i].astype(float) for i in range(array.shape[1]) if np.issubdtype(array[:, i].dtype, np.number)]).T
    if numeric_data.size == 0:
        return "No numeric data"
    return np.sum(numeric_data)

@measure_energy(handler=csv_handler)
def calculate_mean(array):
    numeric_data = np.array([array[:, i].astype(float) for i in range(array.shape[1]) if np.issubdtype(array[:, i].dtype, np.number)]).T
    if numeric_data.size == 0:
        return "No numeric data"
    return np.mean(numeric_data)

@measure_energy(handler=csv_handler)
def calculate_min(array):
    numeric_data = np.array([array[:, i].astype(float) for i in range(array.shape[1]) if np.issubdtype(array[:, i].dtype, np.number)]).T
    if numeric_data.size == 0:
        return "No numeric data"
    return np.min(numeric_data)

@measure_energy(handler=csv_handler)
def calculate_max(array):
    numeric_data = np.array([array[:, i].astype(float) for i in range(array.shape[1]) if np.issubdtype(array[:, i].dtype, np.number)]).T
    if numeric_data.size == 0:
        return "No numeric data"
    return np.max(numeric_data)

print("Starting NumPy Process...")
for i in range(10):
    # Input-output functions
    array = load_csv(path='../Datasets/adult.csv')
    sleep()
    save_csv(array, f'df_numpy_adult_{i}.csv')
    sleep()

    # Load and save JSON
    df = load_json('../Datasets/adult.json')
    sleep()
    save_json(df, f'df_numpy_adult_{i}.json')
    sleep()

    # Load and save HDF5
    df = load_hdf('../Datasets/adult.h5')
    sleep()
    save_hdf(df, f'df_numpy_adult_{i}.h5', key='adult_data')
    sleep()
    
    # Handling missing data
    array = replace_nan(array)
    sleep()

    # Statistical operations
    print(f"Sum: {calculate_sum(array)}")
    sleep()
    print(f"Mean: {calculate_mean(array)}")
    sleep()
    print(f"Min: {calculate_min(array)}")
    sleep()
    print(f"Max: {calculate_max(array)}")
    sleep()

    print(f"Finished {i+1} iterations.")

csv_handler.save_data()
print("NumPy Process ended...")
