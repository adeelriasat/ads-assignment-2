# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 01:00:11 2023

@author: Adeel Warraich
"""

import numpy as np
import pandas as pd


def getDataFramesFromCsv(filePath, sRows=0, nonNumericalRows=0):
    """ Method to return dataframes:
        This method will take filepath ,sRows and nonNumericalRows
        as params and will return 2 dataframes 
        one dataframe with years as column and the second 
        dataframe with countries as column  of the first one
        filePath: Csv path
        sRows: number of rows to skip from start default is 0
        nonNumericalRows: number of non numerical data rows to clean default is 0
    """
    # read the csv file
    csv_data = pd.read_csv(filePath, skiprows=sRows)
    df1 = csv_data
    
    # get first datafrom years as column
    df1.index = df1.iloc[:, 0]

    # remove non numerical data from df
    df1 = df1.iloc[:, nonNumericalRows:]
    
    # get second dataframe countries as column
    # for this purpose transpose the dataframe
    df_transposed = csv_data.transpose()

    # set first row as columns of transpose df
    df_transposed.columns = df_transposed.iloc[0]

    # remove non numerical data from dataframe
    df_transposed = df_transposed.iloc[nonNumericalRows:]
    
    # rename the index column
    df_transposed.index.name = 'year'
    
    return df1, df_transposed


df_yearsAsColumn, df_countryAsColumn = getDataFramesFromCsv(
    '../API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_5359189/API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_5359189.csv', sRows=4, nonNumericalRows=4)
df_countryAsColumn.to_csv('../test1.csv')
print(df_countryAsColumn)
