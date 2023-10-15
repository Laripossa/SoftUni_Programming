input_word = input()

target_words = ["sand", "water", "fish", "sun"]
counter = 0

for word in target_words:
    count = input_word.lower().count(word)
    counter += count

print(counter)

