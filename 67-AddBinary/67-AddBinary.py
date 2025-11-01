# Last updated: 11/1/2025, 9:34:58 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Process both strings from the end to the beginning
        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Compute the sum of bits plus the carry
            total = bit_a + bit_b + carry
            result.append(str(total % 2))  # Add the least significant bit to result
            carry = total // 2  # Compute the carry
            
            # Move pointers
            i -= 1
            j -= 1
        
        # Join and reverse the result to form the final binary string
        return ''.join(reversed(result))