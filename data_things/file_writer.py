#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:50:39 2020

@author: tulasiholdridge
"""
import csv
from web_scraper_functions import make_lang_list
from web_scraper_functions import make_consonant_list
from web_scraper_functions import make_phonology_dict

lang_dir = make_lang_list() # scrape Help:IPA page to get all languages
all_consonants = make_consonant_list(lang_dir)

# create the dict of phonologies
dictionary = make_phonology_dict(lang_dir,all_consonants)

# write data file
with open("phonology_data.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Language', 'Consonants'])
    for lang, consonants in dictionary.items():
        writer.writerow([lang, consonants])
