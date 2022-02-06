#!/usr/bin/env python
# coding: utf-8

#Lloyd_mod4_bonus.py
"""Read an article from the web and count the words."""
# In[1]:


with open('olympics.txt') as f:
    contents = f.read()


# In[2]:


words_counts = {}

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
rem_words = ['is', 'and', 'or', 'the', 'a']


# In[3]:


contents_lower = contents.lower()
#print(contents_lower)


# In[4]:


for ele in contents_lower:
    if ele in punc:
        contents_lower= contents_lower.replace(ele, '')


# In[5]:


#print(contents_lower)


# In[6]:


contents_split = contents_lower.split()
#print(contents_split)


# In[7]:


for word in contents_split:
    if word in rem_words:
        contents_split.remove(word)


# In[8]:


#print(contents_split)


# In[9]:


for word in contents_split:
    if word in words_counts:
        words_counts[word] += 1 # update existing key-value pair
    else:
        words_counts[word] = 1 # insert new key-value pair


# In[10]:


#print(words_counts.items())


# In[13]:


print(f'{"COUNT":<12}WORD')

for count, word in sorted(words_counts.items(), key=lambda item: item[1], reverse=True):
    print(f'{word:<12}{count}')
    
print('\nNumber of unique words:', len(words_counts))

