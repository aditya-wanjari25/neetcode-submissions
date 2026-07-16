"""
dict = {
key : [(value, timestamp)]
}

search
"""


class TimeMap:

    def __init__(self):
        self.data_structure = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data_structure:
            self.data_structure[key].append((value,timestamp))
        else:
            self.data_structure[key] = [(value,timestamp)]



    def get(self, key: str, timestamp: int) -> str:
        # 1. Base case: If the key isn't in our store, return ""
        res = ""
        if key not in self.data_structure:
            return res

        values = self.data_structure[key]
        
        # 2. Initialize binary search pointers
        left, right = 0, len(values) - 1

        # 3. Binary Search loop
        while left <= right:
            mid = (left + right) // 2
            
            # values[mid][1] is the timestamp at the current middle index
            if values[mid][1] <= timestamp:
                # We found a valid value! Save it to 'res'
                res = values[mid][0]
                # Look to the right to see if there's a closer timestamp
                left = mid + 1
            else:
                # The timestamp is too large, narrow the search to the left half
                right = mid - 1

        return res
