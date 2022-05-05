""" Leetcode. Dijkstra.
    743. Network Delay Time
    Link: https://leetcode.com/problems/network-delay-time/
"""
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # graph: {2: [(1,1), (3,1)], 3: [(4, 1)]}
        
        dist = {node: float('inf') for node in range(1, n+1)}
        
        # k = start node
        dist[k] = 0
        
        queue = []
        # queue에 [해당 노드까지 최단 거리, 노드] 형태로 저장
        heapq.heappush(queue, [dist[k], k])
        
        while queue:
            cur_dist, cur_node = heapq.heappop(queue)
            
            if cur_dist > dist[cur_node]:
                continue
                
            for next_node, next_dist in graph[cur_node]:
                new_dist = cur_dist + next_dist
                
                if new_dist < dist[next_node]:
                    dist[next_node] = new_dist
                    heapq.heappush(queue, [new_dist, next_node])
        
        if max(dist.values()) == float('inf'):
            return -1
        else:
            return max(dist.values())
    
    def networkDelayTime_2(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # graph: {2: [(1,1), (3,1)], 3: [(4, 1)]}
        
        dist = {}
        
        queue = [(0, k)]
        
        while queue:
            cur_dist, cur_node = heapq.heappop(queue)
            
            if cur_node not in dist:
                dist[cur_node] = cur_dist
                
                for next_node, next_dist in graph[cur_node]:
                    new_dist = cur_dist + next_dist
                    heapq.heappush(queue, (new_dist, next_node))
        
        if len(dist) == n:
            return max(dist.values())
        else:
            return -1
            
if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    answer = 2
    sol = Solution()
    result = sol.networkDelayTime(times, n, k)

    print(f"answer: {answer}\nresult: {result}\n비교: {answer == result}")
   
    """
    answer: 2
    result: 2
    비교: True
    """