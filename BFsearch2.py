from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    
    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    
    return True
    

def solution(numbers):
    answer = []
    num = list(numbers)
        
    for i in range(1, len(num)+1):
        cand_list = list(map(''.join, permutations(num, i)))
        for j in list(set(cand_list)):
            if check(int(j)):
                answer.append(int(j))
        
    answer = list(set(answer))
    return len(answer)

    