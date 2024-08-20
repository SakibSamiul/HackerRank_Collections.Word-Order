from collections import Counter

n = int(input())

N = [input() for i in range(n)]

words = Counter(N)
print(len(words))
print(*Counter(words).values())