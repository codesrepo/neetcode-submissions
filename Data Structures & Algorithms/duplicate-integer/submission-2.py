class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dup = set()
        seen_add = count_dup.add
        for i in nums:
            if i in count_dup:
                return True
            else:
                seen_add(i)
        return False
        