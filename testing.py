from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
#Yoinked a standard AES implementation to test
def EvalAES(K, X):
  """
  Given the key K and the input X, evaluates AES-128 and returns the output Y.
  """
  cipher = Cipher(algorithms.AES(K), modes.ECB(), backend=default_backend())
  enc = cipher.encryptor()
  Y = enc.update(X) + enc.finalize()
  return Y

def InvertAES(K, Y):
  """
  Given the key K and the output Y, inverts AES-128 and returns the input X.
  """
  cipher = Cipher(algorithms.AES(K), modes.ECB(), backend=default_backend())
  dec = cipher.decryptor()
  X = dec.update(Y) + dec.finalize()
  return X

K = b'\x00' * 16
X = b'\x00' * 16
Y = EvalAES(X, X)
print(Y)


