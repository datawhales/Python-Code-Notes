""" 삼각 달팽이. 기타.
    Link: https://programmers.co.kr/learn/courses/30/lessons/68645
"""
def solution(n):
    answer = [[0] * i for i in range(1, n+1)]
    cnt = 1
    i, j = -1, 0
    for k in range(n, 0, -1):
        for _ in range(k):
            if k % 3 == n % 3:
                i += 1
            elif k % 3 == (n-1) % 3:
                j += 1
            else:
                i -= 1
                j -= 1
            answer[i][j] = cnt
            cnt += 1
    answer = [y for x in answer for y in x]
    return answer

if __name__ == "__main__":
    n = 6
    answer = [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
    result = solution(n)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
    result: [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
    비교: True
    """