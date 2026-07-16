class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for ch in s:
            if ch == '(':
                lo += 1; hi += 1
            elif ch == ')':
                hi -= 1
                if hi < 0:
                    return False
                if lo: lo -= 1
            else:  # ch == '*'
                hi += 1
                if lo: lo -= 1
        return lo == 0

