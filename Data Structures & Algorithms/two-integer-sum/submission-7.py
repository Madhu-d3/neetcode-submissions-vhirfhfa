class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = {}
        
        for i, n in enumerate(nums):
            out[n] = i

        for i , n in enumerate(nums):
            diff = target - n
            if diff in out and out[diff] != i:
                return [i, out[diff]]
        return []
            

        