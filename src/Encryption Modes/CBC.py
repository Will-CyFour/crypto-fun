from secrets import randbits
import sys
from byte_opperations import XOR_two_blocks, pad_PKCS7, unpad_PKCS7
sys.path.append('..')
from AES import encrypt
from constants import BLOCK_SIZE


def CBC_encrypt(plaintext, key, IV: bytes | None = None):
    padded_plaintext = pad_PKCS7(plaintext)
    if IV is None:
        IV = [secrets.randbits(8) for _ in range(BLOCK_SIZE)]
    previous_ciphertext_block = IV
    ciphertext = b''
    for i in range(len(padded_plaintext) // BLOCK_SIZE):
        current_plaintext_block = padded_plaintext[i * 16: (i + 1) * 16]
        assert len(current_plaintext_block) == BLOCK_SIZE
        XOR_two_blocks(current_plaintext_block, previous_ciphertext_block)
        intermediate_value = XOR_two_blocks(current_plaintext_block, previous_ciphertext_block)
        current_ciphertext_block = encrypt(intermediate_value, key)
        ciphertext += current_ciphertext_block
        previous_ciphertext_block = current_ciphertext_block
    return IV + ciphertext

def CBC_MAC(text, key):
    enc = CBC_encrypt(text, key, IV=b'\x00'*16)
    return enc[-16:]

print(CBC_MAC(b'hi', b'\xF1'*16))



