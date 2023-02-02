
sp = input().split()
N =  sp[0]
_cards =  list(map(lambda x : sp[x], range(1, len(sp))))
cards = list(map(lambda x : (_cards[x * 2 - 2], _cards[x * 2 - 1]), range(1, len(_cards)//2 + 1)))
answer = []
call_time = 0
order = 1

def is_glass(x) :
    return True if x == "HOURGLASS" else False
    
def get_time(x) :
    if x <= 0 :
        return 12 - abs(x) % 12
    return x % 12
    
# print(cards)
for x, y in cards :
    # print(x, y, call_time, is_glass(x))
    tmp = [0, "NO"]
    call_time += order
    tmp[0] = get_time(call_time)
    if (is_glass(x) and get_time(call_time) == int(y)) :
        answer.append([get_time(call_time), "NO"])
        continue
    if (get_time(call_time) == int(y)) :
        tmp[1] = "YES"
    if (is_glass(x)) :
        order *= -1
    answer.append(tmp)
for x, y in answer :
    print(x, y)