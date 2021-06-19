""" 이진법 변환 함수 구현.
    파이썬의 내장 함수 bin()으로도 해결 가능.
"""
def binary(n):
    answer = ''
    while n:
        answer += str(n % 2)
        n = n // 2
    return answer[::-1]

def binary_2(n):
    return bin(n)[2:]

if __name__ == "__main__":
    n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for n in n_list:
        print(f'n: {n}, binary_n: {binary(n), binary_2(n)}')
    
    """
    n: 1, binary_n: ('1', '1')
    n: 2, binary_n: ('10', '10')
    n: 3, binary_n: ('11', '11')
    n: 4, binary_n: ('100', '100')
    n: 5, binary_n: ('101', '101')
    n: 6, binary_n: ('110', '110')
    n: 7, binary_n: ('111', '111')
    n: 8, binary_n: ('1000', '1000')
    n: 9, binary_n: ('1001', '1001')
    n: 10, binary_n: ('1010', '1010')
    """