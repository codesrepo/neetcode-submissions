class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                temp = temperatures[stack[-1]]
                while stack and v>temp:
                    res[stack[-1]] = i-stack[-1]
                    stack.pop()
                    if stack:
                        temp = temperatures[stack[-1]]
                stack.append(i)
        return res




        