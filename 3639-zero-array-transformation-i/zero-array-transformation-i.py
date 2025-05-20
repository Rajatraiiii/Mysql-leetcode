class Solution(object):
    def isZeroArray(self, nums, queries):
      
        n = len(nums)
        cover = [0] * (n + 1)

       
        for l, r in queries:
            cover[l] += 1
            if r + 1 < n:
                cover[r + 1] -= 1

        
        for i in range(1, n):
            cover[i] += cover[i - 1]


        for i in range(n):
            if nums[i] > cover[i]:
                return False

        return True
sol = Solution()
print(sol.isZeroArray([1,0,1], [[0,2]]))           
print(sol.isZeroArray([4,3,2,1], [[1,3],[0,2]]))   

        