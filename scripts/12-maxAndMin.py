l = []

for x in input().split():
    l.append(int(x))
l.sort()

print(min(l))
print(max(l))
