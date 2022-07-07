# map -------------|
#                    |======>builtins
# filter-----------|
# reduce

from functools import reduce

lst = [10,2,30,4]
squares=list(map(lambda n:n**2,lst))
cubes=list(map(lambda n:n**3,lst))
#
# # map<5 num-1 >5 num+1
# # num_out=[num-1 if num<5 else num+1 for num in lst]
# # print(num_out)
#
num_out = list(map(lambda n: n - 1 if n < 5 else n + 1, lst))
print(num_out)

gt_ten = list(filter(lambda n: n > 10, lst))
print(gt_ten)

evens = list(filter(lambda n: n % 2 == 0, lst))
print(evens)

sum = reduce(lambda n1, n2: n1 + n2, lst)
print(sum)

all_product = reduce(lambda n1, n2: n1 * n2, lst)
print(all_product)

max_num = reduce(lambda n1, n2: n1 if n1 > n2 else n2, lst)
print(max_num)

min_num = reduce(lambda n1, n2: n1 if n1 < n2 else n2, lst)
print(min_num)
