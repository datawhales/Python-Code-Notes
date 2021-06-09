""" 리스트에서 두 요소를 합하여 target이 되는 요소의 인덱스를 return하는 메소드.
"""
def two_sum(nums, trg):
    """ 2개의 포인터를 이용한 방법(nums는 sorting 되어 있다고 가정).
        시간: O(N), 공간: O(1)
    """
    i, j = 0, len(nums) - 1
    while nums[i] + nums[j] != trg:
        if nums[i] + nums[j] < trg:
            i += 1
        else:
            j -= 1
    return [i, j]

def two_sum_2(nums, trg):
    """ 딕셔너리를 이용한 방법.
        시간: O(N), 공간: O(N)
    """
    trg_dict = dict()
    for i in range(len(nums)):
        if nums[i] in trg_dict:
            return [trg_dict[nums[i]], i]
        key = trg - nums[i]
        trg_dict[key] = i

def two_sum_3(nums, trg):
    """ 2개의 for loop 사용한 방법.
        시간: O(N^2), 공간: O(1)
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == trg:
                return [i, j]
        
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    trg = 9
    print(two_sum(nums, trg))
    print(two_sum_2(nums, trg))
    print(two_sum_3(nums, trg))