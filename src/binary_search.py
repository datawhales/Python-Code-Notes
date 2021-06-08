""" Binary Search algorithm.
    정렬된 리스트에 대해서 사용 가능.
"""
def binary_search(L, trg):
    start, end = 0, len(L) - 1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] < trg:
            start = mid + 1
        else:
            end = mid - 1
    if start < len(L) and L[start] == trg:
        return start
    else:
        return -1

if __name__ == "__main__":
    L = [-7, -6, -2, 0, 3, 4, 4, 5, 7, 9, 50, 100]
    trg = 9
    print(binary_search(L, trg))