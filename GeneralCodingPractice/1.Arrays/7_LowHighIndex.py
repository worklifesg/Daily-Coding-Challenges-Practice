def index(true_param,array,key):
    low = 0
    high = len(array)-1
    mid = int(high/2)
    
    if true_param == 1:
        while low <= high:
            mid_elem = array[mid]

            if mid_elem < key:
                low = mid+1
            else:
                high = mid-1

            mid = low+int((high-low)/2)

        if low < len(array) and array[low] == key:
            return low
    if true_param == 2:
        while low <= high:
            mid_elem = array[mid]

            if mid_elem <= key:
                low = mid+1
            else:
                high = mid-1

            mid = low+int((high-low)/2)
        if high == -1:
            return high
        if high < len(array) and array[high] == key:
            return high
    return -1

array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
key = 2
low = index(1,array,key)
high = index(2,array,key)

print("Low Index of " + str(key) + ": " + str(low))
print("High Index of " + str(key) + ": " + str(high))
