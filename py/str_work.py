from per_work import is_permutstion
def binary_string(S, encoding = 'cp1251'):
    ans = S.encode(encoding)
    ans = list(ans)
    ans = [bin(num)[2:] for num in ans]
    ans = "".join(ans)
    return ans

def hex_string(S, encoding = 'cp1251'):
    ans = S.encode(encoding)
    ans = list(ans)
    ans = [hex(num)[2:] for num in ans]
    ans = "".join(ans)
    return ans

def str_xor(s1, s2):
    if len(s1) != len(s2):
        raise Exception(f"Impossible to XOR {len(s1)} len string and {len(s2)} len string!")
    ans = [str(int(s1[i] != s2[i])) for i in range(len(s1))]
    return "".join(ans)

def str_permutation(s,lst):
    if not is_permutstion(lst):
        raise Exception("This is not permutation!")
    if len(s) != len(lst):
        raise Exception("Impossible!")
    ans = [s[i-1] for i in lst]
    return "".join(ans)

def str_ex(s, lst):
    ans = [s[i-1] for i in lst]
    return "".join(ans)

def str_left_shift(s, k):
    n = len(s)
    ans = [s[(i + k) % n] for i in range(n)]
    return "".join(ans)
