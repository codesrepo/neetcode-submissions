class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        stack = []
        pairs = {")":"(","}":"{","]":"["}
        closing =  set(pairs.keys())
        for i,v in enumerate(s):
            if v in closing:
                if not stack:
                    return False
                top_closing=stack.pop()
                if top_closing!=pairs.get(v,"-"):
                    return False
            else:
                stack.append(v)
        if stack:
            return False
        return True
        