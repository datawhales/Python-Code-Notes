""" 등굣길.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42898
"""
def solution(m, n, puddles):
    answer = [[1 for _ in range(n)] for _ in range(m)]
    for p_x, p_y in puddles:
        answer[p_x-1][p_y-1] = 0
    for i in range(1, m):
        if answer[i-1][0] == 0:
            answer[i][0] = 0
    for j in range(1, n):
        if answer[0][j-1] == 0:
            answer[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if answer[i][j] != 0:
                answer[i][j] = answer[i-1][j] + answer[i][j-1]
    return answer[-1][-1] % 1000000007

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]
    answer = 4
    result = solution(m, n, puddles)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
    
    """
    answer: 4
    result: 4
    비교: True
    """