def solution(phone_book):
    answer = True
    finish = False
    
    phone_book = sorted(phone_book, key=len)
    for i in range(len(phone_book)):
        if finish:
            break
        current = phone_book[i]
        for j in range(i+1, len(phone_book)):
            if len(current) < len(phone_book[j]) and current == phone_book[j][:len(current)]:
                answer = False
                finish = True
                break
            
    return answer

solution(["119", "97674223", "1195524421"])