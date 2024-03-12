from roundkey import key_expansion, xor_words
from constants import NUMBER_OF_ROUNDS
from Sbox import inv_Sbox
from mix_columns import mix_columns, transpose

def inv_sub_bytes(text):
    for i in range(4):
        for j in range(4):
            text[i][j] = inv_Sbox(text[i][j])
    return text


def inv_shift_rows(text):
    transposed_text = transpose(text)
    for i in range(1, 4):
        transposed_text[i] = transposed_text[i][-i:] + transposed_text[i][:-i]
    result_text = transpose(transposed_text)
    return result_text


def add_round_key(text, round_key):
    result = []
    for i in range(4):
        result.append(xor_words(text[i], round_key[i]))
    return result



def decrypt(ciphertext:bytes, key:bytes):
    extended_key = key_expansion(key)
    working_text = list(ciphertext) #converts bytes to list of ints
    working_text = [working_text[i:i+4] for i in range(0, len(working_text), 4)] #split into 4 lists
    for round_num in range(NUMBER_OF_ROUNDS, 0, -1):
        working_text = add_round_key(working_text, extended_key[round_num * 4:round_num * 4 + 4])
        if round_num != 10:
            working_text = mix_columns(working_text, inverse=True)
        working_text = inv_shift_rows(working_text)
        working_text = inv_sub_bytes(working_text)

    working_text = add_round_key(working_text, extended_key[0:4])

    return bytes([item for sublist in working_text for item in sublist])




