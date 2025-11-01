# Last updated: 11/1/2025, 9:33:48 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses the input list of characters in-place.
        :param s: List[str] - The list of characters to reverse
        :return: None - Modifies the input list in-place
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap the characters at the left and right indices
            s[left], s[right] = s[right], s[left]
            # Move towards the middle
            left += 1
            right -= 1