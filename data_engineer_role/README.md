## Setting Up Environment

It is recommended to create a virtual environment to setup the project.

Tools like [virtualenv](https://virtualenv.pypa.io/en/latest/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) provide isolated Python environments, which are cleaner than installing packages systemwide (as they prevent dependency conflicts). They also let you install packages without root privileges.

### For Ubuntu or Mac
Create a new virtual environment by choosing a Python interpreter and making a  `./venv`  directory to hold it:

    $ python3 -m venv  ./venv

Activate the virtual environment:

    $ source ./venv/bin/activate

### For Windows
Set up is not tested for Windows. Need to test and update the steps here appropriately.

### Install dependencies
Install the packages using the following command:

    pip install -r requirements.txt

### Access of datasets from kaggle and data.world

1. kaggle

Add ~/.kaggle/kaggle.json with credentials from kaggle account to access the dataset

2. data.world

    Configuration
This library requires a data.world API authentication token to work.

Your authentication token can be obtained on data.world once you enable Python under Integrations > Python

To configure the library, run the following command:

    dw configure

Alternatively, tokens can be provided via the DW_AUTH_TOKEN environment variable. On MacOS or Unix machines, run (replacing <YOUR_TOKEN>> below with the token obtained earlier):

    export DW_AUTH_TOKEN=<YOUR_TOKEN>

### get_data.py

Purpose of the script is to access the datasets from kaggle and data.world (datadotworld package) using functions that will ask for user inputs to find and download the required datasets from there.

for data.world datasets, script will ask user to input the username/dataset_name of the dataset on data.world and further selecting the dataframe among the list of datasets.

for kaggle datasets, script will download the dataset as zip file, and extract one file that user needs to a specific output folder (folder has to be already present)

### create_dataset.py

Using pandas to merge the two datasets one from World Health Organisation (WHO) and the other on Covid 19 Country wise data. I have used inner join to merge the two datasets.

#### Column created total_healthcare_personell
Calculated the total healthcare personnel by add these columns, "number_of_community_and_traditional_health_workers","number_of_laboratory_health_workers" , "number_of_nursing_and_midwifery_personnel", "number_of_physicians", "number_of_other_health_service_providers"

Thought process is to see how health care personnel has impacted the control and spread of covid19

### script_ex2.py

Basic functional script with class defined for getting information on the dataframes. Usage of Decorators and without decorators

Using a decorator made it possible to call the functions in the class by using self, without calling each funciton
Where as without using the decorator, we called each of the functions to get the same response as in the above case.
Both of them, have their own purposes.