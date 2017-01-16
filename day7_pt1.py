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

def hasABBA(list_of_strings):
    has_ABBA = False
    for string in list_of_strings:
        s_len = len(string)
        index = 0
        last_char = None
        for char in string:
            if last_char == None:
                last_char = char
            else:
                if char == last_char:
                    a = string[index - 2:index + 2]
                    if len(a) == 4:
                        potential = a
                        if potential[0] == potential[3] and potential[0] != potential[1]:
                            has_ABBA = True
                last_char = char
            index += 1
    return has_ABBA

def stringCompliant(string):
    non_bracks, bracks = splitInput(string)
    if hasABBA(non_bracks) and not hasABBA(bracks):
        return True
    else:
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
for IP in new_i:
    if stringCompliant(IP):
        count += 1
print(count)
