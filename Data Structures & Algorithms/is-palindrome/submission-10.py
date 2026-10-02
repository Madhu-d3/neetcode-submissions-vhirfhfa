class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for x in s:
            if x.isalnum() :
                s1.append(x.lower())
        return s1 == s1[::-1]
        
        