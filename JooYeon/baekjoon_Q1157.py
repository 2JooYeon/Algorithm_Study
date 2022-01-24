from collections import Counter

words = list(input().upper())
count = Counter(words)
s_count = list(sorted(count.items(), key = lambda x:x[1]))
a_w, a_c = s_count.pop()
del count[a_w]
if a_c in list(count.values()):
    print('?')
else:
    print(a_w)
