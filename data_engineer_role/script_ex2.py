# importing library
import pandas as pd
# Reading the data
df_covid19 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv")

# sample data
print(df_covid19.head(3))


class ClsDFInfo:
    '''
    Class defined with functions to get an over view of the dataset.
    Contains functions to
    1. get the list of columns; get_df_cols
    2. get the number of columns; get_df_len
    3. get the data types of columns; get_df_types
    '''
    def __init__(self, f):
        self.f = f    
        
    def __call__(self):
        """
        When used with decorator, prints the corresponding 
        text to the function
        """
        print("Decorating", self.f.__name__, "\n")        
        self.f(self.get_df_cols,"cols in df:")        
        self.f(self.get_df_len, "len of df:")
        self.f(self.get_df_types, "datatypes of df")  
        

    def get_df_cols(self, df):
        """
        Function to return the list of columns in the dataframe
        """        
        return df.columns

    def get_df_len(self, df):
        """
        Function to return the Number of columns in the dataframe
        """      
        return len(df.columns)

    def get_df_types(self, df):
        """
        Function to get the column data types using pandas dtypes function
        """
        return df.dtypes

   
# Using the decorator to modify the output from the functions
@ClsDFInfo
def df_info(func, desc):
    z = func(df_covid19)
    print(desc, "----------\n", z, "\n\n")

# initiating function to be called without decorator 
def df_info_wod(func, desc):
    z = func(df_covid19)
   
  
df_info()

# WITHOUT DECORATOR

print("------------------# WITHOUT DECORATOR ----------------")

# Initiating a function under the class defined to call the functions defined in the Class
func = ClsDFInfo(df_info_wod)

# calling the get_df_cols function
z = func.get_df_cols(df_covid19)
print(z, "\n\n")
# calling the get_df_len function
z2 = func.get_df_len(df_covid19)
print(z2, "\n\n")
# calling the get_df_types function
z3 = func.get_df_types(df_covid19)
print(z3, "\n\n")

# Using a decorator made it possible to call the functions in the class by using self, without calling each funciton
# Where as without using the decorator, we called each of the functions to get the same response as in the above case.
# Both of them, have their own purposes.
#