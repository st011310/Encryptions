from str_work import is_permutstion
from str_work import str_ex
from str_work import str_left_shift
from str_work import str_xor
from str_work import str_permutation
from per_work import permutation_inv
from Feistel_cipher import FeistelCipher_D
from Feistel_cipher import FeistelCipher_E

STANDART_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
    ]

STANDART_SHIFTS = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
    ]

REDUCTION_64_TO_56 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
    ]

REDUCTION_56_TO_48 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
    ]

SUPER_BLOCK_TRANSFORMATION = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]


EXPANSION_PLANTTEXT = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
    ]

FINAL_S_PERMUTATION = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
    ]

if(not is_permutstion(STANDART_PERMUTATION)):
    raise Exception("STANDART_PERMUTATION is not permutstion")


def DES_E(P, K, r = 16, block_size = 32, IP = STANDART_PERMUTATION):
    if len(K) != 64:
        raise Exception("DES can't have a not 64 bits key")

    print('Редуцируем размер ключа:')
    K = str_ex(K, REDUCTION_64_TO_56)
    print(K)
    print('Находим все подключи:')
    K_half = len(K) // 2
    subkeys = [K]
    for i in range(r):
        tmp1 = subkeys[i][:K_half]
        tmp2 = subkeys[i][K_half:]
        tmp1 = str_left_shift(tmp1, STANDART_SHIFTS[i])
        tmp2 = str_left_shift(tmp2, STANDART_SHIFTS[i])
        subkeys.append(tmp1 + tmp2)
        print(tmp1, tmp2)
    del subkeys[0]
    print('Сжимаем все подключи до 48 бит:')
    for i in range(r):
        subkeys[i] = str_ex(subkeys[i], REDUCTION_56_TO_48)
        print(subkeys[i])
    def F(R, K):
        print("Расширим правый блок до 48 бит:")
        R = str_ex(R, EXPANSION_PLANTTEXT)
        print(R)
        print("Получим XOR от ключа и правого блока:")
        pred_ans = str_xor(R, K)#48 bits
        print(pred_ans)
        ans = ""
        for i in range(0, len(pred_ans), 6):
            print(f"Преобразуем блок S{i//6}.")
            tmp = pred_ans[i: i + 6]
            print(f"S{i//6} = {tmp}")
            row = int(tmp[0] + tmp[5], base = 2)
            column = int(tmp[1:5], base = 2)
            tmp = SUPER_BLOCK_TRANSFORMATION[i // 6][row][column]
            tmp = bin(tmp)[2:]
            tmp = "0" * (4 - len(tmp)) + tmp 
            print(f"S{i//6} := T[{row}][{column}] = {tmp}")
            ans += tmp
        print("В результате получаем предложение:")
        print(ans)
        print("Сделаем заключительную перестановку:")
        ans = str_permutation(ans, FINAL_S_PERMUTATION)
        print(ans)
        return ans
    C = FeistelCipher_D(P, F, list(reversed(subkeys)), block_size)
    return C

def DES_E_Q(P, K, r = 16, block_size = 32, IP = STANDART_PERMUTATION):
    if len(K) != 64:
        raise Exception("DES can't have a not 64 bits key")
    K = str_ex(K, REDUCTION_64_TO_56)
    K_half = len(K) // 2
    subkeys = [K]
    for i in range(r):
        tmp1 = subkeys[i][:K_half]
        tmp2 = subkeys[i][K_half:]
        tmp1 = str_left_shift(tmp1, STANDART_SHIFTS[i])
        tmp2 = str_left_shift(tmp2, STANDART_SHIFTS[i])
        subkeys.append(tmp1 + tmp2)
    del subkeys[0]
    for i in range(r):
        subkeys[i] = str_ex(subkeys[i], REDUCTION_56_TO_48)
    def F(R, K):
        R = str_ex(R, EXPANSION_PLANTTEXT)
        pred_ans = str_xor(R, K)#48 bits
        ans = ""
        for i in range(0, len(pred_ans), 6):
            tmp = pred_ans[i: i + 6]
            row = int(tmp[0] + tmp[5], base = 2)
            column = int(tmp[1:5], base = 2)
            tmp = SUPER_BLOCK_TRANSFORMATION[i // 6][row][column]
            tmp = bin(tmp)[2:]
            tmp = "0" * (4 - len(tmp)) + tmp 
            ans += tmp
        ans = str_permutation(ans, FINAL_S_PERMUTATION)
        return ans
    C = FeistelCipher_D(P, F, list(reversed(subkeys)), block_size)
    return C

def DES_D(C, K, r = 16, block_size = 32, IP = STANDART_PERMUTATION):
    if len(K) != 64:
        raise Exception("DES can't have a not 64 bits key")

    print('Редуцируем размер ключа:')
    K = str_ex(K, REDUCTION_64_TO_56)
    print(K)
    print('Находим все подключи:')
    K_half = len(K) // 2
    subkeys = [K]
    for i in range(r):
        tmp1 = subkeys[i][:K_half]
        tmp2 = subkeys[i][K_half:]
        tmp1 = str_left_shift(tmp1, STANDART_SHIFTS[i])
        tmp2 = str_left_shift(tmp2, STANDART_SHIFTS[i])
        subkeys.append(tmp1 + tmp2)
        print(tmp1, tmp2)
    del subkeys[0]
    print('Сжимаем все подключи до 48 бит:')
    for i in range(r):
        subkeys[i] = str_ex(subkeys[i], REDUCTION_56_TO_48)
        print(subkeys[i])
    def F(R, K):
        print("Расширим правый блок до 48 бит:")
        R = str_ex(R, EXPANSION_PLANTTEXT)
        print(R)
        print("Получим XOR от ключа и правого блока:")
        pred_ans = str_xor(R, K)#48 bits
        print(pred_ans)
        ans = ""
        for i in range(0, len(pred_ans), 6):
            print(f"Преобразуем блок S{i//6}.")
            tmp = pred_ans[i: i + 6]
            print(f"S{i//6} = {tmp}")
            row = int(tmp[0] + tmp[5], base = 2)
            column = int(tmp[1:5], base = 2)
            tmp = SUPER_BLOCK_TRANSFORMATION[i // 6][row][column]
            tmp = bin(tmp)[2:]
            tmp = "0" * (4 - len(tmp)) + tmp 
            print(f"S{i//6} := T[{row}][{column}] = {tmp}")
            ans += tmp
        print("В результате получаем предложение:")
        print(ans)
        print("Сделаем заключительную перестановку:")
        ans = str_permutation(ans, FINAL_S_PERMUTATION)
        print(ans)
        return ans
    P = FeistelCipher_D(C, F, list(reversed(subkeys)), block_size)
    return P

def DES_D_Q(C, K, r = 16, block_size = 32, IP = STANDART_PERMUTATION):
    if len(K) != 64:
        raise Exception("DES can't have a not 64 bits key")
    K = str_ex(K, REDUCTION_64_TO_56)
    K_half = len(K) // 2
    subkeys = [K]
    for i in range(r):
        tmp1 = subkeys[i][:K_half]
        tmp2 = subkeys[i][K_half:]
        tmp1 = str_left_shift(tmp1, STANDART_SHIFTS[i])
        tmp2 = str_left_shift(tmp2, STANDART_SHIFTS[i])
        subkeys.append(tmp1 + tmp2)
    del subkeys[0]
    for i in range(r):
        subkeys[i] = str_ex(subkeys[i], REDUCTION_56_TO_48)
    def F(R, K):
        R = str_ex(R, EXPANSION_PLANTTEXT)
        pred_ans = str_xor(R, K)#48 bits
        ans = ""
        for i in range(0, len(pred_ans), 6):
            tmp = pred_ans[i: i + 6]
            row = int(tmp[0] + tmp[5], base = 2)
            column = int(tmp[1:5], base = 2)
            tmp = SUPER_BLOCK_TRANSFORMATION[i // 6][row][column]
            tmp = bin(tmp)[2:]
            tmp = "0" * (4 - len(tmp)) + tmp 
            ans += tmp
        ans = str_permutation(ans, FINAL_S_PERMUTATION)
        return ans
    P = FeistelCipher_D(C, F, subkeys, block_size)
    return P

if __name__ == '__main__':
    from random import randint
    flg = True
    while flg:
        P = "".join([str(randint(0, 1)) for _ in range(64)])
        K = "".join([str(randint(0, 1)) for _ in range(64)])
        print("P =", P)
        print("K =", K)
        C = DES_E_Q(P, K, 1)
        print("C =", C)
        if P != DES_D_Q(C, K, 1):
            print("ERROR!")
            print(f"D[C] = {DES_D_Q(C, K, 1)}")
            print(f"P    = {P}")
        else:
            print('OK')
        flg = input() != "0"
