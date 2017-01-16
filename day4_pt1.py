import re
import operator

def getUniqueLetters(string):
    characters = []
    for char in string:
        a = re.match('[a-z]', char)
        # Valid character
        if a != None and char not in characters:
            characters.append(char)
    return characters

# String passed to this function needs to have the checksum removed first
def getLetterCount(string):
    list_of_letters = getUniqueLetters(string)
    dictionary = dict()
    for lol_letter in list_of_letters:
        letter_count = 0
        for str_letter in string:
            if str_letter == lol_letter:
                letter_count = letter_count + 1
        letter_pair = {lol_letter: letter_count}
        dictionary.update(letter_pair)
    return dictionary

def getDistinctLetterCount(list_of_letters):
    letter_count = []
    for letter, count in list_of_letters.items():
        if count not in letter_count:
            letter_count.append(count)
    return letter_count

def computeChecksum(string):
    pair_list = getLetterCount(string)
    letter_count = getDistinctLetterCount(pair_list)
    master_list = []
    for digit in sorted(letter_count, reverse=True):
        sublist = []
        for letter, count in pair_list.items():
            if count == digit:
                sublist.append((letter, count))
        master_list.append(sublist)
    # Sort master_list
    computed_checksum = ''
    for l in master_list:
        if len(l) > 1:
            #sort alphabetical
            l.sort(key=operator.itemgetter(0))
        for i in l:
            computed_checksum = computed_checksum + i[0]
    return computed_checksum[:5] #first 5 only

def splitInput(string):
    a = string.rstrip(']').split('[')
    return a[0], a[1]

def validateChecksum(input_string):
    string, provided_checksum = splitInput(input_string)
    computed_checksum = computeChecksum(string)
    if computed_checksum == provided_checksum:
        return True
    else:
        return False

def extractDigits(string):
    string, provided_checksum = splitInput(string)
    digits = re.search('\d+$', string)
    return int(digits.group(0))

instructions = []
with open('/Users/felix/desktop/input.txt') as f:
    content = f.readlines()
    instructions.append(content)

new_i = []
for c in content:
    x = c.replace('\n', '')
    new_i.append(x)

count_sectorID = 0
for s in new_i:
    if validateChecksum(s):
        count_sectorID = count_sectorID + extractDigits(s)
print(count_sectorID)
