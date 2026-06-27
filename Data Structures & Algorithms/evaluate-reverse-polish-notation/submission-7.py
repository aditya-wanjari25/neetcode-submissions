class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        notations = ["+","-","*","/"]
        ops = {
            "+" : lambda a,b: a+b,
            "-" : lambda a,b: a-b,
            "*" : lambda a,b: a*b,
            "/" : lambda a,b: int(a/b)
        }
        for c in tokens:
            if c not in notations:
                stack.append(int(c))
            else:
                val_b = stack.pop()
                val_a = stack.pop()
                stack.append(ops[c](val_a,val_b))
                    
        
        return stack[-1]
        

        