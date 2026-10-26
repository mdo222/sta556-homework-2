#This is the Python script for cleaning and processing my dataset
import numpy as np
import pandas as pd

#First function: Fill in 0's in with NA values
def fill_na(
        data: pd.DataFrame,
        column_name: str,
        value = 0
) -> pd.DataFrame:
    
    """ Return a copy of the pandas data frame where the specified column is filled in with NA
    values instead of the original value the function was supplied with
    """
    #Check to make the datatype in that column is float
    data[column_name] = data[column_name].astype(float)

    #Replace the specified value in the function with an NA value using np.nan
    data[column_name] = data[column_name].replace(value,np.nan)

    #Return the data set
    return data.copy()

# Second Function: Filter out rows with NA values
def get_non_na_rows(
        data: pd.DataFrame,
        column_names= list) -> pd.DataFrame:
    
    """ Return the a copy of the pandas data frame
    with rows that do not have NA values in them"""

    return data.dropna(subset = column_names).copy()


#Third Function get the columns needed for analysis
def get_columns (
        data:pd.DataFrame,
        column_names: list
) -> pd.DataFrame:
    
    """ Return a copy of the pandas data frame that has the columns specifies in the list
    that is used as an argument in the function
    """

    return data.loc[:,column_names].copy()