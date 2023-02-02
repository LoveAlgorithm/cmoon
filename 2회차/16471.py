from collections import deque
a = input().split()
b = int(a[0])
del a[0]
c = deque(sorted([a[x] for x in range(b)], reverse=True))
#print(c)
d = deque(sorted([a[x + b] for x in range(b)], reverse=True))
#print(d)
goal = (b + 1) / 2
count = 0
for i in range(b) :
    if c[0] < d[0] :
        d.popleft()
        count += 1
    c.popleft()
# print(count, goal)
print("YES" if count >= goal else "NO")