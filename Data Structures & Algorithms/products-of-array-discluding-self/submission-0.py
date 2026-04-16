class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        for i in range(1, len(nums), 1):
            #[1,2,3,4] = [1,1*1,1*2, 2*3]
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-1,0,-1):
            #[1,2,3,4] = [4*3*2, 4*3, 4,1]
            postfix[i-1] = nums[i] * postfix[i]
        return [prefix[i]*postfix[i] for i in range(len(nums))]



        