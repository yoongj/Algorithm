class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(1):

            if n==1:
                return True
                break
            elif n%2==1 or n ==0:
                return False
                break
            else:
                n=n//2