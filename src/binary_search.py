""" Binary Search algorithm + bisect Library.
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

from bisect import bisect_left, bisect_right

def count_by_range(L, left_value, right_value):
    """ 정렬된 리스트에서 값이 특정 범위에 속하는
        원소의 개수를 구하는 함수.

        Arguments:
            L: 정렬된 리스트.
            left_value: 범위에서의 최소값.
            right_value: 범위에서의 최대값.

        Return:
            값이 [left_value, right_value]에 속하는 데이터의 수를 반환
    """
    left_idx = bisect_left(L, left_value)
    right_idx = bisect_right(L, right_value)
    return right_idx - left_idx

if __name__ == "__main__":
    L = [-7, -6, -2, 0, 3, 4, 4, 5, 7, 9, 50, 100]
    trg = 9
    # 리스트 L에서 trg가 첫 번째로 나타나는 인덱스를 찾음
    print(binary_search(L, trg))
    # 리스트 L에 trg를 삽입하려 할 때 가장 왼쪽 인덱스를 찾음
    print(bisect_left(L, trg))
    # 리스트 L에 trg를 삽입하려 할 때 가장 오른쪽 인덱스를 찾음
    print(bisect_right(L, trg))

    # 값이 [0, 5] 범위에 있는 데이터의 개수 출력
    print(count_by_range(L, 0, 5))