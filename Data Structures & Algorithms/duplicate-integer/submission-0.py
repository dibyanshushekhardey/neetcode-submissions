class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = 0
        list_1 = []
        for i in nums:
            if i not in list_1:
                list_1.append(i)
                res += 0
            else:
                res += 1
        if res != 0:
            return True
        else:
            return False
        