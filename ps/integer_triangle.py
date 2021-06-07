""" 정수 삼각형.
    Link: https://programmers.co.kr/learn/courses/30/lessons/43105
"""
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif i == j:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])

if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    answer = 30
    result = solution(triangle)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
    
    """
    answer: 30
    result: 30
    비교: True
    """