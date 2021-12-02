from secrets import *
from pwn import *
import argparse

# OTP Requirements
# 1. Key must be same at least length of message
# 2. Key must never be reused
# 3. Key must be retrieved from random, or in a real case, pseudo-random generator
# 4. Key must be sent over secure medium 
    # - Up to user


#Xor byte values
def xor_bytes(message, key):
    value = '{:x}'.format(int(message, 16) ^ int(key, 16))
    return value

#Generate random key that is same length as message
def generate_key(message, used_keys):
    #Used for conditional break
    boolean = 0

    #Used to get list of used keys
    key_list = []

    #Populate list of keys
    for key in used_keys:
        if key != '\n':
            key_list.append(key.strip('\n'))

    # Recursively check to ensure key is new
    while(boolean == 0):
        # Generate key that is the length of the message to support requirement 1 
        # (Dividing over 2 because function is length doubling PRG)
        # PRG is pseudo random (https://docs.python.org/3/library/secrets.html) Supports requirement 3
        key = token_hex(int(len(message)/2))
        
        # IF you wanna test (program will just keep looping) => key = 'c203142209549f'

        #Check if key was already used to support requirement 2
        if(key not in key_list):
            boolean = 1
            used_keys = open('used_keys.txt', 'a+')
            used_keys.write(key+'\n')
            return key
 
# Encrypt a message
def encrypt(message):
    used_keys = open('used_keys.txt', 'r')
    message = message.encode('utf-8').hex()
    key = generate_key(message, used_keys)
    encrypted_message = xor_bytes(message, key)
    print("Encrypted message: {}, Key: {}".format(encrypted_message, key))

# Decrypt a message
def decrypt(ciphertext, key):
    message = '{:x}'.format(int(ciphertext, 16) ^ int(key, 16))
    print(unhex(message))
    

#Parse arguments
def main():
 
    # Create the parser
    parser = argparse.ArgumentParser()
    
    # Encrypt message
    parser.add_argument('--encrypt', required=False, help='Encrypt a message. Key generated randomly.')

    # Decrypt a message
    parser.add_argument('--decrypt', required=False, help='Decrypt a message. Requires key.')
    parser.add_argument('--key', required=False, help='Key used for decryption. Requires ciphertext.')
  
    # Parse the argument
    args = parser.parse_args()

    
    if args.encrypt:
        encrypt(args.encrypt)
    
    elif args.decrypt: 
        # Check if ciphertext but no key
        if args.key == None:
            print("Need key for decryption")
            exit(0)
        else:
            decrypt(args.decrypt, args.key)
    
    elif args.key:
        # Check if key but no ciphertext
        if args.decrypt == None:
            print("Need ciphertext for decryption")
            exit(0)
        else:
            decrypt(args.decrypt, args.key)

main()

    
    

    


    



