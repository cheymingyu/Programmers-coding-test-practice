import heapq

def solution(jobs):
    answer = 0
    heap = []
    start = -1
    now = 0
    i = 0

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) == 0:
            now += 1
        else:
            cur_task = heapq.heappop(heap)
            start = now
            now += cur_task[0]
            answer += (now - cur_task[1])
            i += 1
    
    return int(answer/len(jobs))