""" 거리두기 확인하기. 기타.
    Link: https://programmers.co.kr/learn/courses/30/lessons/81302
"""

from itertools import combinations

def get_position(place):
    coo = [(i, j) for i in range(len(place)) for j in range(len(place[0])) if place[i][j] == 'P']
    return coo

def check(place):
    # coo는 P의 위치
    coo = get_position(place)

    for (p1_x, p1_y), (p2_x, p2_y) in combinations(coo, 2):
        if abs(p1_x - p2_x) + abs(p1_y - p2_y) == 1:
            return 0
        elif abs(p1_x - p2_x) + abs(p1_y - p2_y) == 2:
            if p1_x == p2_x:
                if place[p1_x][min(p1_y, p2_y) + 1] != 'X':
                    return 0
            elif p1_y == p2_y:
                if place[min(p1_x, p2_x) + 1][p1_y] != 'X':
                    return 0
            # abs(p1_x - p2_x) == abs(p1_y - p2_y) == 1인 경우
            else:
                c1_x, c1_y = p1_x, p2_y
                c2_x, c2_y = p2_x, p1_y
                if place[c1_x][c1_y] != 'X' or place[c2_x][c2_y] != 'X':
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer

if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    answer = [1, 0, 1, 1, 1]
    result = solution(places)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [1, 0, 1, 1, 1]
    result: [1, 0, 1, 1, 1]
    비교: True
    """