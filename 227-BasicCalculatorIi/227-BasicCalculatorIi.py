# Last updated: 11/1/2025, 9:34:01 PM
# Linear Space:
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operation = '+'
        num = 0

        for i, char in enumerate(s):
            if char.isnumeric():
                num = num * 10 + int(char)
            if char in '+-*/' or i == len(s) - 1:
                if operation == '+':
                    stack.append(num)
                elif operation == '-':
                    stack.append(-num)
                elif operation == '*':
                    stack.append(stack.pop() * num)
                elif operation == '/':
                    stack.append(int(stack.pop() / num))
                operation = char
                num = 0
        return sum(stack)

# # Constant space:
# class Solution:
#     def calculate(self, s: str) -> int:
#         i = 0
#         cur = prev = res = 0
#         cur_operation = "+"

#         while i < len(s):
#             cur_char = s[i]
#             if cur_char.isdigit():
#                 cur = 0
#                 while i < len(s) and s[i].isdigit():
#                     cur = cur * 10 + int(s[i])
#                     i += 1

#                 if cur_operation == "+":
#                     res += cur
#                     prev = cur
#                 elif cur_operation == "-":
#                     res -= cur
#                     prev = -cur
#                 elif cur_operation == "*":
#                     res -= prev
#                     res += prev * cur
#                     prev = prev * cur
#                 else:
#                     res -= prev
#                     res += int(prev / cur)
#                     prev = int(prev / cur)

#                 cur = 0
#             if i < len(s) and s[i] in "+-*/":
#                 cur_operation = s[i]
#             i += 1
#         return res
