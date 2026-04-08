class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = []
        for n in nums:
            if n in nums_map:
                return True
            nums_map.append(n)

        return False