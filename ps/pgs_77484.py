""" 로또의 최고 순위와 최저 순위.
    Link: https://programmers.co.kr/learn/courses/30/lessons/77484
"""
def solution(lottos, win_nums):
    result = 0
    array = [0] * 46
    for num in lottos:
        array[num] += 1
    for win_num in win_nums:
        result += array[win_num]
    answer = [result + array[0], result]
    answer = [7 - x if x != 0 else 6 for x in answer]
    return answer

if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    answer = [3, 5]
    result = solution(lottos, win_nums)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [3, 5]
    result: [3, 5]
    비교: True
    """