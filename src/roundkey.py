from Sbox import Sbox
from constants import NUMBER_OF_ROUNDS


ROUND_CONSTANTS = [ 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

def xor_words(word1, word2):
    return [a ^ b for a, b in zip(word1, word2)]

# Take a list of 4 ints and perform the g function on them
def g_function(word:list, round_num:int):

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






"""
00000000
00000000
00000000
00000000
62636363
62636363
62636363
62636363
9b9898c9
f9fbfbaa
9b9898c9
f9fbfbaa
90973450
696ccffa
f2f45733
0b0fac99
ee06da7b
876a1581
759e42b2
7e91ee2b
7f2e2b88
f8443e09
8dda7cbb
f34b9290
ec614b85
1425758c
99ff0937
6ab49ba7
21751787
3550620b
acaf6b3c
c61bf09b
0ef90333
3ba96138
97060a04
511dfa9f
b1d4d8e2
8a7db9da
1d7bb3de
4c664941
b4ef5bcb
3e92e211
23e951cf
6f8f188e"""