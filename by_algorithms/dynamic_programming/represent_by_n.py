""" N으로 표현. DP.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42895
"""
def solution(N, number):
    dp = []
    for i in range(1, 9):
        case = []
        case.append(int(str(N) * i))
        for j in range(1, i):
            k = i - j
            for n1 in dp[j-1]:
                for n2 in dp[k-1]:
                    case.append(n1 + n2)
                    case.append(n1 - n2)
                    case.append(n1 * n2)
                    if n2 != 0:
                        case.append(n1 // n2)
        dp.append(list(set(case)))

        if number in dp[i-1]:
            return i
    return -1

if __name__ == "__main__":
    N = 5
    number = 12
    answer = 4
    result = solution(N, number)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 4
    result: 4
    비교: True
    """