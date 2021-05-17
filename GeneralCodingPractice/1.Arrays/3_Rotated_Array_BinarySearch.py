class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #let us say start and end index of an array
        start=0
        end=len(nums)-1
        
        #if start is greater than end that means it is an empty array
        if start > end:
            return -1
        
        #iterative loop for binary search with rotated array using start = pivot+1 and end=pivot-1 depending upon cases
        while start<=end:
            pivot = start + (end-start)//2
            
            #case 1 when target value reaches middle value and is the pivot value
            if nums[pivot]==target:
                return pivot
            
            #case 2 target lies between start and pivot
            elif nums[start] <= nums[pivot] and target >= nums[start] and target <= nums[pivot]:
                end = pivot-1
            
            #case 3 target lies between pivot and end
            elif nums[pivot] <= nums[end] and target >= nums[pivot] and target <= nums[end]:
                start = pivot+1
            
            #case 4 target lies greater than end value
            elif nums[start] <= nums[pivot] and nums[pivot] <= nums[end] and target > nums[end]:
                start = pivot+1
            #additional case 5 when start value is greater than pivot value i.e. rotated index
            elif nums[start] >= nums[pivot]:
                end = pivot-1
            #additional case 6 i.e. rotated index
            elif nums[pivot] >= nums[end]:
                start = pivot+1
            else:
                return -1
        return -1

'''
Your input
[4,5,6,7,0,1,2]
3
Output
-1
Expected
-1
Runtime: 48 ms, faster than 38.13% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.9 MB, less than 20.84% of Python3 online submissions for Search in Rotated Sorted Array.
'''
