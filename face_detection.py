# https://codeforces.com/problemset/problem/549/A
# face detection
n, m = input().split()
n = int(n)
m = int(m)
image = []
counter = 0
for i in range(n):
    image.append(list(input()))

# face is an 2x2 image including 'f', 'a', 'c', 'e'

if n == 1 or m == 1:
    print(counter)
    exit()

for i in range(1, m):
    for j in range(1, n):
        set1 = set([image[j - 1][i - 1], image[j - 1][i], image[j][i - 1], image[j][i]])
        set2 = set(["f", "a", "c", "e"])
        if set1 == set2:
            counter += 1
print(counter)
