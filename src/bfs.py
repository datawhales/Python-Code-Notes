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

def maze(N, M, graph):
    """ 미로 탈출 문제.
        1인 지역만 지나갈 수 있을 때 탈출 위치까지의 최단 거리 계산.
        
        Point: 다음 위치가 그래프를 벗어나면 continue,
                0인 위치이면 continue,
                1인 위치(한 번도 지나지 않은 지역)이면 큐에 추가하고 이전 위치 + 1을 저장.
    """
    from collections import deque
    # N, M = map(int, input().split())
    # graph = []
    # for _ in range(N):
    #     graph.append(list(map(int, input())))

    def bfs(x, y):
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
                
            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

    bfs(0,0)
    return graph[N-1][M-1]