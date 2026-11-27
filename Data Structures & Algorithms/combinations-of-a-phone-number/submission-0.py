class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_dict = {
            "2" :['a','b','c'],
            "3" :['d','e','f'],
            "4" :['g','h','i'],
            "5" :['j','k','l'],
            "6" :['m','n','o'],
            "7" :['p','q','r', 's'],
            "8" :['t','u','v'],
            "9" :['w','x','y','z'],
        }


        result = []


        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return

            digit_list = number_dict.get(digits[index])
            
            for letter in digit_list:
                backtrack(index+1, current + letter)
        

        if not digits:
            return []
       
        backtrack(0,"")
        return result
            

            

        