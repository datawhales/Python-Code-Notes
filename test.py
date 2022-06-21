def binary_search(L, trg):
    start, end = 0, len(L) - 1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] <= trg:
            start = mid + 1
        else:
            end = mid -1
    if start < len(L):
        return start
    else:
        return -1 


L = [1,4,8,10,11,11,11,11,14,14,17]
trg = 18

print(binary_search(L, trg))

from bisect import bisect_left, bisect_right

print(bisect_left(L, trg))

print(bisect_right(L, trg))
