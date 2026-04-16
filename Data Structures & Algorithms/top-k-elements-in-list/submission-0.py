class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        for n, c in freq_map.items():
            freq[c].append(n)
        res = []
        for n in range(len(freq) -1, 0, -1 ):
            for x in freq[n] :
                res.append(x)
                if len(res) == k:
                    return res
        