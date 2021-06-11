""" 소수인지 판별하는 함수 구현,
    소인수분해 함수 구현.
"""
def is_prime(num):
    """ 소수이면 True,
        소수가 아니면 False 반환.
    """
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

if __name__ == "__main__":
    num_list = [7, 13, 24, 70]
    for num in num_list:
        print(f"num: {num}, is_prime? {is_prime(num)}")
        print(f"num: {num}, factorization: {prime_factorization(num)}")
        print('')
        
    """
    num: 7, is_prime? True
    num: 7, factorization: [(7, 1)]

    num: 13, is_prime? True
    num: 13, factorization: [(13, 1)]

    num: 24, is_prime? False
    num: 24, factorization: [(2, 3), (3, 1)]

    num: 70, is_prime? False
    num: 70, factorization: [(2, 1), (5, 1), (7, 1)]
    """