# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:52:13 2016

@author: Steffany
"""

import numpy as np
            
#array of demands per region
demand  = np.array( [ [1866240, 1166400, 933120, 1283040, 2041200, 1020600] ] )

#matrix of transpertation costs from facility locations to regions
tc = np.array( [ [0.50, 0.63, 0.88, 1.00, 1.25, 1.38],
                 [0.63, 0.63, 0.63, 0.75, 1.00, 1.13], 
                 [0.75, 0.75, 0.63, 0.63, 0.75, 0.88], 
                 [1.00, 1.00, 0.75, 0.63, 0.75, 0.63], 
                 [1.13, 1.25, 0.75, 0.88, 0.63, 1.00] ] )
av_tc = tc.mean(axis=1) #average cost of transportation from a location
del tc

sfc = np.array( [ [775000, 725000, 695000, 695000, 715000] ] )
new_sfc = sfc/2000000 #cost per book of storage in a small facility in a given city
del sfc

lfc = np.array( [ [975000, 895000, 850000, 850000, 875000] ] )
new_lfc = lfc/4000000 #cost per book of storage in a large facility in a given city
del lfc

small_facilities = ['Seattle Small', 
              'Denver Small', 
              'St.Louis Small', 
              'Atlanta Small', 
              'Philadelphia Small'] 
             
large_facilities = ['Seattle Large', 
              'Denver Large', 
              'St.Louis Large', 
              'Atlanta Large', 
              'Philadelphia Large']

lf_cap = [4000000, 4000000, 4000000, 4000000, 4000000]
sf_cap = [2000000, 2000000, 2000000, 2000000, 2000000]
              
#cost of storage+transportaion for book in a small facility in a given city
ac_sfc = new_sfc + av_tc 
ac_sfc = ac_sfc.transpose() 
s_f = dict(zip(small_facilities,ac_sfc))
sf_size = dict(zip(small_facilities,sf_cap))
del small_facilities, ac_sfc, new_sfc, sf_cap

#cost of storage+transportaion for book in a large facility in a given city
ac_lfc = new_lfc + av_tc 
ac_lfc = ac_lfc.transpose()
l_f = dict(zip(large_facilities,ac_lfc))
lf_size = dict(zip(large_facilities,lf_cap))
del large_facilities, ac_lfc, new_lfc, lf_cap

#dictionaries of size and cost
facilities = {**s_f, **l_f}
f_size = {**sf_size,**lf_size}
del s_f, l_f, lf_size, sf_size, av_tc

#narrows down facilities to which are 'cheapest'
while demand.sum() <= sum(f_size.values()):
    key = max(facilities, key=facilities.get)
    del facilities[key]
    del f_size[key]

del demand 
locations = list(f_size.keys())
location = locations.append(key)
print(locations)
    
del key, f_size, facilities