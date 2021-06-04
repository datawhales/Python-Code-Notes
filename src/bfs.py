""" bfs 함수 구현.

    ex) graph = [
        [1, 3, 6],
        [0, 2, 3],
        [1, 4, 5],
        [0, 1, 4],
        [2, 3, 5],
        [2, 4],
        [0]
    ]
"""
def bfs_shortest_path(graph, v, visited):
    """ 최단 경로 구하는 bfs 함수.
        visited에 1 저장이 아닌 지난 edge의 수를 저장.
        연결된 다음 노드에 대해 이전 노드보다 1 더한 값을 저장한다.
    """
    from collections import deque
    queue = deque([v])
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                # 이전 step보다 1 더한 값을 저장
                visited[i] = visited[x] + 1

def bfs(graph, v, visited):
    """ 일반적인 bfs 함수.
    """
    from collections import deque
    queue = deque([v])
    visited[v] = 1
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1