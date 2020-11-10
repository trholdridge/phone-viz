#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:50:39 2020

@author: tulasiholdridge
"""

from data_collection import *

# write data file
with open("phonology_data.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Language', 'Consonants'])
    for lang, consonants in phonologies.items():
        writer.writerow([lang, consonants])

# test change
