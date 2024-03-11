from Sbox import Sbox
from constants import NUMBER_OF_ROUNDS


ROUND_CONSTANTS = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

def xor_words(word1, word2):
    return [a ^ b for a, b in zip(word1, word2)]

def g_function(word:list, round_num:int):
    """Take a list of 4 ints and perform the g function on them"""
    new_word = word.copy()
    new_word = new_word[1:] + new_word[:1]
    for i in range(len(new_word)):
        new_word[i] = Sbox(new_word[i])
    new_word[0] = new_word[0] ^ ROUND_CONSTANTS[round_num]
    return new_word

def key_expansion(key:bytes):
    ints_list = list(key) #converts bytes to list of ints
    words_list = [ints_list[i:i+4] for i in range(0, len(ints_list), 4)] #split into 4 lists
    for round_num in range(NUMBER_OF_ROUNDS):
        w_0 = words_list[-4].copy()
        w_1 = words_list[-3].copy()
        w_2 = words_list[-2].copy()
        w_3 = words_list[-1].copy()
        g_result = g_function(w_3, round_num) #take the very last word and run it through the g function
        words_list.append(xor_words(g_result, w_0))
        words_list.append(xor_words(words_list[-1], w_1))
        words_list.append(xor_words(words_list[-1], w_2))
        words_list.append(xor_words(words_list[-1], w_3))
    return words_list


