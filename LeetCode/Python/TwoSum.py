class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #creating dictionary to hold values that I loop through
        hist = {}

        #for index, value in nums
        for i, n in enumerate(nums):
            #if target - n is in the hist dictionary (checks key, not value)
            if target - n in hist:
                #using target-n to return the key, i is the index we are using to loop
                return(hist[target-n], i)
            #if not in the dictionary, add it
            hist[n] = i