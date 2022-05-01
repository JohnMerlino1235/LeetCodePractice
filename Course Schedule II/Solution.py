class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = {i: [] for i in range(numCourses)}
        visited, cycle, ans = set(), set(), []

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        """
        Base Cases for a Course:
        1 -> visited -> course has been added to output answer
        2 -> visiting -> course has not beed added to output but added to the cycle
        3 -> unvisited -> course has not been added to the answer or the cycle
        """

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for nei in adj_list[course]:
                if not dfs(nei):
                    return False

            cycle.remove(course)
            visited.add(course)
            ans.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return ans

