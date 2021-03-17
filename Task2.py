import pickle

file = open('task2', 'rb')
list_1 = pickle.loads(file.read())
print(list_1)
file.close()

sum_list = 0
for i in range(len(list_1)):
    sum_list += list_1[i]

print(f'SUM = {sum_list}')
print(f'Average = {sum_list / len(list_1)}')