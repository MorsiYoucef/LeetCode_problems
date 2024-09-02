class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base case for powers of two: 1 is 2^0
        if n == 1:
            return True
        # Numbers less than 1 are not powers of two
        if n <= 0:
            return False
        # Check if n is divisible by 2 and recursively check n // 2
        if n % 2 == 0:
            return self.isPowerOfTwo(n // 2)
        else:
            return False
