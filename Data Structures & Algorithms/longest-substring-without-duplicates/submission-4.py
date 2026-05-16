class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_seen={}
        track_len = 0
        current_len = 0
        current_pointer = 0
        for i,v in enumerate(s):
            pos = temp_seen.get(v,-1)
            if pos==-1:
                temp_seen[v] = i
            else:
                current_pointer = max(current_pointer,temp_seen[v]+1)
                temp_seen[v] = i
            current_len = i - current_pointer +1
            track_len = max(track_len,current_len)
        return track_len


                

            

        