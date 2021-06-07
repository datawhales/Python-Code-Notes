""" DP를 이용하여 푸는 문제 예시.
    거쳐간 숫자의 합 최대값 구하기, 최단 경로 개수 구하기 등.
    가장자리를 먼저 -> 이후 나머지.
"""
def path(m, n, puddles):
    """ 가는 길에 웅덩이가 존재할 때 최단 경로 개수 구하는 함수.

        구현 방식:
            1. 웅덩이의 좌표에 0으로 표시.
            2. 가장자리부터 채우기.
            3. 조건에 맞게 나머지 전부 채우기.
    """
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
    return answer[-1][-1]