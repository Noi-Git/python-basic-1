sentence = "This is a common interview question people get when they go for a interview at a big tech company. A company common use a question"
words = sentence.split() #split into a list
# print('---', words)
count = dict()

# for word in range(len(words)):
for word in words:

  if count.get(word): # you can do if word in words
    count[word] += 1
  else:
    count[word] = 1

# sorted_words = sorted(count.items(), key=lambda kv: kv[1])
sorted_words = sorted(count.items(), key=lambda kv: kv[1], reverse=True)
# print(f'sorted words: {sorted_words}')

most_frequency_word = sorted_words[0]
print('---- Most frequence word ----', most_frequency_word)


