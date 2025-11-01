# Last updated: 11/1/2025, 9:32:38 PM
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        
        return ''.join(stack)
