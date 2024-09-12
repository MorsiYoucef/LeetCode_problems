class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            leftIndex = 0
            rightIndex = 0
            for j in range(len(nums)):
                if j == i:
                    continue
                elif j<i:
                    leftIndex+=nums[j]
                elif j>i:
                    rightIndex +=nums[j]
            if leftIndex == rightIndex:
                return i
        return -1
            
        