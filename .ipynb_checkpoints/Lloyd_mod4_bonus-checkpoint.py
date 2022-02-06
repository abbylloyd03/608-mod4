Lloyd_mod4_bonus.py
"""   """

with open('olympics.txt') as f:
    contents = f.read()
    
words_counts = {}

# count occurences of each unique word
for word in contents.split():
    if word in words_counts:
        words_counts[word] += 1 # update existing key-value pair
    else:
        words_counts[word] = 1 # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(words_counts.items()):
    print(f'{word:<12}{count}')
    
print('\nNumber of unique words:', len(words_counts))

    
