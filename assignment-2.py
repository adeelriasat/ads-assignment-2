# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 01:00:11 2023

@author: Adeel Warraich
"""

import numpy as np
import pandas as pd


def getDataFramesFromCsv(filePath, sRows=0):
    """ Method to return dataframes:
        This method will take filepath and sRows
        as params and will return 2 dataframes 
        one dataframe will as it is and the second 
        dataframe will be transpose of the first one
        filePath: Csv path
        sRows: number of rows to skip from start default is 0
    """
    # get first datafrom years as column
    df1 = pd.read_csv(filePath, skiprows=sRows)
    return df1,df2
    