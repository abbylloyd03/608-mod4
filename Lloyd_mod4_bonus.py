#Lloyd_mod4_bonus.py
"""Read a text file and count the words."""

with open('olympics.txt') as f:
    contents = f.read()

contents_lower = contents.lower()

words_counts = {}

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
rem_words = ['is', 'and', 'or', 'the', 'a']

for x in contents_lower:
    if x in punc:
        contents_lower = contents_lower.replace(x, '')

contents_split = contents_lower.split()

for word in contents_split:
    if word in rem_words:
       contents_split.remove(word)

# count occurences of each unique word
for word in contents_split:
    if word in words_counts:
        words_counts[word] += 1 # update existing key-value pair
    else:
        words_counts[word] = 1 # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(words_counts.items()):
    print(f'{word:<12}{count}')
    
print('\nNumber of unique words:', len(words_counts))

    
