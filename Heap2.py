import heapq

def solution(jobs):
    answer = 0
    heap = []
    start = -1
    now = 0

    for _ in range(len(jobs)):
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
    
    return int(answer/len(jobs))
        

print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))
