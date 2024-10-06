class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                return nums[i]
            else:
                my_dict[nums[i]] = 1