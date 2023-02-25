class MaxProfit:
    def stockProjection(self, stockPrice: list[int]):
    
        if not stockPrice:
            return 0
        
        maxProfit = 0
        startPrice = stockPrice[0]    
        
        for i in stockPrice:
            
            if startPrice > i:
                startPrice = i;
                
            elif i - startPrice  > maxProfit:  
                maxProfit = i - startPrice  
                
        return maxProfit
    
    
           
p = MaxProfit()

result = p.stockProjection([7,1,5,3,6,4])                   

print(result)   
        
        
        