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
        
        
        
