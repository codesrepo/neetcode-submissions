from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        unique_objects = set(t)
        seq_len = -1
        start = []
        len_small = len(t)
        pattern = ""
        current_len = 10000
        for i,v in enumerate(s):
            if v not in unique_objects:
                continue
            if v in unique_objects:
                start.append(i)
                required[v]-=1
                if required[v]>=0:
                    len_small-=1
                if required[v]<0:
                    while(start and required[s[start[0]]]<0):
                        required[s[start[0]]]+=1
                        start = start[1:]                    
              
            if len_small==0:
                if start and (current_len > start[-1]-start[0]+1):
                    current_len = start[-1]-start[0]+1
                    pattern = s[start[0]:start[-1]+1]           
        return pattern



                



        