# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:48:38 2016

@author: Steffany
"""

import pandas as pd
import numpy as np

xlx = pd.ExcelFile('quikflix.xlsx')

df1 = xlx.parse(1)
#df_nump = df1.as_matrix()
cities = df1.set_index("Index")
#pop = df1.loc[: , "Population"]
city_pop = cities.loc[: , "Population"]


df2 = xlx.parse(2)
dist_np = df2.as_matrix()
distances = df2.set_index("Cities")
del df1
del df2

dist_np = np.delete(dist_np, 0, 1)
#nyc = distances[distances[1] <= 150]
#nyc = nyc[nyc[1] > 1]
#nyc = nyc.loc[:, 1]
#dist_cov = 0

sub_150 = np.where(dist_np <= 150)
sub_150 = np.where(sub_150 > 0)
zip_150 = np.asarray(sub_150).T
print(zip_150)