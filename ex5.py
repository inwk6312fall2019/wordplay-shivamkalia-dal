def uses_all(word,strings):
    for letter in strings:
        if letter not in word:
            return False
    return True

fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiouy') == True:
        print(word)
        count += 1

print(count)
