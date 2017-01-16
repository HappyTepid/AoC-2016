instructions = []
with open('/Users/felix/desktop/day6.txt') as f:
    content = f.readlines()
    instructions.append(content)

new_i = []
for c in content:
    x = c.replace('\n', '')
    new_i.append(x)

def getDistinctChars(string):
    dist_chars = []
    for char in string:
        if char not in dist_chars:
            dist_chars.append(char)
    return dist_chars

def countCharAppearances(string):
    master_list = []
    distinct_chars = getDistinctChars(string)
    for d_char in distinct_chars:
        char_count = 0
        for s_char in string:
            if d_char == s_char:
                char_count = char_count + 1
        pair = (d_char, char_count)
        master_list.append(pair)
    return master_list

def getMostCommonLetter(string):
    highest_count = ('a', 0)
    tuples = countCharAppearances(string)
    for pair in tuples:
        if pair[1] > highest_count[1]:
            highest_count = pair
    return highest_count[0]

password_length = len(new_i[0])
password = ''
x = 0
while x < password_length:
    column = []
    for string in new_i:
        column.append(string[x])
    password = password + getMostCommonLetter(column)
    x = x + 1
print(password)
