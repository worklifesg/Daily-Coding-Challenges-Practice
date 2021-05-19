class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        if k < 0:
            k=k+length
        
        self.reverse_array(nums,0,length-1)
        self.reverse_array(nums,0,k-1)
        self.reverse_array(nums,k,length-1)
        
    
    def reverse_array(self,arr, start, end):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start+=1
            end-=1
'''
Your input
[1,2,3,4,5,6,7]
3
[-1,-100,3,99]
2
Output
[5,6,7,1,2,3,4]
[3,99,-1,-100]
Expected
[5,6,7,1,2,3,4]
[3,99,-1,-100]

Runtime: 220 ms, faster than 45.03% of Python3 online submissions for Rotate Array.
Memory Usage: 25.4 MB, less than 67.08% of Python3 online submissions for Rotate Array
'''
