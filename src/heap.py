import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소 heap에 넣기
    for value in iterable:
        heapq.heappush(h, value)
    # heap에 삽입된 모든 원소 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

if __name__ == "__main__":
    iterable = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    result = heapsort(iterable)
    print(result)