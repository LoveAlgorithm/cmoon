from copy import deepcopy

a = input().split()
T = a[0]
del a[0]

# print(a)
lst = []
tmp = []
sub_tmp1 = []
sub_tmp2 = []
for x in a :
    if '0' < x < '9' :
        tmp.append(sub_tmp1)
        tmp.append(sub_tmp2)
        lst.append(deepcopy(tmp))
        sub_tmp1.clear()
        sub_tmp2.clear()
        tmp.clear()
        sub_tmp1.append(x)
    else :
        sub_tmp2.append(x)
del lst[0]
# print(lst)

def word_sort(str1, str2) :
    a = len(str1)
    b = len(str2)
    k = min(a, b)
    for i in range(k) :
        if str1[i] == str2[i] :
            continue
        else :
            if str1[i] == '-' :
                return 1
            if str2[i] == '-' :
                return 0
            if str1[i] <= str2[i] :
                return 0
            return 1
    if k == a :
        return 0
    else : 
        return 1
    return 0
    
for n, words in lst :
    k = int(n[0])
    for i in range(k - 1) :
        for j in range(i + 1, k) :
            if word_sort(words[i], words[j]) :
                tmp = words[i]
                words[i] = words[j]
                words[j] = tmp
                
                
# print(lst)
for row in lst :
    print(*row[1], end=" ")