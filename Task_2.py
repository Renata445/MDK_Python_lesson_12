n = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
r_n = 2
def slicer(tpl, random_num):
    if random_num not in tpl:
        return ()
    if tpl.count(random_num) == 1:
        return tpl[tpl.index(random_num):]
    return tpl[tpl.index(random_num):tpl.index(random_num, tpl.index(random_num) + 1) + 1]

print(slicer(n, r_n))
