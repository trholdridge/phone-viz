#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:36:38 2020

@author: tulasiholdridge
"""
import json
import statistics as stats
import matplotlib.pyplot as plt
plt.ioff() # don't automatically show figures


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

# analyze_num_consonants : {X} [[List-of Number] -> X] Dict -> X
def analyze_num_consonants(f,d):
    return f([len(consonants) for consonants in d.values()])

# most_consonants : Dict -> String
# finds which language in a dict has the most consonants
def most_consonants(d):
    return analyze_num_consonants(max,d)

# least_consonants : Dict -> String
# finds which language in a dict has the least consonants
def least_consonants(d):
    return analyze_num_consonants(min,d)

# avg_num_consonants : Dict -> Number
# finds average number of consonants for all langs in a dict
def avg_num_consonants(d):
    return analyze_num_consonants(stats.mean,d)

# median_num_consonants : Dict -> Number
# finds median number of consonants for all langs in a dict
def median_num_consonants(d):
    return analyze_num_consonants(stats.median,d)

# def num_consonants_histo:
# plots a histogram with number of consonants in each lang
def num_consonants_histo(d):
    fig = plt.figure()
    plt.hist(analyze_num_consonants(lambda x : x, d), 
             range(least_consonants(d),most_consonants(d),3), 
             color='pink')
    plt.xticks(range(least_consonants(d),most_consonants(d),3))
    plt.xlabel("Number of consonants")
    plt.ylabel("Number of languages")
    plt.title("How many consonants do languages have?")
    return fig
    
# def consonant_frequency:

# list_all_consonants : Dict -> Set
# returns all consonants present in the phoneme dictionary
def list_all_consonants(d):
    return set().union(*[consonants for consonants in d.values()])
    