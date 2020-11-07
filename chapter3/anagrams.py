import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

anagram_list = []

#input name
name = input("Input name = ")
name = name.lower()
print(f'Using name = {name}')

#sort name & find anagrams

name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    # anagrams shouldn't be the same
    if word != name_sorted:
        if name_sorted == sorted(word):
            anagram_list.append(word)
            

if len(anagram_list) == 0:
    print("There are no anagrams")
else:
    #Fancy way to print list
    print("Anagrams = ", *anagram_list, sep='\n')

