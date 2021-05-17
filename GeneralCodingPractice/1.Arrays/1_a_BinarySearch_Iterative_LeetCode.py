class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #intial lower and higher keys
        lower =0
        higher = len(nums)-1
        
        while lower <=higher:
            mid = lower+((higher-lower)//2)
            
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                higher = mid-1
            else:
                lower = mid+1
        return -1

''' Test Case:
[-1,0,3,5,9,12]
9
Output
4
Expected
4

236 ms, faster than 59.70% of Python3 online submissions for Binary Search. - Memory = 15.5 MB
But has memory complexity of O(1) constant
'''
