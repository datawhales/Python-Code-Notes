""" 베스트앨범. 해시.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42579
"""
from collections import defaultdict

def solution(genres, plays):
    ret = []
    hash_table = defaultdict(list)
    genre_order = {}
    
    # {'classic': [(0, 500), (2, 150), (3, 800)],
    #  'pop': [(1, 600), (4, 2500)]}
    for i, (genre, num) in enumerate(zip(genres, plays)):
        hash_table[genre].append((i, num))
    
    for genre in hash_table:
        hash_table[genre].sort(key=lambda x: x[1], reverse=True)
        genre_order[genre] = sum([num for idx, num in hash_table[genre]])
    
    genre_order = sorted(genre_order.items(), key=lambda x: x[1], reverse=True)
    
    for genre, genre_sum in genre_order:
        ret += [x[0] for x in hash_table[genre][:2]]
    
    return ret

def solution_2(genres, plays):
    ret = []
    hash_map = defaultdict(dict)
    
    # {'classic': {0: 500, 2: 150, 3: 800},
    # 'pop': {1: 600, 4: 2500}}
    for i, genre in enumerate(genres):
        hash_map[genre][i] = plays[i]
    
    genre_order = sorted(hash_map.items(), key=lambda x: -sum(num for idx, num in x[1].items()))
    
    for genre, _ in genre_order:
        ret += [i for i, num in sorted(hash_map[genre].items(), key=lambda x: -x[1])[:2]]
    return ret

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    answer = [4, 1, 3, 0]
    result = solution(genres, plays)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [4, 1, 3, 0]
    result: [4, 1, 3, 0]
    비교: True
    """