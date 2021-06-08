""" Linear Search algorithm.
    1. while문 사용
    2. sentinel
    3. for문 사용
    4. list.index() 사용
"""
def linear_search_1(L, trg):
    """ 1. while문 사용.
    """
    i = 0
    while i < len(L) and L[i] != trg:
        i += 1
    if i == len(L):
        return -1
    else:
        return i
    
def linear_search_2(L, trg):
    """ 2. sentinel.
    """
    L.append(trg)
    i = 0
    while L[i] != trg:
        i += 1
    L.pop()
    if i == len(L):
        return -1
    else:
        return i

def linear_search_3(L, trg):
    """ 3. for문 사용.
    """
    for i in range(len(L)):
        if L[i] == trg:
            return i
    return -1

def linear_search_4(L, trg):
    """ list.index() 사용.
    """
    return L.index(trg)

if __name__ == "__main__":
    L = [5, -2, 0, 100, -6, 7, 4, 9, -7, 50, 4, 3]
    trg = 4
    print(linear_search_1(L, trg))
    print(linear_search_2(L, trg))
    print(linear_search_3(L, trg))
    print(linear_search_4(L, trg))