class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # brute force -> O(n^2)
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            count = 0
            for j in range(i+1, len(temperatures)):
                count+=1
                if temperatures[j] > curr:
                    output[i] = count
                    break
        
        return output
    
            
            

            
                    
