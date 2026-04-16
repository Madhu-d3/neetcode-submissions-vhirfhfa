class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        while i < j:
            diff = numbers[j] + numbers[i]
            if diff > target:
                j -= 1
            elif diff < target:
                i += 1
            elif diff == target:
                return [i+1, j+1]