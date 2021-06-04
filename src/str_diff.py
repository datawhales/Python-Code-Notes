""" 길이가 같은 두 문자열에 대해 문자가 서로 다른 위치의 개수를 반환하는 함수.

    ex) 'box'와 'fox'는 'b'와 'f'만 다르므로 1을 return.
"""
def str_diff(s1, s2):
    return sum([1 if s1[i] != s2[i] else 0 for i in range(len(s1))])

if __name__ == "__main__":
    s1, s2 = 'box', 'fox'
    print(str_diff(s1, s2))