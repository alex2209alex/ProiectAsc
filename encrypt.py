import hashlib
import sys

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def xor_encrypt(input_file, output_file, password):
    from math import ceil

    f = open(input_file, 'r')
    g = open(output_file , 'wb')
    text = f.read()
    xorKey = password
    xorKey = ceil(len(text)/len(xorKey)) * xorKey
    length = len(text)

    for i, key in zip(range(length), xorKey):

        text = (text[:i] +
             chr(ord(text[i]) ^ ord(key)) +
                     text[i + 1:])
        g.write(text[i].encode())
    f.close()
    g.close()

if len(sys.argv) < 4:
    print("Error : not enough arguments!")
    sys.exit()
elif len(sys.argv) > 4:
    print("Error : too many arguments !")
    sys.exit()

for i, arg in enumerate(sys.argv):
    if i == 1:
        password = arg
    elif i == 2:
        input_file = arg
    elif i == 3:
        output_file = arg

if encrypt_string(password) != '3f1a2bcaca2f02a8cd826b57caa7fa8a3214da1856aedb1a2c24ef29c3ea3771':
    print('Wrong password!')
    sys.exit()
else :
    xor_encrypt(input_file, output_file, password)