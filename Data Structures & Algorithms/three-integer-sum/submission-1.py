class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i , n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            j , k = i + 1 , len(nums) - 1
            while j < k:
                total_sum = n + nums[j] + nums[k]
                if nums[k] + nums[i] + nums[j] > 0 :
                    k = k - 1
                elif nums[k] + nums[i] + nums[j] < 0:
                    j = j + 1
                else:
                    res.append([n, nums[j],nums[k]])
                    j = j+1
                    while nums[j] == nums[j-1] and j < k:
                        j = j + 1
        return res
            


