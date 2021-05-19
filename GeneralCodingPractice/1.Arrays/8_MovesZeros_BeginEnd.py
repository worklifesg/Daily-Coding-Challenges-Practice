def moves_begin_zero(array):
    if len(array) < 1:
        return
    
    length = len(array)
    #we will assing the pointers of read and write index
    r_ind = length-1
    w_ind = length-1
    
    #creating a loop where if read index is not zero, the read index value is stored in write index and write index is decremented towards the start
    while(r_ind >=0):
        if array[r_ind] !=0:
            array[w_ind] = array[r_ind]
            w_ind-=1
        
        r_ind-=1
    
    #when write idnex is >0 after read_index reaches -1, all indices left in the begninning are assigned zero
    while(w_ind >=0):
        array[w_ind]=0
        w_ind-=1

def moves_end_zero(array):
    if len(array)<1:
        return
    length = len(array)
    r_ind = 0
    w_ind=0
    while(r_ind<=length-1):
        if array[r_ind] !=0:
            array[w_ind]=array[r_ind]
            w_ind+=1
        r_ind+=1
    while(w_ind<=length-1):
        array[w_ind]=0
        w_ind+=1

array = [1,2,0,5,0,4,0,6]
array1 = array.copy()
print('Original array: ',array)
moves_end_zero(array)
print('Moving all zeros to the end: ',array)
moves_begin_zero(array1)
print('Moving all zeros to the beginning: ',array1)

'''
Runtime Complexity: O(n) and Memory Complexity is constant O(1)
In LeetCode, the problem is to move all zeros to the end of the array and we used the above function to do it
Runtime: 52 ms, faster than 48.98% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.3 MB, less than 59.84% of Python3 online submissions for Move Zeroes.

Faster code for using for loop to read and write
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        r_ind = 0
        w_ind = 0
        for i in nums:
            if i == 0:
                r_ind += 1
            else:
                nums[w_ind] = i
                w_ind += 1

        while r_ind:
            nums[w_ind] = 0
            w_ind += 1
            r_ind -= 1  
 '''
Runtime: 48 ms, faster than 74.51% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 17.16% of Python3 online submissions for Move Zeroes.
 '''
