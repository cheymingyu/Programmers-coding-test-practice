# 기능개발

def solution(progresses, speeds):
    progresses.reverse()
    speeds.reverse()
    
    answer = []

    while len(speeds) != 0:
        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
        count = 0
        for _ in range(len(progresses)):
            if progresses[-1] >= 100:
                progresses.pop()
                count += 1
            else:
                break;
        if count != 0:
            answer.append(count)
        speeds = speeds[:len(progresses)]

    return answer

solution([93, 30, 55], [1, 30, 5])