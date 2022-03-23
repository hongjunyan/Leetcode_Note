import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph_bfs(self, node: 'Node') -> 'Node':

        def bfs(node: "Node") -> Node:
            q = collections.deque()
            q.append(node)
            old2new = {node: Node(node.val)}  # {old_node: new_node}

            while q:
                cur = q.popleft()
                copy = old2new[cur]

                for nb in cur.neighbors:
                    if nb not in old2new:
                        old2new[nb] = Node(nb.val)
                        q.append(nb)
                    copy.neighbors.append(old2new[nb])
            return old2new[node]

        return bfs(node) if node else None

    def cloneGraph_dfs(self, node: 'Node') -> 'Node':
        old2new = {}  # {old_node: new_node

        def dfs(node: "Node") -> "Node":
            if node in old2new:
                return old2new[node]

            copy = Node(node.val)
            old2new[node] = copy
            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))

            return copy

        return dfs(node) if node else None
