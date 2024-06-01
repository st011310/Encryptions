from str_work import str_xor
def FeistelCipher(P, F, subkeys, blocksize = 32):
    r = len(subkeys)
    if len(P) % blocksize != 0:
        P = "0" * (blocksize - len(P) % blocksize) + P
    if len(P) > 2 * blocksize:
        return NotImplemented
    L = P[:blocksize]
    R = P[blocksize:]
    for i in range(r):
        L, R = R, str_xor(L, F(R, subkeys[i]))
    C = L + R
    return C
