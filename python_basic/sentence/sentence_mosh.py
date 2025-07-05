from pprint import pprint

sentence = "This is a common interview question people get when they go for a interview at a big tech company. A company common use a question"

words = sentence.split()

char_freuency = {}
for char in words:
    if char in char_freuency:
        char_freuency[char] += 1
    else:
        char_freuency[char] = 1

char_freuency_sorted = sorted(
    char_freuency.items(),
    key=lambda kv: kv[1],
    reverse=True)
pprint(char_freuency_sorted[0])
