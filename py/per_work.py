def permutation_inv(lst):
    ans = [ lst.index(i) for i in lst]
    return ans

def is_permutstion(lst):
    return len(set(lst)) == len(list(lst))
