"""
Longest Consecutive Sequence (LeetCode 128)

Problem:
    Given an unsorted array of integers nums, return the length of the
    longest run of consecutive values (order in the array doesn't
    matter). Must run in O(n) time.

Example:
    nums = [100, 4, 200, 1, 3, 2]
    Output: 4             # the run 1, 2, 3, 4
"""
from typing import List
from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: #catch edge case scenarios
            return 0
        track_count = Counter(nums)
        pos_series = []
        seen_so_far = set()
        for i,v in enumerate(nums):
            seen_so_far.add(v)
            if v-1 in track_count:
                    continue
              
            if track_count.get(v+1):
                    pos_series.append(i)
        
        big_len=1
        for i in pos_series:
            max_len=0
            c=nums[i]
            while track_count.get(c):
                max_len+=1
                c+=1
            if big_len<max_len:
                big_len=max_len
        return big_len
            