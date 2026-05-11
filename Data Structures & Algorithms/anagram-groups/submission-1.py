from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        clusters = {}
        for i,v in enumerate(strs):
            #print(frozenset(Counter(v)))
            temp = Counter(v)
            num_cat = []
            for j in temp:
                num_cat.append(str(j)+str(temp[j]))
            f = frozenset(num_cat)
            if f in clusters:
                clusters[f].append(i)
            else:
                clusters[f] = [i]
        for k,v in clusters.items():
            group = []
            for i in v:
                group.append(strs[i])
            res.append(group)
        return res

        