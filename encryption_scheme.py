#
# Project 1, Frequency Analysis
#
import random
import os
import json
import random
from random import randrange
import string

# printing lowercase
# https://www.educative.io/edpresso/how-to-generate-a-random-string-in-python
#generate random key


def generate_random_key(t):
    letters=string.ascii_lowercase
    key = ''.join(random.choice(letters) for i in range(t));
    return key;

# calculate the j(i)
# i location within L
# t length of key
# l length of the message

#letter_key = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,
#"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26," ":27}
letter_key = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
L = 500;
plaintext = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago";
L= len(plaintext);

def get_j_of_i(i,t,l):
    #adding 2 to t so the T value can be larger than
    if t%2==0:
        t_max=t
    else:
        t_max=t
    if(i%2):
        return i%t_max;
    else:
        return ((l-i*t)%l)%t_max;

def encrypt_message(plaintext, key):

    t=len(key);
    L=len(plaintext);
    cipher_i = 0;
    i=0;
    cipher_out="";
    while i<L:
        #calculate j(i)
        plaintext_ascii = ord(plaintext[i]);
        #lowercase ascii codes are 97-122 w/ space being 32;
        #converts char to ascii with space at a @ 0 and space at 26
        if(plaintext_ascii==32):
            plaintext_ascii=26;
        else:
            plaintext_ascii-=97;
        shift_cipher = get_j_of_i(cipher_i,t,L)
        if shift_cipher==0 or shift_cipher>t:
            while shift_cipher==0 or shift_cipher>t:

                #j(i) dictactes that we insert a random character
                cipher_out+=letter_key[randrange(27)]
                shift_cipher = get_j_of_i(cipher_i,t,len(plaintext))
                #moving forward to shift cipher to ensure we don't lose any of the message
                cipher_i+=1;
        #shift plaintext by cipher
        plaintext_ascii+=shift_cipher;
        #ensuring if the shift moves past <space> it returns to a @ 0
        plaintext_ascii = (plaintext_ascii)%27;
        cipher_out+= letter_key[plaintext_ascii].upper();
        cipher_i+=1
        i+=1
    return cipher_out;



def decrypt_message(cipher, key, L):
    t=len(key);
    cipher_length = len(cipher)
    i=0;
    decrypted_message=""
    while i<cipher_length:
        #calculate j(i)
        shift_cipher = get_j_of_i(i,t,L)
        if shift_cipher==0 or shift_cipher>t:
            while shift_cipher==0 or shift_cipher>t:
                #j(i) dictactes that we insert a random character
                shift_cipher = get_j_of_i(i,t,len(plaintext))
                #moving forward to shift cipher to ensure we don't lose any of the message
                i+=1;
        plaintext_ascii = ord(cipher[i]);
        #lowercase ascii codes are 97-122 w/ space being 32;
        #converts char to ascii with space at a @ 0 and space at 26
        if(plaintext_ascii==32):
            plaintext_ascii=26;
        else:
            plaintext_ascii-=65;

        #shift plaintext by cipher
        plaintext_ascii-=shift_cipher;
        #ensuring if the shift moves past <space> it returns to a @ 0
        plaintext_ascii = (plaintext_ascii)%27;
        decrypted_message+= letter_key[plaintext_ascii].lower();
        i+=1
    return decrypted_message;


i=0;
t = int(input("Enter length of key: "))
if t<4: t=4
if t>20: t=20

#generate dynamic
key = generate_random_key(t);
encrypted_message = encrypt_message(plaintext, key);
decrypted_message = decrypt_message(encrypted_message, key, len(plaintext));
print("Plain Text:", end='')
print(plaintext)
print("key:" + key);
print("\n")
print("Ciphertext Random Characters Lower:" + encrypted_message);
print("\n")
print("Ciphertext:"+ encrypted_message.upper())
print("\n")
print("Decrypted Message:"+ decrypted_message.lower())
print("\n")
