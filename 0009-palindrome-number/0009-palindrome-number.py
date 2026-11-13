class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        left = 0
        right = len(x1)-1
        while True:
            if left >= right:
                if x == int(x1):
                    return True
                else:
                    return False
            else:
                if x1[left] == x1[right]:
                    left += 1
                    right -=1
                else:
                    return False

        