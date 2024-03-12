
def transpose(text):
    transposed_text = []
    for i in range(4):
        transposed_text.append(list(word[i] for word in text))
    return transposed_text

def mix_columns(text, inverse=False):
    mixing_function = inverse_mix_single_column if inverse else mix_single_column
    for i in range(len(text)):
        text[i] = mixing_function(text[i])
    return text


def mix_single_column(column):
    result_column = [0] * 4

    result_column[0] = multiply(0x02, column[0]) ^ multiply(0x03, column[1]) ^ column[2] ^ column[3]
    result_column[1] = column[0] ^ multiply(0x02, column[1]) ^ multiply(0x03, column[2]) ^ column[3]
    result_column[2] = column[0] ^ column[1] ^ multiply(0x02, column[2]) ^ multiply(0x03, column[3])
    result_column[3] = multiply(0x03, column[0]) ^ column[1] ^ column[2] ^ multiply(0x02, column[3])

    return result_column


def inverse_mix_single_column(column):
    result_column = [0] * 4

    result_column[0] = multiply(0x0e, column[0]) ^ multiply(0x0b, column[1]) ^ multiply(0x0d, column[2]) ^ multiply(0x09, column[3])
    result_column[1] = multiply(0x09, column[0]) ^ multiply(0x0e, column[1]) ^ multiply(0x0b, column[2]) ^ multiply(0x0d, column[3])
    result_column[2] = multiply(0x0d, column[0]) ^ multiply(0x09, column[1]) ^ multiply(0x0e, column[2]) ^ multiply(0x0b, column[3])
    result_column[3] = multiply(0x0b, column[0]) ^ multiply(0x0d, column[1]) ^ multiply(0x09, column[2]) ^ multiply(0x0e, column[3])

    return result_column


def multiply(a, b):
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B  # This is the irreducible polynomial for AES
        b >>= 1
    return result

