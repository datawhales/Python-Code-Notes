nums = [5,7,1,4,2,3,6]

def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums


def insertion_sort(nums):

    # 5 7 1 4 2 3 6
    # 1 5 7 4 2 3 6
    # 1 4 5 7 2 3 6
    # 1 2 4 5 7 3 6
    # 1 2 3 4 5 7 6
    # 12 3 4 5 6 7

    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break
    return nums




def merge(left_part, right_part):
    # merge left part and right part
    # left: 5 7 1   right: 4 2 3 6
    
    if not left_part and not right_part:
        return []
    if not left_part:
        return right_part
    if not right_part:
        return left_part

    ret = []
    left, right = 0, 0
    while left < len(left_part) and right < len(right_part):
        # 양쪽의 포인터 위치의 숫자를 비교해서 더 작은 것을 ret에 append
        # append한 쪽의 포인터를 +1
        # 한쪽이 먼저 도달한 경우 반대 쪽 [pointer:]를 한번에 append
        if left_part[left] < right_part[right]:
            ret.append(left_part[left])
            left += 1
        elif left_part[left] > right_part[right]:
            ret.append(right_part[right])
            right += 1
        else:
            ret += [left_part[left], right_part[right]]
            left += 1
            right += 1
        
        if left == len(left_part):
            ret += right_part[right:]
            return ret
        if right == len(right_part):
            ret += left_part[left:]
            return ret
        


def merge_sort(nums):
    # 5 7 1 4 2 3 6
    
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_part, right_part = nums[:mid], nums[mid:]

    return merge(merge_sort(left_part), merge_sort(right_part))




def quick_sort(nums):
    # 5 7 1 4 2 3 6
    # pivot = 4, pivot_idx = 3
    # 5 7 1 2 3 6
    # 1 2 3 4 5 6 7
    if len(nums) <= 1:
        return nums

    pivot_idx = len(nums) // 2
    pivot = nums[pivot_idx]
    remain = nums[:pivot_idx] + nums[pivot_idx+1:]
    left = [x for x in remain if x <= pivot]
    right = [x for x in remain if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)




def quick_sort(nums, start, end):
    if start >= end:
        return
    pivot = start
    left, right = start + 1, end
    # left는 시작 지점보다 1 더한 위치, right는 마지막 위치
    # 왼쪽 포인터의 숫자와 피벗 위치의 숫자를 비교하여 피벗 위치보다 커질 때까지 왼쪽 포인터 +1
    # 오른쪽 포인터의 숫자와 피벗 위치의 숫자를 비교하여 피벗 위치보다 작아질 때까지 오른쪽 포인터 -1
    # 피벗 왼쪽 포인터 오른쪽 포인터 -> 왼쪽과 오른쪽을 스왑
    # 피벗 오른쪽 포인터 왼쪽 포인터 -> 피벗과 오른쪽을 스왑
    while left <= right:
        while left <= end and nums[left] <= nums[pivot]:
            left += 1
        while right > start and nums[right] >= nums[pivot]:
            right -= 1
        
        if left > right:
            nums[pivot], nums[right] = nums[right], nums[pivot]
        else:
            nums[left], nums[right] = nums[right], nums[left]

    quick_sort(nums, start, right-1)
    quick_sort(nums, right+1, end)




def selection_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(nums)
# selection_sort(nums)

def insertion_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums

# insertion_sort(nums)


def merge(left_part, right_part):
    ret = []
    i, j = 0, 0
    while i < len(left_part) and j < len(right_part):
        # 왼쪽과 오른쪽을 비교해서 더 작은 것부터 append
        if left_part[i] < right_part[j]:
            ret.append(left_part[i])
            i += 1
        else:
            ret.append(right_part[j])
            j += 1
        
        if i == len(left_part):
            ret += right_part[j:]
        elif j == len(right_part):
            ret += left_part[i:]
    return ret

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    
    left_part = merge_sort(nums[:mid])
    right_part = merge_sort(nums[mid:])

    return merge(left_part, right_part)

merge_sort(nums)


def binary_search(L, trg):
    start, end = 0, len(L) - 1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] < trg:
            start = mid + 1
        else:
            end = mid -1
    if start < len(L):
        return start
    else:
        return -1

L = [1,4,8,10,11,11,11,11,14,14,17]
trg = 11

print(binary_search(L, trg))

print(L[binary_search(L, trg)])

from bisect import bisect_left, bisect_right

print(bisect_left(L, trg))

print(bisect_right(L, trg))



import heapq

heap = []

heapq.heappush(heap, [0,'A'])
heapq.heappush(heap, [5, 'B'])

heapq.heappop(heap)


import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    ret = {node: float('inf') for node in graph}
    # 자기 자신으로 돌아오는 경우는 0
    ret[start] = 0

    queue = []
    # start를 큐에 삽입
    heapq.heappush(queue, [ret[start], start])

    while queue:
        cur_len, cur_node = heapq.heappop(queue)

        if cur_len > ret[cur_node]:
            continue
        
        for next_node, next_len in graph[cur_node].items():
            new_len = cur_len + next_len
            if new_len < ret[next_node]:
                ret[next_node] = new_len
                heapq.heappush(queue, [new_len, next_node])

    return ret



class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def inorder_traversal(root):
    ret = []
    def dfs(tree): 
        if tree.left is not None:
            dfs(tree.left)
        
        ret.append(tree.value)

        if tree.right is not None:
            dfs(tree.right)

    dfs(root)
    return ret


def inverse_tree(tree):
    if tree is None:
        return None

    if tree.left is None and tree.right is None:
        return tree

    left_part = tree.left
    right_part = tree.right
    tree.left, tree.right = inverse_tree(right_part), inverse_tree(left_part)
    return tree


tree = Tree(1)
tree.left = Tree(2)
tree.left.left, tree.left.right = Tree(4), Tree(5)
tree.right = Tree(3)
tree.right.left, tree.right.right = Tree(6), Tree(7)

inorder_traversal(tree)


inorder_traversal(inverse_tree(tree))