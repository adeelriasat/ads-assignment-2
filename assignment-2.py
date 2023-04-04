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
    
    # get first datafrom years as index column
    df1.index = df1.iloc[:, 0]

    # remove non numerical data from df
    df1 = df1.iloc[:, nonNumericalRows:]
    
    # clean the dataframe first remove all columns which are empty 
    # then all rows which are empty and then those with missing entries
    df1 = df1.dropna(axis=1, how='all').dropna(how='all').dropna()

    # get second dataframe countries as column
    # for this purpose transpose the dataframe
    df_transposed = csv_data.transpose()

    # set first row as columns of transpose df
    df_transposed.columns = df_transposed.iloc[0]

    # remove non numerical data from dataframe
    df_transposed = df_transposed.iloc[nonNumericalRows:]
    
    # rename the index column
    df_transposed.index.name = 'Year'
    
    # clean the transposed dataframe those are completely empty and then drop column with missing entries
    df_transposed = df_transposed.dropna(how='all').dropna(axis=1)    
    
    # make year as integer for the graph to avoid cluttering
    df_transposed.index = pd.to_numeric(df_transposed.index)

    return df1, df_transposed


df_yearsAsColumn, df_countryAsColumn = getDataFramesFromCsv(
    '../from oil/API_EG.ELC.PETR.ZS_DS2_en_csv_v2_5362831.csv', sRows=4, nonNumericalRows=4)
df_countryAsColumn.to_csv('../test1.csv')
df_yearsAsColumn.to_csv('../test.csv')
print(df_countryAsColumn)
