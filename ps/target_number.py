""" 타겟 넘버. Recursion.
    Link: https://programmers.co.kr/learn/courses/30/lessons/43165
"""
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    return solution(numbers[:-1], target - numbers[-1]) + solution(numbers[:-1], target + numbers[-1])

if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    answer = 5
    result = solution(numbers, target)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 5
    result: 5
    비교: True
    """