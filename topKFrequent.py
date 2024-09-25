class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                continue
            dic[nums[i]] = nums.count(nums[i])
        sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        res = []
        j = 1
        for key in sorted_dict:
            if k == 0:
                break
            res.append(key)
            k-=1
            
        return res
        