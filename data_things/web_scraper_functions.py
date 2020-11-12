#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:06:43 2020

@author: tulasiholdridge
"""
from bs4 import BeautifulSoup
import requests

# create a dictionary that maps langs to their phonologies
def make_phonology_dict(langs,consonant_sets):
    dict(zip(langs, consonant_sets))

# make_lang_list : _ -> [List-of String]
# creates a list of strings, where each string is a language
# under wikipedia's directory of Help:IPA pages
def make_lang_list():
    # use requests and beautiful soup to grab wiki page contents
    parent_url = 'https://en.wikipedia.org/wiki/Help:IPA'
    parent_page = requests.get(parent_url)
    directory_soup = BeautifulSoup(parent_page.content, 'html.parser')
    
    # narrow down content to the section we want
    table_container = directory_soup.find('div', attrs={'aria-labelledby' : 'International_Phonetic_Alphabet_keys'})
    table_section = table_container.find('td')
    table_links = table_section.find_all('a')
    
    # add urls to a list
    lang_dir_long = []
    for link in table_links:
        lang_dir_long.append(link.get('href')) # extract url from 'a' object
    
    # shorten to just language name as used in url
    lang_dir = []
    for link in lang_dir_long:
        lang_dir.append(link[15:])
        
    # return list of language names
    return lang_dir


# make_consonant_list : List -> [List-of Set]
# navigates to the Help:IPA/[Language] page for every language in a list
# and puts the set of its consonants in a list
def make_consonant_list(lang_list):
    url_prefix = "https://en.wikipedia.org/wiki/Help:IPA/"
    # this won't be run often, so not worried about vectorization
    consonant_lists = [scrape_ipa(url_prefix + lang) for lang in lang_list]
    
    #return list of consonant sets
    return consonant_lists
    
# scrape_ipa : String -> [List-of Set]
# gets all IPA consonants from a url specified by the String, and returns
# them in set form
def scrape_ipa(lang):
    # use requests and beautiful soup to grab wiki page contents
    lang_page = requests.get(lang)
    soup = BeautifulSoup(lang_page.content, 'html.parser')
    
    # locate consonant table
    test_table_format = soup.find('a', attrs={'title' : 'Consonant'})
    
    # most pages are formatted a certain way, but some won't be
    if (test_table_format is None):
        # cheesing it for now
        return
    
    # if it's the normal formatting, go through the procedure
    consonant_table_raw = test_table_format.parent.parent.parent
    consonant_table = consonant_table_raw.find_all('tr')
    consonant_links = []
    # if the row has no link, don't use it. if it does, add it to list
    for table_row in consonant_table:
        temp = table_row.find('a') # will be None if the row doesn't have a link
        if (temp is not None):
            consonant_links.append(temp)

    #add consonants to a list
    consonants = []
    for link in consonant_links:
        try:
            temp_class = link.parent['class'] # is there a class?
            if (temp_class[0] == 'IPA'): # if the row has a consonant
                consonants.append(link.contents[0]) # just the text
        except KeyError: # if no parent class
            continue
    
    #return set of consonants
    return set(consonants)

