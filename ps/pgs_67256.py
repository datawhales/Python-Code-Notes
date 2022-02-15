""" 키패드 누르기.
    Link: https://programmers.co.kr/learn/courses/30/lessons/67256
"""
def solution(numbers, hand):
    phone_map = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 ['*', 0, '#']]
    num_map = {phone_map[i][j]: (i, j) for i in range(len(phone_map)) for j in range(len(phone_map[0]))}
    
    answer = ''
    left, right = '*', '#'

    def distance(a, b):
        return abs(num_map[a][0] - num_map[b][0]) + abs(num_map[a][1] - num_map[b][1])
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            if distance(left, num) < distance(right, num):
                answer += 'L'
                left = num
            elif distance(left, num) > distance(right, num):
                answer += 'R'
                right = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num
    
    return answer

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    answer = "LRLLLRLLRRL"
    result = solution(numbers, hand)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: LRLLLRLLRRL
    result: LRLLLRLLRRL
    비교: True
    """