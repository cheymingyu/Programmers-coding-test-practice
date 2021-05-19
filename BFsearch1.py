# 수포자

import numpy as np

def solution(answers):
    n = len(answers)
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4 ,2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a = len(p1)
    b = len(p2)
    c = len(p3)
    if n <= 5:
        p1 = p1[:n]
        p2 = p2[:n]
        p3 = p3[:n]
    else:
        for _ in range(n//a):
            if a >= n:
                break
            p1.extend([1, 2, 3, 4, 5])
        for _ in range(n//b):
            if b >= n:
                break
            p2.extend([2, 1, 2, 3, 2, 4 ,2, 5])
        for _ in range(n//c):
            if c >= n:
                break
            p3.extend([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
        
    answ_p1 = 0
    answ_p2 = 0
    answ_p3 = 0
    
    for i in range(len(p1)%n):
        if len(p1) != n:
            p1.pop()
            
    for i in range(len(p2)%n):
        if len(p2) != n:
            p2.pop()
            
    for i in range(len(p3)%n):
        if len(p3) != n:
            p3.pop()
            
    answers = np.array(answers)
    p1 = np.array(p1)
    p2 = np.array(p2)
    p3 = np.array(p3)
    p1 = answers - p1
    p2 = answers - p2
    p3 = answers - p3
    
    answ_p1 = np.sum(p1 == 0)
    answ_p2 = np.sum(p2 == 0)
    answ_p3 = np.sum(p3 == 0)
    
    # for i in range(n):
    #     if answers[i] == p1[i]:
    #         answ_p1 += 1
    #     if answers[i] == p2[i]:
    #         answ_p2 += 1
    #     if answers[i] == p3[i]:
    #         answ_p3 += 1
    
    max_score = max(answ_p1, answ_p2, answ_p3)
    
    answer = []
    
    if answ_p1 == max_score:
        answer.append(1)
    if answ_p2 == max_score:
        answer.append(2)
    if answ_p3 == max_score:
        answer.append(3)
    
    return answer


solution([1,2,3,4,5])