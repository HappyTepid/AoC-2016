import hashlib
import re

door_id = 'ffykfhsq'
index = 0
password = ['-','-','-','-','-','-','-','-']

while '-' in password:
    encode_input = door_id + str(index)
    encode_output = hashlib.md5(encode_input.encode('utf-8')).hexdigest()
    if encode_output[0:5] == '00000' and bool(re.search('\d', encode_output[5])):
        position = int(encode_output[5])
        if position < len(password):
            if password[position] == '-':
                password[position] = encode_output[6]
    index = index + 1
print(''.join(password))
