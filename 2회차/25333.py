import math
from collections import deque
_a = deque(input().split())
b = _a.popleft()
a = [x for x in map(int, _a)]
# print (a)

c = [x for x in map(lambda x : (a[x * 3], a[x * 3 + 1], a[x * 3 + 2]), range(len(a) // 3))]
# print("c: ",c)

answer = []
for x, y, z in c :
    gcd = math.gcd(x, y)
    answer.append(z // gcd)
print(*answer)