n = [1, 6, 9, 12, 16, 2, 1]

def sieve(lst):
    res = []
    for i in lst:
        if not (i in res):
            res = [i] + res
    return tuple(res)


print(sieve(n))
