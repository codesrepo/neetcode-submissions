from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        for i in set(Counter(s).keys()).union(set(Counter(t).keys())):
            if count_t[i]!=count_s[i]:
                return False
        return True