def solution(priorities, location):
    seq = [i for i in range(len(priorities))]
    order = []
    
    while priorities:
        tmp = 0
        if priorities[0] == max(priorities):
            priorities.pop(0)
            tmp = seq.pop(0)
            order.append(tmp)
            if tmp == location:
                break
        else:
            priorities.append(priorities.pop(0))
            seq.append(seq.pop(0))
    

    answer = len(order)
    return answer

solution([1, 1, 9, 1, 1, 1]	, 0)