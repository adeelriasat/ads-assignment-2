# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 01:00:11 2023

@author: Adeel Warraich
"""

import numpy as np
import pandas as pd
import stats   # homemade stats routines
import matplotlib.pyplot as plt


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

def exploreStatProperties(df):
    """
    Parameters
    ----------
    df : pandas dataframe.

    Returns:
    None
    Show.
    different statistical properties of a dataframe
    """
    # show basic stats
    print('Basis Stats of Distribution')
    basic_stats = df.describe()
    print(basic_stats)

def showSkewnessAndKurtosis(df):
    """

    Parameters
    ----------
    df : pandas dataframe.

    this method will take panda series and show skewness and kurtosis
    """
    # show skewness and kurotosis
    print('<--Skewness of Distribution-->')
    print(stats.skew(df))
    print('<--Kurtosis of Distribution-->')
    print(stats.kurtosis(df))
    
    
# get two dataframe from method one with country as column and one with year as column
df_elecFromOilYear, df_elecFromOilCountry = getDataFramesFromCsv(
    '../from oil/API_EG.ELC.PETR.ZS_DS2_en_csv_v2_5362831.csv', sRows=4, nonNumericalRows=4)
print(df_elecFromOilCountry.index)
# explore the statistical properties
exploreStatProperties(df_elecFromOilYear)
showSkewnessAndKurtosis(df_elecFromOilYear['2010'])
showSkewnessAndKurtosis(df_elecFromOilYear['2015'])

# calculate mean, median , and max of united kingdom elec production from oil
# using aggregate function
print('<--Mean, Median, Max, Min Electricty Production From Oil of UK from 1960 to 2015-->')
print(df_elecFromOilCountry['United Kingdom'].aggregate(['mean', 'median', 'max', 'min']))


# sort values by production of elec in asc order for australia column
sortedByAustraliaAsc = df_elecFromOilCountry.sort_values(by=['Australia'])

# now in descending order for united kingdom
sortedByUkDesc = df_elecFromOilCountry.sort_values(by=['United Kingdom'], ascending=False)

# plot the bar graph to check the production of electricty from oil and production of elec from coal

# get electricty production from coal data
df_elecFromCoalYear, df_elecFromCoalCountry = getDataFramesFromCsv(
    '../from coal/API_EG.ELC.COAL.ZS_DS2_en_csv_v2_5362822.csv', sRows=4, nonNumericalRows=4) 

# get electricty production from renewable sources data
df_elecFromRenewableYear, df_elecFromRewewableCountry = getDataFramesFromCsv(
    '../from renewable/API_EG.ELC.RNWX.KH_DS2_en_csv_v2_5358682.csv', sRows=4, nonNumericalRows=4) 

# df_elecFromCoalYear.to_csv('../coalyear.csv')
# df_elecFromCoalCountry.to_csv('../coalcountry.csv')

# convert to int to avoid cluttering
df_elecFromOilCountry.index = df_elecFromOilCountry.index.astype(int)
df_elecFromCoalCountry.index = df_elecFromCoalCountry.index.astype(int)
df_elecFromRewewableCountry.index = df_elecFromRewewableCountry.index.astype(int)

# plot the line graph from 1960 to 2015
plt.figure(figsize=(8,6))
plt.plot(df_elecFromOilCountry.index, df_elecFromOilCountry["United Kingdom"], label="UK (From Oil)")
plt.plot(df_elecFromCoalCountry.index, df_elecFromCoalCountry["United Kingdom"], label="From (From Coal)")

plt.plot(df_elecFromOilCountry.index, df_elecFromOilCountry["Australia"], label="AUS (From Oil)")
plt.plot(df_elecFromCoalCountry.index, df_elecFromCoalCountry["Australia"], label="AUS (From Coal)")

plt.xlabel("Year")
plt.ylabel("Electricity Production (% of total)")
plt.legend()
plt.show()

# plot the bar graph



# pearsons_corr = cities.corr()
# kendall_corr = cities.corr(method='kendall')
# print('correlation')
# print('pearsons Correlation')
# print(pearsons_corr)
# print(kendall_corr)
