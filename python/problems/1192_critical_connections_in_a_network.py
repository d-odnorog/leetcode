# https://leetcode.com/problems/critical-connections-in-a-network/
from collections import defaultdict


class Solution:
    def criticalConnections(
        self, n: int, connections: list[list[int]]
    ) -> list[list[int]]:
        G = defaultdict(list)
        for v, w in connections:
            G[v].append(w)
            G[w].append(v)
        self.time = 0
        visited = set()
        visited_time = defaultdict(int)
        parent = defaultdict(lambda: float('inf'))
        res = []

        def dfs(v):
            if v in visited:
                return visited_time[v]
            visited.add(v)
            visited_time[v] = self.time
            self.time += 1
            highest = float('inf')
            for w in G[v]:
                if w in visited:
                    if w != parent[v]:
                        highest = min(highest, visited_time[w])
                else:
                    parent[w] = v
                    highest_w = dfs(w)
                    if highest_w > visited_time[v]:
                        res.append([v, w])
                    highest = min(highest, highest_w)

            return highest

        dfs(0)

        return res


if __name__ == '__main__':
    s = Solution()

    assert s.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]) == [[1, 3]]
    assert s.criticalConnections(2, [[0, 1]]) == [[0, 1]]
