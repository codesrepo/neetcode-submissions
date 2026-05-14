class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def get_cumm(nums):
            forward =[]
            cumm = 1
            for i,v in enumerate(nums):
                if i==0:
                    forward.append(1)
                else:
                    cumm*=nums[i-1]
                    forward.append(cumm)
            return forward
        forward = get_cumm(nums)
        reverse = get_cumm(nums[::-1])
        reverse = reverse[::-1]
        for i in range(len(nums)):
            forward[i]=forward[i]*reverse[i]
        return forward

        


        