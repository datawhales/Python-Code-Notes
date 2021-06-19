""" 이진 변환 반복하기. 기타.
    Link: https://programmers.co.kr/learn/courses/30/lessons/70129
"""
def solution(s):
    cnt, total_erased = 0, 0
    while s != '1':
        total_erased += s.count('0')
        s = bin(s.count('1'))[2:]
        cnt += 1
    return [cnt, total_erased]

if __name__ == "__main__":
    s = "110010101001"
    answer = [3, 8]
    result = solution(s)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [3, 8]
    result: [3, 8]
    비교: True
    """