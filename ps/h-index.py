""" H-Index. Sorting.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42747
"""
def solution(citations):
    citations = sorted(citations, reverse=True)
    for h in range(len(citations)):
        if citations[h] <= h:
            return h
    return len(citations)

if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    answer = 3
    result = solution(citations)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
    
    """
    answer: 3
    result: 3
    비교: True
    """