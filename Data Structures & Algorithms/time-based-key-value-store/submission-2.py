'''
Store multiple values of the same key
{key: value}
if timestamps are unique
{1: [key, value, 2: [key, value]}

ts 1: alice happy
{1: ['alice','happy']}

get alice 1
Check value at TS 1, if key matches return the value,
if key doesnt match go TS -= 1 until TS >=0
'''

class TimeMap:

    def __init__(self):
        self.data_structure = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data_structure[timestamp] = [key, value]

    def get(self, key: str, timestamp: int) -> str:
        
        while timestamp > 0:
            if timestamp in self.data_structure:
                if(self.data_structure[timestamp][0] == key):
                    return self.data_structure[timestamp][1]
            
            timestamp -= 1
        return ""
        
        
        
