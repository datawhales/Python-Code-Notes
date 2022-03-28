""" 소수 찾기. 완전탐색.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42839
"""
from itertools import permutations

def is_prime(num):
    if num <= 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    ret = 0
    num_list = []
    for i in range(1, len(numbers) + 1):
        num_list += list(set((permutations(numbers, i))))
    num_set = set([int(''.join(x)) for x in num_list])
    for num in num_set:
        if is_prime(num):
            ret += 1
    return ret

if __name__ == "__main__":
    numbers = "011"
    answer = 2
    result = solution(numbers)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """