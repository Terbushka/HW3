# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

# 3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# 4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches".format(5, 7))
# 6. By passing index numbers into the curly braces.
print("Anna has {0} apples and {1} peaches".format(5, 7))
# 7. By using keyword arguments into the curly braces.
print("Anna has {num_apples} apples and {num_peaches} peaches.".format(num_apples = 5, num_peaches = 7))
# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {0:5} apples and {1:3} peaches'.format(5, 7))
# 9. With f-strings and variables
apples = 5
peaches = 7
print(f'Anna has {apples} apples and {peaches} peaches')
# 10. With % operator
print('Anna has %s apples and %s peaches' % (apples, peaches))
# 11. With variable substitutions by name (hint: by using dict)
app = 6
peach = 7
data_dict = {"apples": app, "peaches": peach}
print('Anna has %(apples)s apples and %(peaches)s peaches' % data_dict)

# 12. Convert (1) to list comprehension
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)

# 13. Convert (2) to regular for with if-else
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)
# 14. Convert (3) to dict comprehension
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)

# 15. Convert (4) to dict comprehension
d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)

# 16.  Convert (5) to regular for with if
d_5 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d_5[x] = x ** 3
print(d_5)

# 17. Convert (6) to regular for with if-else
d_6 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d_6[x] = x ** 3
    else:
        d_6[x] = x
print(d_6)

# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
# 19. Convert (8) to regular function
def foo_8 (x,y, z):
    if y < x and x > z:
        return z
    else:
        return y

# 20.Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
print(sorted(lst_to_sort, reverse=True))

# 22.Use map and lambda to update the lst_to_sort by multiply each element by 2
new_lst = list(map(lambda x: x * 2, lst_to_sort))
print(new_lst)
# 23.Raise each list number to the corresponding number on another list
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(lambda x, y: x + y, list_A, list_B))
print(list_C)
# 24.Use reduce and lambda to compute the numbers of a lst_to_sort
from functools import reduce
sum = reduce(lambda a, b : a + b, lst_to_sort)
print(sum)
# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1
n_lst = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(n_lst)
# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers
b = range(-10, 10)
b_min = list(filter(lambda x: x < 0, b))
print(b_min)
# 27.Using the filter function, find the values that are common to the two lists
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_3 = list(filter(lambda x: x in list_1,list_2))
print(list_3)