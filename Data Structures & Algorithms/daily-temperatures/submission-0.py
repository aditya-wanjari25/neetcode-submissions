class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_day_index = stack.pop()
                days_waited = i - prev_day_index
                result[prev_day_index] = days_waited

            stack.append(i)
        
        return result


        