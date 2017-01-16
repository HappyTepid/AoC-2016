def splitInput(string):
    non_bracks = []
    bracks = []
    buffer = ''
    in_bracks = False
    for char in string:
        if not in_bracks:
            if char != '[':
                buffer += char
            else:
                # begin bracks
                non_bracks.append(buffer)
                buffer = ''
                in_bracks = True
        else:
            if char != ']':
                buffer += char
            else:
                # end bracks
                bracks.append(buffer)
                buffer = ''
                in_bracks = False
    if not in_bracks:
        non_bracks.append(buffer)
    else:
        bracks.append(buffer)
    return non_bracks, bracks

def findABA(list_of_strings):
    return_list = []
    for sequence in list_of_strings:
        char_minus_2 = ''
        char_minus_1 = ''
        current_char = ''
        for char in sequence:
            char_minus_2 = char_minus_1
            char_minus_1 = current_char
            current_char = char
            if char_minus_2 == current_char and char_minus_1 != char_minus_2:
                return_list.append(char_minus_2+char_minus_1+current_char)
    return return_list

def reverseABA(findABA_output):
    return str(findABA_output[1]+findABA_output[0]+findABA_output[1])

def evaluateString(string):
    non_bracks, bracks = splitInput(string)
    ABA = findABA(non_bracks)
    for A in ABA:
        for b in bracks:
            if reverseABA(A) in b:
                return True
    return False

instructions = []
with open('/Users/felix/desktop/day7.txt') as f:
    content = f.readlines()
    instructions.append(content)

new_i = []
for c in content:
    x = c.replace('\n', '')
    new_i.append(x)

count = 0
for s in new_i:
    if evaluateString(s):
        count = count + 1
print(count)
