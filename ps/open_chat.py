""" 오픈채팅방. 문자열.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42888
"""

def solution(record):
    answer = []
    nickname = dict()
    # userID별로 닉네임 저장
    for r in record:
        data = r.split()
        if data[0] != 'Leave':
            nickname[data[1]] = data[2]
    # 저장된 닉네임 이용하여 출력
    for r in record:
        data = r.split()
        if data[0] == 'Enter':
            answer.append(f"{nickname[data[1]]}님이 들어왔습니다.")
        elif data[0] == 'Leave':
            answer.append(f"{nickname[data[1]]}님이 나갔습니다.")

    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan"]
    answer = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    result = solution(record)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    result: ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    비교: True
    """