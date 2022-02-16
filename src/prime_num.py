""" 1. is_prime(num: int) -> bool
        소수인지 판별하는 함수 구현,
    2. prime_factorization(num: int) -> List
        소인수분해 함수 구현.
    3. get_all_primes(num: int) -> None
        1부터 N까지의 모든 소수를 출력하는 함수 구현.
"""
def is_prime(num):
    """ 소수이면 True,
        소수가 아니면 False 반환.
    """
    if num <= 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factorization(num):
    """ 소인수분해하여 tuple 형태로 표현.

        Ex) 24 = 2^3 * 3 -> [(2, 3), (3, 1)] return.
    """
    result = []
    p = 2
    while num > 1:
        cnt = 0
        while num % p == 0:
            num /= p
            cnt += 1
        if cnt >= 1:
            result.append((p, cnt))
        p += 1
    return result

def get_all_primes(num):
    """ 에라토스테네스의 체 알고리즘 이용하여,
        1부터 N까지의 모든 소수를 출력하는 함수.
    """
    import math
    # num까지의 숫자가 각각 소수인지를 나타내고 있는 리스트
    result = [True for _ in range(num + 1)]
    for i in range(2, int(math.sqrt(num)) + 1):
        # i가 소수인 경우
        if result[i]:
            j = 2
            while i * j <= num:
                result[i * j] = False
                j += 1
    for i in range(2, num + 1):
        if result[i]:
            print(i, end=' ')

if __name__ == "__main__":
    num_list = [7, 13, 24, 70, 100]
    for num in num_list:
        print(f"num: {num}, is_prime? {is_prime(num)}")
        print(f"num: {num}, factorization: {prime_factorization(num)}")
        print('')

    print(f"{num_list[-1]}까지의 모든 소수는,")
    get_all_primes(num_list[-1])

    """
    num: 7, is_prime? True
    num: 7, factorization: [(7, 1)]

    num: 13, is_prime? True
    num: 13, factorization: [(13, 1)]

    num: 24, is_prime? False
    num: 24, factorization: [(2, 3), (3, 1)]

    num: 70, is_prime? False
    num: 70, factorization: [(2, 1), (5, 1), (7, 1)]

    num: 100, is_prime? False
    num: 100, factorization: [(2, 2), (5, 2)]

    100까지의 모든 소수는,
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97     
    """