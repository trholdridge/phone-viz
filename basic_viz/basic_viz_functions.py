#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:36:38 2020

@author: tulasiholdridge
"""
import json
import matplotlib.pyplot as plt

# first, access the already-created phonology data
with open('../data_things/phonology_data.txt') as txtfile:
  phono_dict_raw = json.load(txtfile)

#-----------------------------------------------------#
#------------------ processing dict ------------------#
#-----------------------------------------------------#

# filter_dict : Dict -> Dict
# removes entries where no phonemes were extracted
def filter_dict(d):
    return (dict(filter(is_valid_entry, d.items())))

# is_valid_entry : DictItem -> Boolean
# is the phoneme portion of an entry in the phoneme dictionary 
# a list with > 0 elements?
def is_valid_entry(e):
    return (isinstance(e[1], list) and len(e[1]) > 0)

# dict_lists_to_sets : Dict -> Dict
# converts phoneme lists in dict to sets
def dict_lists_to_sets(d):
    return (dict(map(entry_list_to_set, d.items())))
            
# entry_list_to_set : DictItem -> DictItem
# changes the list of phonemes in a dict entry to a set of phonemes
def entry_list_to_set(e):
    return (e[0], set(e[1]))

#-----------------------------------------------------#
#--------------------- constants ---------------------#
#-----------------------------------------------------#

# number of languages listed on the wikipedia directory page
#TOTAL_LANGS = phono_df_raw.shape[0]
# number of languages where consonants were successfully scraped
#SUCCESSFUL_LANGS = phono_df.shape[0]

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
#def median_num_consonants():
    #return phono_df['Consonants'].median


# def num_consonants_histo:

# def consonant_frequency:

# def list_all_consonants: