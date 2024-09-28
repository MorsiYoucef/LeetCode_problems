class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            dic[arr[i]]=arr.count(arr[i])
        values = list(dic.values())
        repeated_values = set([value for value in values if values.count(value) > 1])

        if (repeated_values):
            return False
        else:
            return True