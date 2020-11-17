#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:36:38 2020

@author: tulasiholdridge
"""
import json
import matplotlib.pyplot as plt


#-----------------------------------------------------#
#------------------- creating dict -------------------#
#-----------------------------------------------------#

# create_dict : _ -> Dict
# imports phoneme dictionary from .txt data file
def create_dict():
    with open('../data_things/phonology_data.txt') as txtfile:
        return json.load(txtfile)

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
#--------------------- functions ---------------------#
#-----------------------------------------------------#
    
# count_langs : Dict -> Nat
# counts number of entries in a dictionary
def count_langs(d):
    return len(d)

# most_consonants : Dict -> String
# finds which language in a dict has the most consonants
# def most_consonants(d):

# least_consonants : Dict -> String
# finds which language in a dict has the least consonants
# def least_consonants(d):

# avg_num_consonants : Dict -> Number
# finds average number of consonants for all langs in a dict
# def avg_num_consonants(d):

# median_num_consonants : Dict -> Number
# finds median number of consonants for all langs in a dict
#def median_num_consonants(d):


# def num_consonants_histo:

# def consonant_frequency:

# def list_all_consonants: