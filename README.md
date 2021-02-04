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

## Running the Dashboards

Execute the following commands to run the dashboard:

    streamlit run projects/<app_name>/main.py

You can now view the dashboard in your browser: http://localhost:8501

**Note: ** The port might change from 8501 to a different one if 8501 is already in use.

## Running using Docker Compose

You can also run the dashboard using docker-compose by running the following command:

    docker-compose up

You can now view the dashboard in your browser: http://localhost:8501

**Note: ** The port 8501 should be available to run the app using docker-compose.