class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        for left in range(len(numbers)):
            while numbers[left] + numbers[right] > target: right -= 1
            if numbers[left] + numbers[right] == target: return [left + 1, right + 1]
        return[-1, -1]