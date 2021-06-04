""" dfs 함수 구현.
    그래프 형태에 따라 다르게 구현.
"""
def dfs_by_index(graph, v, visited):
    """ 노드가 연결되어 있으면 1로 나타내는 2차원 배열 그래프.

        ex)
            graph = [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 1]
            ]
    """
    visited[v] = 1
    for i in range(len(graph)):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs_by_index(graph, i, visited)

def dfs_by_nodenum(graph, v, visited):
    """ 각 노드에 대해 연결된 노드의 번호를 나타내는 2차원 배열 그래프.

        ex)
            graph = [
                [],
                [2, 3, 8],
                [1, 7],
                [1, 4, 5],
                [3, 5],
                [3, 4],
                [7],
                [2, 6, 8],
                [1, 7]
            ]
    """
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs_by_nodenum(graph, i, visited)