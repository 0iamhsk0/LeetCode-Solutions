# Last updated: 11/1/2025, 9:35:02 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    # Strip any trailing spaces and split the string into words
        words = s.strip().split()
        # Return the length of the last word
        return len(words[-1])