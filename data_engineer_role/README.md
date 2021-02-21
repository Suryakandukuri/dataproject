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