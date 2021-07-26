""" 가장 큰 수. Sorting.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42746
"""

from functools import cmp_to_key

def compare_func(str1, str2):
    # str1 > str2인 경우 str2 -> str1 순서 정렬
    if str1 + str2 > str2 + str1:
        return 1
    # str1 < str2인 경우 str1 -> str2 순서 정렬
    elif str1 + str2 < str2 + str1:
        return -1
    # str1 == str2인 경우
    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare_func), reverse=True)
    return str(int(''.join(numbers)))

def solution_2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

if __name__ == "__main__":
    numbers = [3, 30, 34, 5, 9]
    answer = "9534330"
    result = solution(numbers)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
    
    """
    answer: 9534330
    result: 9534330
    비교: True
    """