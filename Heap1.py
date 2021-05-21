import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        if scoville[0] >= K:
            break;
        if len(scoville) <= 1:
            answer = -1
            break;
        new_s = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, new_s)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
