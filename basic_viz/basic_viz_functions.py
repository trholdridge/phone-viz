#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:36:38 2020

@author: tulasiholdridge
"""
import pandas as pd
import matplotlib.pyplot as plt

# first, access the already-created phonology data
phono_df_raw = pd.read_csv("../data_things/phonology_data.csv",
                           dtype={"Language": str, "Consonants": list})

# 'Consonants == Consonants' ensures that it isn't NaN
filter_langs = 'Consonants == Consonants & Consonants != []'
phono_df = phono_df_raw.query(filter_langs).reset_index(drop=True)

#-----------------------------------------------------#
#--------------------- constants ---------------------#
#-----------------------------------------------------#

# number of languages listed on the wikipedia directory page
TOTAL_LANGS = phono_df_raw.shape[0]
# number of languages where consonants were successfully scraped
SUCCESSFUL_LANGS = phono_df.shape[0]

#-----------------------------------------------------#
#--------------------- functions ---------------------#
#-----------------------------------------------------#

# most_consonants : DF -> String
# finds which language in a df has the most consonants
# def most_consonants:

# least_consonants : DF -> String
# finds which language in a df has the least consonants
# def least_consonants:

# avg_num_consonants : DF -> Number
# finds average number of consonants for all langs in the df
# def avg_num_consonants:

# median_num_consonants : DF -> Number
# finds median number of consonants for all langs in the df
def median_num_consonants():
    return phono_df['Consonants'].median


# def num_consonants_histo:

# def consonant_frequency:

# def list_all_consonants: