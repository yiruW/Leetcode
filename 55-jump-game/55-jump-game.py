class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        while index < len(nums) -1:
            if nums[index] == 0: return False
            ref = index
            maxStep = 0
            for i in range(1, nums[index] +1):
                if i + index >= len(nums) - 1: return True
                pos = nums[i+index] + i + index
                if pos >= len(nums) - 1: return True
                if pos >= maxStep:
                    maxStep = pos
                    ref = i
            if maxStep == 0: return False
            index = ref + index
        return True
            