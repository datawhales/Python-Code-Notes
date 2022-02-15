""" 숫자 문자열과 영단어. 
    Link: https://programmers.co.kr/learn/courses/30/lessons/81301
"""
def solution(s):
    import re
    patterns = {'zero': '0', 'one': '1', 'two': '2',
                'three': '3', 'four': '4', 'five': '5',
                'six': '6', 'seven': '7', 'eight': '8',
                'nine': '9'}
    for p in patterns:
        s = re.sub(p, patterns[p], s)
    return int(s)

if __name__ == "__main__":
    s = "one4seveneight"
    answer = 1478
    result = solution(s)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 1478
    result: 1478
    비교: True
    """