from constants import BLOCK_SIZE

#XORs two bytes objects of any size together, if they have different lengths the additional bytes are ignored
def XOR_two_blocks(block1:bytes, block2:bytes):
    if len(block1) < len(block2):
        return XOR_two_blocks(block2, block1)
    return bytes(a ^ b for a, b in zip(block1, block2[:len(block1)]))

#PKCS padding for ECB and CBC
def pad_PKCS7(data: bytes):
    pad_size = BLOCK_SIZE - len(data) % BLOCK_SIZE
    padding = bytes([pad_size]) * pad_size
    result = data + padding
    assert len(result) % BLOCK_SIZE == 0
    return data + padding

def unpad_PKCS7(data: bytes):
    padding_size = int(data[-1])
    return data[:-padding_size]

