""" 입국심사. Binary Search.
    Link: https://programmers.co.kr/learn/courses/30/lessons/43238
"""
def solution(n, times):
    times.sort()
    min_t, max_t = times[0], times[-1]
    min_predicted, max_predicted = min_t * n // len(times), max_t * n // len(times)
    start, end = 0, max_predicted - min_predicted
    while start <= end:
        mid = (start + end) // 2
        pred = min_predicted + mid
        if sum([pred // x for x in times]) >= n:
            end = mid - 1
        else:
            start = mid + 1
    return min_predicted + start

if __name__ == "__main__":
    n = 6
    times = [7, 10]
    answer = 28
    result = solution(n, times)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 28
    result: 28
    비교: True
    """