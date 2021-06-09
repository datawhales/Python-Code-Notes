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

# quick sort 3
def pivot_select(L, start, end):
    mid = (start + end) // 2
    if L[start] > L[mid]:
        L[start], L[mid] = L[mid], L[start]
    if L[start] > L[end]:
        L[start], L[end] = L[end], L[start]
    if L[mid] > L[end]:
        L[mid], L[end] = L[end], L[mid]
    return mid

def partitioning(L, pivot_idx):
    pivot = L[pivot_idx]
    left, right = 0, len(L)-1
    while left < right:
        while left < len(L) and L[left] <= pivot:
            left += 1
        while right >= 0 and L[right] >= pivot:
            right -= 1
        if left < right:
            L[left], L[right] = L[right], L[left]
    if pivot_idx < left:
        left -= 1
    L[pivot_idx], L[left] = L[left], L[pivot_idx]
    return left

def partition_sort(L, start, end):
    if start < end:
        pivot_idx = pivot_select(L, start, end)
        pivot_idx = partitioning(L, pivot_idx)
        partition_sort(L, start, pivot_idx-1)
        partition_sort(L, pivot_idx+1, end)

def quick_sort(L):
    partition_sort(L, 0, len(L)-1)