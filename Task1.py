sub = {}
file = open('task1.txt', 'r')
content = file.readlines()
file.close()
for i in range(0, len(content), 2):
    content[i] = content[i].replace("\n", "")
    content[i + 1] = content[i + 1].replace("\n", "")
    sub.update({content[i]: content[i + 1]})
print(sub)

with open('task1_2.txt', 'w') as file:
    for item in sub.values():
        file.write(f'{item} ')

