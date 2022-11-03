class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        u = len(numbers) - 1
        while (l < u):
            temp = numbers[l] + numbers[u]
            if temp == target:
                return [l+1,u+1]
            elif temp < target:
                l += 1
            else:
                u -= 1
        