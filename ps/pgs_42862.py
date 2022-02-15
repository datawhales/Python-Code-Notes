""" 체육복.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42862
"""
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # used: 사용된 여분
    used = set([x for x in lost if x in reserve])
    # 본인의 여분을 사용하는 사람 제외하고 남은 학생
    lost = [x for x in lost if x not in reserve]
    lost_cnt = len(lost)
    for i in lost:
        if i-1 in reserve and i-1 not in used:
            used.add(i-1)
            lost_cnt -= 1
        elif i+1 in reserve and i+1 not in used:
            used.add(i+1)
            lost_cnt -= 1
        
    return n - lost_cnt

if __name__ == "__main__":
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    answer = 5
    result = solution(n ,lost, reserve)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 5
    result: 5
    비교: True
    """