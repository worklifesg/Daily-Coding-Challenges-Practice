def search_rec(nums, target,lower,higher):
#if lower index is greater than higher which occurs only when the element is not present in the list
  if lower > higher:
    return -1
        
   #mid value:
  mid = lower +((higher-lower)//2)
  #if the mid value as the key same as expected element return the value in the mid key
  if nums[mid] == target:
    return mid
  #if key is less than mid value start the function again (recursive)
  elif target < nums[mid]:
    return search_rec(nums, target, lower,mid-1)
  #if key > mid value start the rest of the array for seach again
  else:
    return search_rec(nums, target, mid+1,higher)
    
def search(nums, target):
  return search_rec(nums, target,0,len(nums)-1)

arr = [1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
inputs = [10, 49, 99, 110, 176]

for i in range(len(inputs)):
  print("search(arr, " + str(inputs[i])+ ") = " +  str(search(arr, inputs[i])))

''' Run
search(arr, 10) = 1
search(arr, 49) = -1
search(arr, 99) = 8
search(arr, 110) = -1
search(arr, 176) = 14
'''

''' Using LeetCode'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)
    
    def binary_search(self, nums, target, low, high):
        middle = low + (high - low) // 2
        if nums[middle] == target:
            return middle
        elif low > high:
            return -1
        elif nums[middle] < target:
            return self.binary_search(nums, target, middle + 1, high)
        else:
            return self.binary_search(nums, target, low, middle - 1)

'''
Your input
[-1,0,3,5,9,12]
9
Output
4
Expected
4

Runtime: 228 ms, faster than 90.85% of Python3 online submissions for Binary Search.
Memory Complexity - O(log n)
'''
