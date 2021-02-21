import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import pandas
import requests
import datadotworld as dw
from pathlib import Path

# Functions specific to access data.world datasets using their APIs
def dw_load_data(path):
    """
    Function to load the datasets from the data.world using their 
    Python connector REST API
    1. takes input from user for the dataset path username/dataset_name
    2. returns LocalDataset object which holds data
    """
    dataset = dw.load_dataset(path, auto_update=True)
    df_dict = dataset.dataframes
    print("**Dictionary of the dataframes present**")
    print(df_dict)
    return dataset

def get_dw_dataframe():
    """
    Function to get the one dataframe from the dataframes present 
    in LocalDataset object
    1. user input for path of the dataset on data.world 'username/dataset_name'
    2. user input of dataframe key from the dictionary enter  ex: 'stats'

    Returns dataframe user selects
    """
    path = input("Enter path of the data.world dataset: ")
    dataset = dw_load_data(path)
    df_key = input("Enter dataframe key: ")
    dataframe = dataset.dataframes[df_key]
    print("Dataframe Sample:")
    print(dataframe.head(3))
    return dataframe

# Functions specific to access KAGGLE datasets using their APIs

def download_kaggle_dataset(kaggle_path, folder_name):
    """
    Pre-requisite: ~/.kaggle/kaggle.json should be present with user credentials from kaggle
    Function to download dataset from kaggle using KaggleApi
    1. Initiates and Authenticates the API
    2. Downloads the datasets as a ZIP file
    Inputs: kaggle_path: "username/dataset_name" from kaggle
    folder_name: folder name you want to create in your local
    Returns the zip file location for extracting the data
    """
    kaggle_api = KaggleApi()
    # authentication
    kaggle_api.authenticate()
    # download the datasets
    kaggle_api.dataset_download_files(kaggle_path, folder_name)
    zipfile_name = kaggle_path.split("/")[1] + ".zip"
    # zip file location
    zipfile_loc = folder_name+ "/" +zipfile_name
    if Path(zipfile_loc).is_file():
        print("Dataset as ZIP file is downloaded")
    else:
        print("Data Not Downloaded")
    return zipfile_loc

def extract_kaggle_data(zipfile_loc,output_path):
    """
    Function to extract one single file from the kaggle dataset
    downloaded as a zipfile.
    Inputs: zip file location, file name, output path
    Output: Extract necessary dataset/file to output path
    """
    zf = ZipFile(zipfile_loc)
    print("List of folders and files present in this Zip file:")
    print(zf.namelist())
    file_name = input("Enter the file you want to extract: ")
    file_path = output_path + "/" + file_name
    zf.extract(file_name, output_path)
    zf.close()
    if Path(file_path).is_file():
        print("Dataset is extracted")
    else:
         print("Data Not extracted")
    pass

def kaggle_dataset():
    '''
    Function to combine downlaod and extract functions written after asking 
    user inputs on kaggle path, folder name to be created in local while download
    output folder after extraction of the file
    '''
    kaggle_path = input("Enter the kaggle dataset path: ")
    folder_name = input("Enter the folder name to be created: ")
    output_path = input("Enter the output folder path: ")
    zipfile_loc = download_kaggle_dataset(kaggle_path, folder_name)
    extract_kaggle_data(zipfile_loc, output_path)
    print("Kaggle Datasets are downlaoded and extracted")
    pass

def main():
    # Assigning the data.world dataframe to dw_df variable
    dw_df = get_dw_dataframe()
    # write the dataframe to folder "data"
    dw_df.to_csv("data/who_dataset.csv", index = False)
    kaggle_dataset()

if __name__ == '__main__':
   main()