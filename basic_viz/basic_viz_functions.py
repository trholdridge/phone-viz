#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:36:38 2020

@author: tulasiholdridge
"""
import pandas as pd

# first, access the already-created phonology data
phono_df_raw = pd.read_csv("../data_things/phonology_data.csv")

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
