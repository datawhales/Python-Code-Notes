""" undirected graph 구현과
    graph traverse (DFS, BFS) 구현.
"""
class undi_graph:
    def __init__(self, V, E):
        self.V = V[:]
        self.neighbor = dict()
        for v in V:
            self.neighbor[v] = []
        for v, w in E:
            self.neighbor[v].append(w)
            self.neighbor[w].append(v)

    def __DFTHelp(self, visited, v):
        if not visited[v]:
            visited[v] = True
            print(v)   # preorder
            for w in self.neighbor[v]:
                self.__DFTHelp(visited, w)
            # print(v)   # postorder

    def DFT(self):
        if self.V:
            visited = dict()
        for v in self.V:
            visited[v] = False
        for v in self.V:
            self.__DFTHelp(visited, v)

    def BFT(self):
        if self.V:
            visited = dict()
        for v in self.V:
            visited[v] = False
        from collections import deque
        queue = deque()
        for v in self.V:
            queue.append(v)
            while queue:
                v.popleft()
                print(v)
                if not visited[v]:
                    visited[v] = True
                    for w in self.neighbor[v]:
                        queue.append(w)