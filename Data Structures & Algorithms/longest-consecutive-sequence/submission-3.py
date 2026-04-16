class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        print(nums)
        i = 0
        print(nums)
        count, maxCount = 1, 1
        if len(nums) == 0:
            return 0
        elif len(nums) == 1 : 
            return 1
        while i < len(nums) - 1:
            print(i, nums[i], nums[i + 1], count)
            if nums[i + 1] == nums[i] + 1:
                count += 1
            else:
                count = 1
            maxCount = max(count, maxCount)
            i += 1

        return maxCount
        