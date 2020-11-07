import sys
from itertools import permutations
from collections import Counter
import load_dictionary

def main():
    """Read file, filter them, and User can see anagrams at the first character"""
    name = 'tmvoordle'
    name = name.lower()

    word_list_ini = load_dictionary.load('2of4brif.txt')

    trigrams_filtered = load_dictionary.load('least-likely_trigrams.txt')

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)

