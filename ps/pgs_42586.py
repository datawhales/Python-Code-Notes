""" 기능개발. 스택/큐.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42586
"""
def solution(progresses, speeds):
    from collections import deque
    import math

    process_time = [math.ceil((100 - x) / y)
                    for x, y in zip(progresses, speeds)]

    queue = deque(process_time)
    max_num, cnt = process_time[0], 0
    result = []

    while queue:
        x = queue.popleft()
        if x > max_num:
            result.append(cnt)
            max_num = x
            cnt = 1
        else:
            cnt += 1
    result.append(cnt)

    return result


if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    answer = [2, 1]
    result = solution(progresses, speeds)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [2, 1]
    result: [2, 1]
    비교: True
    """