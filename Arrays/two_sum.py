class Solution:
    def twoSum( self,nums: list[int], target: int) -> list[int]:
        prevMap = {} 

        for i, item in enumerate(nums):
            diff = target - item

            if(diff in prevMap):
                return [prevMap[diff],i]
            prevMap[item] = i
            
# Calling Above Function            
s = Solution()

result = s.twoSum([1,2,3,4,5], 5)

print(result)