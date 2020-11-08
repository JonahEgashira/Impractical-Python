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

def prep_words(name, word_list_ini):
    """Prepare word list for c-v list"""
    print("length of initial word_list = {}".format(len(word_list_ini)))
    len_name = len(name)
    word_list = [word.lower() for word in word_list_ini if len(word) == len_name]
    print("length of new word_list = {}".format(len(word_list)))
    return word_list

def cv_map_words(word_list):
    """map consonant and vowel by word"""
    vowels = 'aeiouy'
    cv_mapped_words = []

    for word in word_list:
        temp = ''
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        cv_mapped_words.append(temp)
    # filter UNIQUE c-v pattern
    total = len(set(cv_mapped_words))
    # percentage of exclude pattern
    target = 0.05
    exclude = int(total * target)
    count_pruned = Counter(cv_mapped_words).most_common(total - exclude)
    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print("length of filtered_cv_map = {}".format(len(filtered_cv_map)))
    return filtered_cv_map 


def cv_map_filter(name, filtered_cv_map):
    """remove impossible pattern of permutation based on c-v patterns"""
    perms = {''.join(i) for i in permutations(name)}
    print("length of initial permutations set = {}".format(len(perms)))
    vowels = 'aeiouy'
    filter_1 = set()
    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        if temp in filtered_cv_map:
            filter_1.add(candidate)
    print('# of choices after filter_1 = {}'.format(len(filter_1)))
    return filter_1

def trigram_filter(filter_1, trigrams_filtered):
    """remove impossible trigrams"""
    filtered = set()
    for candidate in filter_1:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate:
                filtered.add(candidate)
    filter_2 = filter_1 - filtered
    print('# of choices after filter_2 = {}'.format(len(filter_2)))
    return filter_2

def letter_pair_filter(filter_2):
    filtered = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv',
               'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd',
                          'rl', 'rm', 'rt', 'rv', 'tl', 'tm']
    for candidate in filter_2:
        for r in rejects:
            if r in candidate:
                filtered.add(candidate)
        for fp in first_pair_rejects:
            if candidate.startswith(fp):
                filtered.add(candidate)
    filter_3 = filter_2 - filtered
    print('# of choices after filter_3 = {}'.format(len(filter_3)))
    if 'voldemort' in filter_3:
        print("Voldemort found!", file=sys.stderr)
    return filter_3

def view_by_letter(name, filter_3):
    """filter by the first letter typed"""
    print("Remaining letters = {}".format(name))
    first = input("select a starting letter or press Enter to see all")
    subset = []
    for candidate in filter_3:
        if candidate.startswith(first):
            subset.append(candidate)
    print(*sorted(subset), sep='\n')
    print("Number of choices starting with {} = {}".format(first, len(subset)))
    try_again = input("try again? (Press Enter else any other key to Exit):")
    if try_again.lower() == '':
        view_by_letter(name,filter_3)
    else:
        sys.exit()

if __name__ == '__main__':
    main()

