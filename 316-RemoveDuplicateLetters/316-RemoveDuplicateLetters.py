# Last updated: 11/1/2025, 9:33:51 PM
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occourance = {letter:i for i, letter in enumerate(s)}
        seen = set()
            
        for i, letter in enumerate(s):
            if letter not in seen:

                while stack and stack[-1] > letter and last_occourance[stack[-1]] > i:
                    seen.remove(stack.pop())

                seen.add(letter)
                stack.append(letter)

        return ''.join(stack)
        