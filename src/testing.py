from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from AES import encrypt
from inverse_AES import decrypt, inv_sub_bytes
from AES import sub_bytes

# print(inv_sub_bytes(sub_bytes(0xFF)))


# Yoinked a standard AES implementation to test
def EvalAES(K, X):
    cipher = Cipher(algorithms.AES(K), modes.ECB(), backend=default_backend())
    enc = cipher.encryptor()
    Y = enc.update(X) + enc.finalize()
    return Y


def InvertAES(K, Y):
    cipher = Cipher(algorithms.AES(K), modes.ECB(), backend=default_backend())
    dec = cipher.decryptor()
    X = dec.update(Y) + dec.finalize()
    return X


key = b'Q'*5+b'O'*6+b'Z'*5
plaintext = b'J' * 16




print(decrypt(encrypt(plaintext, key), key))
