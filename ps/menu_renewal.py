""" 메뉴 리뉴얼.
    Link: https://programmers.co.kr/learn/courses/30/lessons/72411
"""
def solution(orders, course):
    from collections import Counter
    from itertools import combinations
    answer = []
    counter = Counter()
    for num in course:
        for order in orders:
            menu_list = [menu for menu in order]
            menu_list.sort()
            combination_list = list(combinations(menu_list, num))
            counter += Counter(combination_list)
        sorted_counter = sorted(counter.items(), key=lambda x: -x[1])
        idx = 0
        while idx < len(sorted_counter) and sorted_counter[idx][1] == sorted_counter[0][1]:
            if sorted_counter[idx][1] >= 2:
                answer.append(sorted_counter[idx])
            idx += 1
        counter = Counter()
    answer = [tup[0] for tup in answer]
    answer = [''.join(tup) for tup in answer]
    answer = sorted(answer)
    return answer

if __name__ == "__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2, 3, 4]
    result = ["AC", "ACDE", "BCFG", "CDE"]
    ret = solution(orders, course)
    print(f"return: {ret}\nresult: {result}\n비교: {ret == result}")
   
    """
    return: ['AC', 'ACDE', 'BCFG', 'CDE']
    result: ['AC', 'ACDE', 'BCFG', 'CDE']
    비교: True
    """