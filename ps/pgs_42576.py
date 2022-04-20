""" 완주하지 못한 선수. 해시.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42576
"""
from collections import Counter

def solution(participant, completion):
    counter = Counter(completion)
    for person in participant:
        if counter[person] == 0:
            return person
        counter[person] -= 1

if __name__ == "__main__":
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    answer = "vinko"
    result = solution(participant, completion)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: vinko
    result: vinko
    비교: True
    """