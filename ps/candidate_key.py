""" 후보키. 문자열.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42890
"""

from itertools import combinations

def check_unique(relation, keys):
    # keys = (1,2))와 같은 형태로 key 인덱스가 주어졌을 때 유일성을 만족하는지 확인
    new_data = [' '.join(list(data[i] for i in keys)) for data in relation]
    return len(set(new_data)) == len(relation)

def check_minimality(keys):
    # keys = [(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]
    # 와 같은 형태로 주어졌을 때 최소성을 만족하는 key만을 남기는 함수
    new_keys = []
    for key in keys:
        if len(key) == 1:
            new_keys.append(key)
            continue
        if not any([set(final_key).issubset(key) for final_key in new_keys]):
            new_keys.append(key)
    return new_keys

def solution(relation):
    keys = []
    for i in range(1, len(relation[0]) + 1):
        for comb in combinations(range(len(relation[0])), i):
            if check_unique(relation, comb):
                keys.append(comb)
    final_keys = check_minimality(keys)
    return len(final_keys)

if __name__ == "__main__":
    relation = [["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]
    answer = 2
    result = solution(relation)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """