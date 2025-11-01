# Last updated: 11/1/2025, 9:35:05 PM
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # row_start, col_start = 0, 0
        # x = len(matrix[0])
        # row_end, col_end = x, x
        # while row_start <= row_end and col_start <= col_end:
        #     #four traversals:
        #     #right, down, left, up and these inside the while loop, each traversal each loop

        #     #right:
        #     for i in range(col_start, col_end):
        #         print(matrix[row_start][i]) #traversing that row(1st array) using column idices
        #     row_start -= 1

        #     #down:
        #     for i in range(row_start, row_end):
        #         print(matrix[i][col_end])
        #     col_end -= 1

        #     #left:
        #     for i in range(col_end, col_start):
        #         print(matrix[row_end][i])
        #     row_end -= 1

        #     #up:
        #     for i in range(row_end, row_start):
        #         print(matrix[i][col_start])
        #     col_start += 1

        # return 

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        result = []

        while row_start <= row_end and col_start <= col_end:
            # Move right
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1  # Move the row start down

            # Move down
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1  # Move the column end left

            # Move left (only if there's a row left)
            if row_start <= row_end:
                for i in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1  # Move the row end up

            # Move up (only if there's a column left)
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1  # Move the column start right

        return result


        