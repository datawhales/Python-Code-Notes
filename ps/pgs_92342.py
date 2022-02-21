""" 양궁대회. (미완성)
    Link: https://programmers.co.kr/learn/courses/30/lessons/92342
"""
def convert(n):
    string = bin(n)[2:]
    string = '0' * (11 - len(string)) + string
    return [int(x) for x in string]

def solution(n, info):
    zero_score = sum((10 - i) for i in range(len(info)) if info[i] >= 1)
    score_list = [2 * (10 - i) if info[i] >= 1 else 10 - i for i in range(len(info))]
    possible = [x+1 for x in info]

    answer_list = []
    answer_score = []
    for i in range(2048):
        true_list = convert(i)
        answer_cand = [t * p for t, p in zip(true_list, possible)]
        if n == sum(answer_cand):
            answer_list.append(answer_cand)
            answer_score.append(sum(score_list[i] for i in range(len(score_list)) if answer_cand[i] >= 1))
    
    final_list = []
    if max(answer_score) > zero_score:
        max_index = [i for i in range(len(answer_score)) if answer_score[i] == max(answer_score)]
        final_list = [answer_list[i] for i in max_index]
        final_list.sort(key=lambda x: (x[10], x[9], x[8],
                                       x[7], x[6], x[5], x[4],
                                       x[3], x[2], x[1], x[0]), reverse=True)
        return final_list[0]
    else:
        return [-1]
    

if __name__ == "__main__":
    n = 9
    info = [0,0,1,2,0,1,1,1,1,1,1]
    answer = [1,1,2,0,1,2,2,0,0,0,0]
    result = solution(n, info)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: [0,2,2,0,1,0,0,0,0,0,0]
    result: [0,2,2,0,1,0,0,0,0,0,0]
    비교: True
    """
