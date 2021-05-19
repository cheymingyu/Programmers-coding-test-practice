def solution(clothes):
    closet = {}
    tmp = []

    for i in clothes:
        name, kind = i
        if kind in closet:
            closet[kind].append(name)
        else:
            closet[kind] = [name]
    
    for key in closet.keys():
        tmp.append(len(closet[key]))

    total = 1
    for i in tmp:
        total *= i+1

    answer = total-1
    return answer

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])