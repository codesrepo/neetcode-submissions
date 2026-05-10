class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dup = {}
        for i in nums:
            if i in count_dup:
                return True
            else:
                count_dup[i]=1
        return False
        