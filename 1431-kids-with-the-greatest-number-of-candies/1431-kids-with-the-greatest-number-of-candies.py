class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [current_candies + extraCandies >= max_candies 
                  for current_candies in candies]
      
        return result
        