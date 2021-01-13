def solution(dataset, a, b, c):
    result=[] #initialize empty matrix to store transformed values
    for i in range(len(dataset)): #loop to solve equation for each value of x
        sol=a*(dataset[i]**2)+b*dataset[i]+c
        result.append(sol)  #store f(x) values in result array
    b = sorted(result) #sort array by default ascending order
    return b, min(b) #return sorted array and minimum value in sorted array

'''
dataset = [-4,-3,-2,2,3,4]
result_final = solution(dataset,-1,3,5)
print(result_final)
'''
