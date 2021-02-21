import kaggle
import pandas
import requests
import datadotworld as dw


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
    1. user input of dataframe key from the dictionary enter  ex: 'stats'
    """
    path = input("Enter path of the dataset: ")
    dataset = dw_load_data(path)
    df_key = input("Enter dataframe key: ")
    dataframe = dataset.dataframes[df_key]
    print("Dataframe Sample:")
    print(dataframe.head(3))
    return dataframe

dw_df = get_dw_dataframe()

