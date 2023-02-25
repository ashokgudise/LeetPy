class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        dupChecker = set()
        
        
        for num in nums:
            
            if num in dupChecker:
                return True
            dupChecker.add(num)
            
        return False    
        
        
        
        
        
        
s = Solution()

result = s.containsDuplicate([1,2,3,1])        

print(result)