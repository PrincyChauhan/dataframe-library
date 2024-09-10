## Instructions:

1. Download the datasets in `CSV` and `JSON` formats from the [link](https://drive.google.com/drive/folders/13xHh2bvxF8X9cho1fVohIbu4lrpdvVlz?usp=sharing) and place them in the `datasets` folder.

2. IMPORTANT: Please generate the required hdf5 files by navigating to the `datasets` folder and running the file `generate_hdfs.py`

3. To run energy measurement for a library for a particular dataset, nagvigate to scripts folder and use the command

    `sudo python3 measure_<dataset_name>_<library_name>.py`

    Ex: To measure energy consumption of Dask on Adult dataset, use
    `sudo python3 measure_adult_dask.py`



## Additional Information:

 - Results folder contains results of our experiments
 - Summary folder contains mean, median and standard deviations of pkg, dram and time duration for all libraries for a particular dataset
