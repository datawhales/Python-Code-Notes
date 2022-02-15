""" 신고 결과 받기.
    Link: https://programmers.co.kr/learn/courses/30/lessons/92334
"""
def solution(id_list, report, k):
    from collections import Counter
    report = list(set(report))
    count = Counter([x.split()[1] for x in report])
    ban_ids = []
    for id in id_list:
        if count[id] >= k:
            ban_ids.append(id)
    true_report = [x for x in report if x.split()[1] in ban_ids]
    result_dict = {id: 0 for id in id_list}
    for t in true_report:
        result_dict[t.split()[0]] += 1
    return list(result_dict.values())

def solution_2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1
    
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

if __name__ == "__main__":
    id_list = ['muzi', 'frodo', 'apeach', 'neo']
    report = ['muzi frodo', 'apeach frodo', 'frodo neo',
              'muzi neo', 'apeach muzi']
    k = 2
    answer = [2, 1, 1, 0]
    result = solution(id_list, report, k)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [2, 1, 1, 0]
    result: [2, 1, 1, 0]
    비교: True
    """