""" 10진법 이하의 n진법 변환 함수 구현.
"""
def convert_to_base_k(n: int, k: int) -> str:
    answer = ''
    while n:
        answer += str(n % k)
        n //= k
    return answer[::-1]