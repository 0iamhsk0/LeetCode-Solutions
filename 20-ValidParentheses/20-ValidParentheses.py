# Last updated: 11/1/2025, 9:35:19 PM
# Approach 1
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if stack and c in brackets and brackets[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0

# Approach 2
# class Solution:
#     def isValid(self, s: str) -> bool:

#         if len(s) % 2 != 0:
#             return False

#         stack = []

#         for val in s:
#             if val == "(" or val == "{" or val == "[":
#                 stack.append(val)
#             else:
#                 if len(stack) == 0:
#                     return False

#                 peek = stack[-1]
#                 if val == ")":
#                     if peek == "(":
#                         stack.pop()
#                     else:
#                         return False
#                 elif val == "}":
#                     if peek == "{":
#                         stack.pop()
#                     else:
#                         return False
#                 elif val == "]":
#                     if peek == "[":
#                         stack.pop()
#                     else:
#                         return False

#         return len(stack) == 0


