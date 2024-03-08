import sys

sys.path.append('..')
from AES import encrypt, decrypt
from constants import BLOCK_SIZE
from byte_opperations import pad_PKCS7, unpad_PKCS7


def ECB_encrypt(plaintext: bytes, key: bytes):

    padded_plaintext = pad_PKCS7(plaintext)
    ciphertext = b''
    for i in range(padded_plaintext // BLOCK_SIZE):
        curr_block = padded_plaintext[i * 16: (i + 1) * 16]
        assert len(curr_block) == BLOCK_SIZE
        ciphertext += encrypt(curr_block, key)
    return ciphertext

def ECB_decrypt(ciphertext: bytes, key: bytes):
    padded_plaintext = b''
    for i in range(ciphertext // BLOCK_SIZE):
        padded_plaintext += decrypt(ciphertext[i], key)
    return unpad_PKCS7(padded_plaintext)

print(BLOCK_SIZE)
