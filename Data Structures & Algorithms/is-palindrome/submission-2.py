class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for x in s.lower():
            if x.isalnum():
                s_list.append(x)
        
        return s_list == s_list[::-1]

        