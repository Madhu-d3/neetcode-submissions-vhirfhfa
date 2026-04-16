class Solution:
    def groupAnagrams(self, str):
        
        str_map = defaultdict(list)
        for s in str:
            char_map = [0] * 26
            for c in s:
                char_map[ord(c) - ord('a')] += 1
            str_map[tuple(char_map)].append(s)
        return list(str_map.values())
        

