class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        l = len(s)
        while i < l:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # the great indian rope trick
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res
            
            



