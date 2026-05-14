class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        
        return encoded 


    def decode(self, s: str) -> List[str]:
        # "5#hello5#world"
        decoded = []
        i = 0
        while i < len(s):
            # find len of word
            j = i
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            decoded.append(word)

            i = j + length + 1
        
        return decoded
        
        
