class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointer solution
        l, r = 0, len(s) - 1
        while l <= r:
            if alphanum(s[l]) :
                if alphanum(s[r]):
                    if s[l].lower() == s[r].lower():
                        l += 1
                        r -= 1
                    else:
                        return False
                else:
                    r -= 1
            else:
                l += 1

        return True

def alphanum(c):
    return (ord('a') <= ord(c) <= ord('z')
            or ord('A') <= ord(c) <= ord('Z')
            or ord('0') <= ord(c) <= ord('9'))

        