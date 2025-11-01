# Last updated: 11/1/2025, 9:33:21 PM
class Solution:
    #def fib(self, n: int) -> int:
        #base cases:
        # if n = 0:
        #     return 0
        # if n = 1:
        #     return 1
        ## general method
        # if n <= 1:
        #     return n
        # last = self.fib(n-1)
        # slast = self.fib(n-2)
        # return last + slast
        ## O(n)- space and O(1) - time method:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev, curr = 0, 1
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr

        