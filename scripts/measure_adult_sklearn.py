import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler
import json
import h5py
import time

csv_handler = CSVHandler('sklearn_adult_with_json_hdf5.csv')


def sleep():
    time.sleep(30)

# I/O functions - READ
@measure_energy(handler=csv_handler)
def load_csv(path):
    return pd.read_csv(path)

@measure_energy(handler=csv_handler)
def save_csv(df, path):
    return df.to_csv(path, index=False)

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


@measure_energy(handler=csv_handler)
def preprocess_data(df):
    # Replace '?' with pd.NA
    df.replace(' ?', pd.NA, inplace=True)

    # Convert pd.NA to np.nan for compatibility with scikit-learn
    df.fillna(np.nan, inplace=True)

    # Separate numeric and non-numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns
    non_numeric_columns = df.select_dtypes(exclude=['number']).columns

    # Impute missing numeric columns with the mean
    if not df[numeric_columns].empty:
        imputer_numeric = SimpleImputer(strategy='mean')
        df[numeric_columns] = imputer_numeric.fit_transform(df[numeric_columns])

    # Impute missing non-numeric columns with the most frequent value
    if not df[non_numeric_columns].empty:
        imputer_non_numeric = SimpleImputer(strategy='most_frequent')
        df[non_numeric_columns] = imputer_non_numeric.fit_transform(df[non_numeric_columns])
    
    # Encode non-numeric columns to numeric values using Label Encoding
    label_encoders = {}
    for column in non_numeric_columns:
        label_encoders[column] = LabelEncoder()
        df[column] = label_encoders[column].fit_transform(df[column])
    
    return df

###--------------------------------------------###

# Other functions and main script logic remain the same

# Statistical Operations using Scikit-Learn
@measure_energy(handler=csv_handler)
def calculate_sum(df):
    return df.sum()

@measure_energy(handler=csv_handler)
def calculate_mean(df):
    return df.mean()

@measure_energy(handler=csv_handler)
def calculate_min(df):
    return df.min()

@measure_energy(handler=csv_handler)
def calculate_max(df):
    return df.max()

@measure_energy(handler=csv_handler)
def unique(df):
    return df.nunique()

###--------------------------------------------###

print("Starting Scikit-Learn Process...")
for i in range(10):
    # Input-output functions
    df = load_csv(path='../Datasets/adult.csv')
    sleep()
    save_csv(df, f'df_sklearn_adult_{i}.csv')
    sleep()

    # Load and save JSON
    df = load_json('../Datasets/adult.json')
    sleep()
    save_json(df, f'df_sklearn_adult_{i}.json')
    sleep()

    # Load and save HDF5
    df = load_hdf('../Datasets/adult.h5')
    sleep()
    save_hdf(df, f'df_sklearn_adult_{i}.h5', key='adult_data')
    sleep()

    # Preprocess data (replace missing values and encode labels)
    df = preprocess_data(df)
    sleep()

    # Statistical operations
    calculate_sum(df)
    sleep()
    calculate_mean(df)
    sleep()
    calculate_min(df)
    sleep()
    calculate_max(df)
    sleep()
    unique(df)
    sleep()

    print(f"Finished {i+1} iterations.")

csv_handler.save_data()
print("Scikit-Learn Process ended...")
