#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:52:58 2020

@author: tulasiholdridge
"""
import csv
from web_scraper_functions import *

lang_dir = create_lang_list() # scrape Help:IPA page to get all languages
all_consonants = set(scrape_ipa_pages(lang_dir))

# create a dictionary that maps langs to their phonologies
phonologies = dict(zip(lang_dir, all_consonants))