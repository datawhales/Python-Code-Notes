""" 전화번호 목록. 해시.
    Link: https://programmers.co.kr/learn/courses/30/lessons/42577
"""
def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True

def solution_2(phone_book):
    hash_table = {}
    for number in phone_book:
        hash_table[number] = 1
    for number in phone_book:
        tmp = ''
        for char in number:
            tmp += char
            if tmp in hash_table and tmp != number:
                return False
    return True

if __name__ == "__main__":
    phone_book = ["119", "97674223", "1195524421"]
    answer = False
    result = solution(phone_book)
    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: False
    result: False
    비교: True
    """