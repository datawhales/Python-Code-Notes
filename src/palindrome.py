""" palindrome substring 관련 문제에서 활용 가능한 코드.
"""
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

ret = ''
s = 'babad'
for i in range(len(s) - 1):
    ret = max(ret, expand(s, i, i), expand(s, i, i+1), key=len)

print(ret)

def expand(s, left, right, cnt):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        cnt += 1
        left -= 1
        right += 1
    return cnt

cnt = 0
for i in range(len(s)):
    cnt = expand(s, i, i, cnt)

for i in range(len(s)-1):
    cnt = expand(s, i, i+1, cnt)
    
print(cnt)