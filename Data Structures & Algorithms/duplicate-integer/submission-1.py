class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dup = set()
        for i in nums:
            if i in count_dup:
                return True
            else:
                count_dup.add(i)
        return False
        