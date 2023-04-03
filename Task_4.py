n = (1, 3, 4, 6, 8, 11, 2, 3)
r_n = 4
def del_from_tuple(tpl, number):
    if not (number in tpl):
       return tpl
    else:
        k = tpl.index(number)
        return tuple(list(tpl)[0:k] + list(tpl[k + 1:]))


print(del_from_tuple(n, r_n))



