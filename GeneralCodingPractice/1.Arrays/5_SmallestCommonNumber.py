def smallest_common_number(array1,array2,array3):
    #iterators pointers
    i=0
    j=0
    k=0
    
    while i < len(array1) and j < len(array2) and k < len(array3):
        #smallest common number condition when the value at index for each array is same
        if array1[i] == array2[j] and array2[j] == array3[k]:
            return array1[i]
        
        #if not same then the array with smallest value moves to the next index
        
        if array1[i] < array2[j] and array1[i] < array3[k]:
            i+=1
        if array2[i] < array1[j] and array2[i] < array3[k]:
            j+=1
        if array3[i] < array1[j] and array3[i] < array2[k]:
            k+=1
    return -1

### Test case

array1 = [1,2,3]
array2 = [3,4,5]
array3 = [3,4,8]

print('The smallest common number is %d'%(smallest_common_number(array1,array2,array3)))

'''
Finished in 28 ms
The smallest common number is 3

'''
