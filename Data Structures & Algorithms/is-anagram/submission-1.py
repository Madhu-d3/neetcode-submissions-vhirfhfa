class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for s1 in s:
            s_map[s1] = s_map.get(s1, 0) + 1

        for t1 in t:
            t_map[t1] = t_map.get(t1, 0) + 1
        return s_map == t_map
