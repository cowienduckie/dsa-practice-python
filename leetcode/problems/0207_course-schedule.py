from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        before = [set() for _ in range(numCourses)]
        after = [set() for _ in range(numCourses)]

        for next_course, req in prerequisites:
            before[next_course].add(req)
            after[req].add(next_course)

        queue = deque([course for course in range(numCourses) if not before[course]])
        while queue:
            curr_course = queue.popleft()
            for next_course in after[curr_course]:
                before[next_course].remove(curr_course)
                if not before[next_course]:
                    queue.append(next_course)

        return not any(before)
