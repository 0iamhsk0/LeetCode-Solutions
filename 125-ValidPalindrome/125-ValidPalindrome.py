# Last updated: 11/1/2025, 9:34:38 PM
# re (regular expressions) module is used to substitute occurrences of a pattern in a string with a replacement

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = re.sub('[^a-zA-Z0-9]','',s).lower()
        rev_str = new_str[::-1]
        if new_str == rev_str:
            return True
        return False
        