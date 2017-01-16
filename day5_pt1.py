import hashlib

door_id = 'ffykfhsq'
index = 0
count = 0
password = ''

while count < 8:
    encode_input = door_id + str(index)
    encode_output = hashlib.md5(encode_input.encode('utf-8')).hexdigest()
    if encode_output[0:5] == '00000':
        password = password + encode_output[5]
        count = count + 1
    index = index + 1

print(password)
