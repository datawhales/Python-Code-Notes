""" Sorting algorithms.
    1. Selection Sort.
    2. Insertion Sort.
    3. Merge Sort.
    4. Quick Sort.
"""
def selection_sort(L):
    for i in range(len(L)):
        smallest = i
        for j in range(i + 1, len(L)):
            if L[j] < L[smallest]:
                smallest = j
        L[i], L[smallest] = L[smallest], L[i]
    return L

def insertion_sort(L):
    for i in range(1, len(L)):
        for j in range(i, 0, -1):
            if L[j] < L[j-1]:
                L[j-1], L[j] = L[j], L[j-1]
            else:
                break
    return L

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i == len(left): result += right[j:len(right)]
    if j == len(right): result += left[i:len(left)]
    return result

def merge_sort(L):
    if len(L) <= 1: return L
    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)

def quick_sort_1(L, start, end):
    if start >= end: return
    pivot = start
    left, right = start + 1, end
    while left <= right:
        while left <= end and L[left] <= L[pivot]:
            left += 1
        while right > start and L[right] >= L[pivot]:
            right -= 1
        # 엇갈렸다면, right와 pivot swap
        if left > right:
            L[right], L[pivot] = L[pivot], L[right]
        else:
            L[left], L[right] = L[right], L[left]
    quick_sort_1(L, start, right-1)
    quick_sort_1(L, right+1, end)

def quick_sort_2(L):
    if len(L) <= 1: return L
    pivot_idx = len(L) // 2
    pivot = L[pivot_idx]
    remain = L[:pivot_idx] + L[pivot_idx+1:]
    left = [x for x in remain if x <= pivot]
    right = [x for x in remain if x > pivot]
    return quick_sort_2(left) + [pivot] + quick_sort_2(right)

