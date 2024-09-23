class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(goal)):
            goal = goal[1:] + goal[0]
            if s == goal: return True

        return False
