from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        track_count = Counter(nums)
        pos_series = []
        seen_so_far = set()
        for i,v in enumerate(nums):
            seen_so_far.add(v)
            if i==0:
                if track_count.get(v+1):
                    pos_series.append(i)
            else:
                x = track_count.get(v-1,"dummy")
                if x in seen_so_far:
                    continue
                else:
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
            



                

        