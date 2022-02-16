""" k진수에서 소수 개수 구하기.
    Link: https://programmers.co.kr/learn/courses/30/lessons/92335
"""
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def convert_k(n: int, k: int) -> str:
    answer = ''
    while n:
        answer += str(n % k)
        n //= k
    return answer[::-1]

def solution(n, k):
    num_string = convert_k(n, k)
    num_list = num_string.split('0')
    num_list = [int(x) for x in num_list if x != '']
    return sum(map(is_prime, num_list))

if __name__ == "__main__":
    n = 437674
    k = 3
    answer = 3
    result = solution(n, k)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 3
    result: 3
    비교: True
    """
