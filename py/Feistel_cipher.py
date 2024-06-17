from str_work import str_xor
def FeistelCipher_E(P, F, subkeys, blocksize = 32):
    r = len(subkeys)
    if len(P) % blocksize != 0:
        P = "0" * (blocksize - len(P) % blocksize) + P
    if len(P) > 2 * blocksize:
        return NotImplemented
    L = P[:blocksize]
    R = P[blocksize:]
    for i in range(r):
        L, R = str_xor(R, F(L, subkeys[i])), L
        #L, R = R, str_xor(L, F(R, subkeys[i]))
    C = R + L
    return C

def FeistelCipher_D(C, F, subkeys, blocksize = 32):
    subkeys = list(reversed(subkeys))
    P = FeistelCipher_E(C, F, subkeys, blocksize)
    return P

if __name__ == '__main__':
    from random import randint
    flg = True
    def f(X, R):
        return str_xor(X, R)
    while flg:
        P = "".join([str(randint(0, 1)) for _ in range(64)])
        print("P =", P)
        lst = ["".join([str(randint(0, 1)) for _ in range(32)]) for __ in range(16)]
        for i in range(len(lst)):
            print(f"K{i} =", lst[i])
        C = FeistelCipher_E(P, f, lst)
        print("C =", C)
        if P != FeistelCipher_D(C, f, lst):
            print("ERROR!")
            print(FeistelCipher_D(C, f, lst))
        else:
            print('OK')
        flg = input() != '0'
