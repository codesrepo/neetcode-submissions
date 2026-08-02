class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AL = {}
        for i in range(numCourses):
            AL[i] = []
        for i in prerequisites:
            AL[i[1]].append(i[0])

        ts = []
        visited = set()
        stack=[]
        current_path = set()
        for k in AL.keys():
            if not AL[k]: continue
            if k in visited: continue
            stack.append(k)
            while stack:
                node = stack[-1]
                current_path.add(node)
                if node not in visited:
                    visited.add(node)
                    for v in AL[node]:
                        if v in current_path: return False
                        if v in visited: continue 
                       
                        stack.append(v)
                else:
                    stack.pop()
                    current_path.remove(node)
                    if node not in ts:
                        ts.append(node)
        return True
                
                
                


                