""" 프린터. 스택/큐.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42587
"""
from collections import deque

def solution(priorities, location):
    ret = []
    queue = deque([(i, priority) for i, priority in enumerate(priorities)])
    
    while queue:
        idx, priority = queue.popleft()
        if not queue:
            ret.append(idx)
        else:
            if priority >= max(queue, key=lambda x: x[1])[1]:
                ret.append(idx)
            else:
                queue.append((idx, priority))
                
    return ret.index(location) + 1

def solution_2(priorities, location):
    cnt = 1
    queue = deque([(i, priority) for i, priority in enumerate(priorities)])
    
    while queue:
        idx, priority = queue.popleft()
        if any(priority < q[1] for q in queue):
            queue.append((idx, priority))
        else:
            if idx == location:
                return cnt
            cnt += 1

if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    answer = 1
    result = solution(priorities, location)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 1
    result: 1
    비교: True
    """