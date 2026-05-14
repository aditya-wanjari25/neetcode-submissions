class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using bucket sort
        bucket_list = []
        bucket_list = [[] for i in range(len(nums)+1)]
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        # {1:3,2:2,3:1}
        for key, value in freq_dict.items():
            bucket_list[value].append(key)
        
        result = []
        for l in reversed(bucket_list):
            if len(result) < k and len(l)>0:
                result.extend(l)
                

        return result
            
            
            
            
            
