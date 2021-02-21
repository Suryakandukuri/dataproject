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

### Running the Scrapers

for running Amazon Kindle Ebooks Last 90 days script and also there is ipython notebook (get_kindle_data.ipynb)

    python get_kindle_books.py


for running Flipkart Mobile phones data script, and also there is ipython notebook (get_flipkart_mobile_data.ipynb)

    python get_flipkart_data.py


for sales data analysis, you can look into salesdata_analysis.ipynb