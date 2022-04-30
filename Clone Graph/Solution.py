"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Notes:
        - Connected undirected graph
        - Each node in graph contains the following:
            <-> val (Integere)
            <-> neighbors (List[Node])

        <-> Input:
            - adjacency list
            - each node's value is its node index, ex Node1 = 1, Node2 = 2, .. etc
            - given node will always be the first node
        <-> Output:
            -

        Use HashMap and DFS, if 1 has neighbor 2 then 2 is also going to have neighbor 1
        Map old nodes to new nodes / copy nodes

        - Start at 1, create a copy of nodes and their neighbors
        - Recursive
        - Go to first neighbor of first node, clone starting at 2
        - One a node is cloned, map the old node to the cloned node


        """

        cloned_graph = {}

        def dfs(node):
            if node in cloned_graph:
                return cloned_graph[node]

            new_clone = Node(node.val)

            cloned_graph[node] = new_clone

            for neighbor in node.neighbors:
                new_clone.neighbors.append(dfs(neighbor))

            return new_clone

        return dfs(node) if node else None