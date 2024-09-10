import pandas as pd
import dask.dataframe as dd
import vaex as ve

adult = pd.read_csv('adult.csv')
adult_vaex = ve.read_csv('adult.csv')
adult_dask = dd.read_csv('adult.csv')

drugs = pd.read_csv('drugs.csv')
drugs_vaex = ve.read_csv('drugs.csv')
drugs_dask = dd.read_csv('drugs.csv')

# USCensus1990 = pd.read_csv('USCensus1990.csv')
# USCensus1990_vaex = ve.read_csv('USCensus1990.csv')
# USCensus1990_dask = dd.read_csv('USCensus1990.csv')

def save_hdf_pandas(df, path, key):
    return df.to_hdf(path, key=key)

def save_hdf_dask(df, path, key):
    return df.to_hdf(path, key=key)

def save_hdf_vaex(df, path, key='a'):
    return df.export(path)

save_hdf_pandas(adult, 'adult.h5', 'a')
save_hdf_pandas(drugs, 'drugs.h5', 'a')
# save_hdf_pandas(USCensus1990, 'USCensus1990.h5', 'a')

save_hdf_vaex(adult_vaex, 'adult_v.hdf5', 'a')
save_hdf_vaex(drugs_vaex, 'drugs_vaex.hdf5', 'a')
# save_hdf_vaex(USCensus1990_vaex, 'USCensus1990_v.hdf5', 'a')

save_hdf_dask(adult_dask, 'adult_dask.h5', 'a')
save_hdf_dask(drugs_dask, 'drugs_dask.h5', 'a')
# save_hdf_dask(USCensus1990_dask, 'USCensus1990_dask.h5', '/data')

print("Testing")

def load_hdf_dask(path, key):
    return pd.read_hdf(path, key=key)

def load_hdf_pandas(path):
    return pd.read_hdf(path)

def load_hdf_vaex(path):
    return ve.open(path)

load_hdf_dask(path='adult_dask.h5', key='a')
load_hdf_pandas(path='adult.h5')
load_hdf_vaex(path='adult_v.hdf5')
# load_hdf_dask(path='USCensus1990_dask.h5', key='/data')
# load_hdf_pandas(path='USCensus1990.h5')
# load_hdf_vaex(path='USCensus1990_v.hdf5')
load_hdf_dask(path='drugs_dask.h5', key='a')
load_hdf_pandas(path='drugs.h5')
load_hdf_vaex(path='drugs_vaex.hdf5')

print("Success")


