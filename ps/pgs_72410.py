""" 신규 아이디 추천. 정규표현식 이용.
    Link: https://programmers.co.kr/learn/courses/30/lessons/72410
"""
def solution(new_id):
    import re
    # step 1
    new_id = new_id.lower()
    # step 2
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    # step 3
    new_id = re.sub(r'\.+', '.', new_id)
    # step 4
    new_id = re.sub('^\.', '', new_id)
    new_id = re.sub('\.$', '', new_id)
    # step 5
    if not new_id:
        new_id = 'a'
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub('\.$', '', new_id)
    # step 7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    return new_id
if __name__ == "__main__":
    new_id = "...!@BaT#*..y.abcdefghijklm"
    answer = "bat.y.abcdefghi"
    result = solution(new_id)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: bat.y.abcdefghi
    result: bat.y.abcdefghi
    비교: True
    """