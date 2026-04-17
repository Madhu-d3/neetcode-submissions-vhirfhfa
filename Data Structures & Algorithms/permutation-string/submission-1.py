class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_set = {}
        if len(s1) > len(s2):
            return False
        for s in s1:
            char_set[ord(s) - ord('a')] = char_set.get(ord(s) - ord('a'), 0) + 1
        l , r = 0, len(s1)
        while l < r and r < len(s2) + 1:
            s2_set = {}
            for x in s2[l:r]:
                #print(x, s2_set.get(ord(x) - ord('a'), 0))
                s2_set[ord(x) - ord('a')] = s2_set.get(ord(x) - ord('a'), 0) + 1
            if s2_set == char_set :
                return True
            #print(s2_set, char_set,s2[l:r] , s1)
            l += 1
            r += 1
        return False

        
        