""" 위장. 해시.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42578
"""
def solution(clothes):
    clothes_map = {}
    answer = 1
    for name, category in clothes:
        if category not in clothes_map:
            clothes_map[category] = 1
            continue
        clothes_map[category] += 1
    for num in clothes_map.values():
        answer *= num + 1
    return answer - 1

if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    answer = 5
    result = solution(clothes)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 5
    result: 5
    비교: True
    """