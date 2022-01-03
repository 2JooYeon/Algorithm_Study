lst = []

score = 0

for _ in range(10):
    lst.append(int(input()))

for i in lst:
    score += i
    if score >= 100:
        if score - 100 > 100 - (score - i):
            score -= i
        break
    
print(score)