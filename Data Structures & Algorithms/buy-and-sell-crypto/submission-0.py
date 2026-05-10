class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = -1
        min_so_far = 1000
        pnl = 0
        for i,v in enumerate(prices):
            if min_so_far > v:
                min_so_far=v
                max_so_far=v
            if max_so_far < v:
                max_so_far=v
            diff = max_so_far - min_so_far
            if pnl<diff:
                pnl=diff
        return pnl
        



        