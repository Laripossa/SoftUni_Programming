current_word = input()
index_list = []

for index in range(len(current_word)):
    if current_word[index].isupper():
        index_list.append(index)

print(index_list)
