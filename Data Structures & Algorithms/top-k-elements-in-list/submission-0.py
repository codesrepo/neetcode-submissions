from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq  = Counter(nums)
        sorted_custom = sorted(freq.items(), key=lambda x: -x[1])
        for i in range(k):
            res.append(sorted_custom[i][0])
        return res


        