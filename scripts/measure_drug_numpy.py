# from pyJoules.energy_meter import measure_energy
# from pyJoules.handler.csv_handler import CSVHandler
# import time
# import numpy as np
# import pandas as pd  # Import pandas for JSON and HDF5 operations
# import chardet

# # Initialize CSVHandler for energy measurement logging
# csv_handler = CSVHandler('numpy_drug.csv')

# def sleep():
#     time.sleep(30)

# def detect_encoding(path):
#     with open(path, 'rb') as f:
#         result = chardet.detect(f.read())
#     return result['encoding']

# @measure_energy(handler=csv_handler)
# def load_csv_with_numpy(path):
#     try:
#         encoding = detect_encoding(path)  # Detect encoding
#         data = np.genfromtxt(path, delimiter=',', skip_header=1, filling_values=np.nan, encoding=encoding)
#         print(f"Loaded data with shape: {data.shape}")
#         return data
#     except Exception as e:
#         print(f"Error loading file: {e}")
#         return None

# @measure_energy(handler=csv_handler)
# def save_csv_with_numpy(data, path):
#     try:
#         np.savetxt(path, data, delimiter=',', fmt='%s')  # Save as CSV using NumPy
#         print(f"Saved data to {path}")
#     except Exception as e:
#         print(f"Error saving file: {e}")

# @measure_energy(handler=csv_handler)
# def replace_nan(data, value=0):
#     # Replace NaN values with the specified value
#     return np.nan_to_num(data, nan=value)

# # @measure_energy(handler=csv_handler)
# # def calculate_sum(data):
# #     return np.nansum(data)

# # @measure_energy(handler=csv_handler)
# # def calculate_mean(data):
# #     return np.nanmean(data)

# # @measure_energy(handler=csv_handler)
# # def calculate_min(data):
# #     return np.nanmin(data)

# # @measure_energy(handler=csv_handler)
# # def calculate_max(data):
# #     return np.nanmax(data)

# def load_json(path):
#     try:
#         return pd.read_json(path)
#     except Exception as e:
#         print(f"Error loading JSON file: {e}")
#         return None

# def save_json(df, path):
#     try:
#         df.to_json(path, orient='records')
#         print(f"Saved JSON to {path}")
#     except Exception as e:
#         print(f"Error saving JSON file: {e}")

# def load_hdf(path):
#     try:
#         return pd.read_hdf(path, key='_data')
#     except Exception as e:
#         print(f"Error loading HDF5 file: {e}")
#         return None

# def save_hdf(df, path, key='_data'):
#     try:
#         df.to_hdf(path, key=key)
#         print(f"Saved HDF5 to {path}")
#     except Exception as e:
#         print(f"Error saving HDF5 file: {e}")

# print("Starting NumPy Process...")
# for i in range(10):
#     # Input-output functions
#     data = load_csv_with_numpy(path='../Datasets/drugs.csv')
#     if data is not None:
#         sleep()
#         save_csv_with_numpy(data, f'df_numpy_drugs_{i}.csv')
#         sleep()

#         # Load and save JSON
#         df = load_json('../Datasets/drugs.json')
#         if df is not None:
#             sleep()
#             save_json(df, f'df_numpy_drugs_{i}.json')
#             sleep()

#         # Load and save HDF5
#         df = load_hdf('../Datasets/drugs.h5')
#         if df is not None:
#             sleep()
#             save_hdf(df, f'df_numpy_drugs_{i}.h5', key='_data')
#             sleep()
    
#         # Handling missing data
#         # data = replace_nan(data)
#         # sleep()

#         # # Statistical operations
#         # print(f"Sum: {calculate_sum(data)}")
#         # sleep()
#         # print(f"Mean: {calculate_mean(data)}")
#         # sleep()
#         # print(f"Min: {calculate_min(data)}")
#         # sleep()
#         # print(f"Max: {calculate_max(data)}")
#         # sleep()

#         print(f"Finished {i+1} iterations.")

# csv_handler.save_data()
# print("NumPy Process ended...")

from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import time
import numpy as np
import pandas as pd  # Import pandas for JSON and HDF5 operations
import chardet

# Initialize CSVHandler for energy measurement logging
csv_handler = CSVHandler('numpy_drug.csv')

def sleep():
    time.sleep(30)

def detect_encoding(path):
    with open(path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

@measure_energy(handler=csv_handler)
def load_csv_with_numpy(path):
    try:
        encoding = detect_encoding(path)  # Detect encoding
        # Load data with variable length rows
        data = np.genfromtxt(path, delimiter=',', skip_header=1, filling_values=np.nan, dtype=str, encoding=encoding)
        
        # Filter rows that have exactly 8 columns
        filtered_data = np.array([row for row in data if len(row) == 8])
        
        print(f"Loaded filtered data with shape: {filtered_data.shape}")
        return filtered_data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

@measure_energy(handler=csv_handler)
def save_csv_with_numpy(data, path):
    try:
        np.savetxt(path, data, delimiter=',', fmt='%s')  # Save as CSV using NumPy
        print(f"Saved data to {path}")
    except Exception as e:
        print(f"Error saving file: {e}")

@measure_energy(handler=csv_handler)
def replace_nan(data, value=0):
    # Replace NaN values with the specified value
    return np.nan_to_num(data, nan=value)

def load_json(path):
    try:
        return pd.read_json(path)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None

def save_json(df, path):
    try:
        df.to_json(path, orient='records')
        print(f"Saved JSON to {path}")
    except Exception as e:
        print(f"Error saving JSON file: {e}")

def load_hdf(path):
    try:
        return pd.read_hdf(path, key='_data')
    except Exception as e:
        print(f"Error loading HDF5 file: {e}")
        return None

def save_hdf(df, path, key='_data'):
    try:
        df.to_hdf(path, key=key)
        print(f"Saved HDF5 to {path}")
    except Exception as e:
        print(f"Error saving HDF5 file: {e}")

print("Starting NumPy Process...")
for i in range(10):
    # Input-output functions
    data = load_csv_with_numpy(path='../Datasets/drugs.csv')
    if data is not None:
        sleep()
        save_csv_with_numpy(data, f'df_numpy_drugs_{i}.csv')
        sleep()

        # Load and save JSON
        df = load_json('../Datasets/drugs.json')
        if df is not None:
            sleep()
            save_json(df, f'df_numpy_drugs_{i}.json')
            sleep()

        # Load and save HDF5
        df = load_hdf('../Datasets/drugs.h5')
        if df is not None:
            sleep()
            save_hdf(df, f'df_numpy_drugs_{i}.h5', key='_data')
            sleep()
    
        print(f"Finished {i+1} iterations.")

csv_handler.save_data()
print("NumPy Process ended...")
