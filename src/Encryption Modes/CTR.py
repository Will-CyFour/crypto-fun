from secrets import randbits
import sys
from byte_opperations import XOR_two_blocks
sys.path.append('..')
from AES import encrypt #don't even need decrypt lol


#Does modular addition for the counter, in case the counter needs to wrap around
def mod_256_to_16_addition(vector:bytes, integer:int) -> bytes:
    vector_int = int.from_bytes(vector, byteorder='big')
    result = (vector_int + integer) % (256 ** 16)
    return result.to_bytes(16, byteorder='big')


print(mod_256_to_16_addition(b'\x00' + b'\xFF' * 15, 0))

#Encrypt with counter mode encryption, also has the option to choose your IV
def counter_mode_encrypt(plaintext: str | bytes, key: bytes, IV = None):
    if type(plaintext) == str:
        plaintext = plaintext.encode()

    #We should check to see if IV is valid
    if IV is None:
        IV = bytes([randbits(8) for _ in range(16)])
    key_string = b''
    for block in range((len(plaintext) + 15) // 16):#the + 15 is a little hack to avoid having to use a ceiling operation
        key_string += encrypt(message=(mod_256_to_16_addition(IV, block)), key=key)
    return IV + XOR_two_blocks(plaintext, key_string)

#Decrypt
def counter_mode_decrypt(ciphertext: str | bytes, key: bytes | None):
    IV = ciphertext[:16] #first 16 bytes of ciphertext
    counter_mode_encrypt(plaintext=ciphertext[16:], key=key, IV=IV)


#counter_mode_encrypt("hi", None)



h = b'\x01'
i = b'\x02\x05'
print(h)
print(i)
print(h + i)
i += i
print(i)


