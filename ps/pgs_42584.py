""" 주식가격. 스택/큐.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42584
"""
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        cur = queue.popleft()
        tmp = 0
        for price in queue:
            if cur <= price:
                tmp += 1
            else:
                tmp += 1
                break
        answer.append(tmp)
    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    answer = [4, 3, 1, 1, 0]
    result = solution(prices)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [4, 3, 1, 1, 0]
    result: [4, 3, 1, 1, 0]
    비교: True
    """