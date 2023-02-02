from collections import deque
a = deque(input().split())
num_case = a.popleft()
# print(a)
lst = []
while a :
    tmp = []
    sub_tmp1 = []
    sub_tmp2 = []
    unit = int(a[0])
    for i in range(0, unit + 3) :
        if (i < 3) :
            sub_tmp1.append(a.popleft())
        else :
            sub_tmp2.append(a.popleft())
    tmp.append(sub_tmp1)
    tmp.append(sub_tmp2)
    lst.append(tmp)

# print(lst)
answer = []
for x, y in lst :
    # print(x,y)
    stack = []
    count = 0
    k = -1 * int(x[2])
    for str in y :
        tmp_str2 = str[k:]
        stack.append(tmp_str2)
        for str2 in y :
            tmp_str = str2[k:]
            if str == str2 :
                continue
            if stack and stack[-1] and stack[-1] != tmp_str :
                continue
            if stack and stack[-1] and stack[-1] == tmp_str :
                stack.pop()
                count += 1
                break
    answer.append(count)
print(*[x // 2 for x in answer])