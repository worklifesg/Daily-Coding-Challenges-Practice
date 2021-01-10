def solution(X,Y):
    '''
    By taking X[:-1] we remove the last value and by taking X[1:], we remove 
    first value and then zip them to create lists of consecutive value
    '''
    x_diff = [x_i-x_k for x_k,x_i in zip(X[:-1],X[1:])] #difference of consecutive values
    y_list=tuple(Y[i:i+3] for i in range(0,len(Y),2)) #create a list of functions as defined (i-1, i-1, i)
    y_list_updated=y_list[:-1] #last index value is extra value which is not needed
    '''
    Evaluating the function
    '''
    y_avg = [(y_list_updated[i][0]+4*y_list_updated[i][1]+y_list_updated[i][2])/3 for i in range(len(y_list_updated))] 
    '''
    Defining the result variable to store the computed area udner the curve.
    Using the for loop for both x_diff and the function for y values we multiply them and add to the result.
    '''
    result = 0
    for i in range(len(x_diff)):
        for k in range(len(y_avg)):
            result+=(x_diff[i]*y_avg[k])
        return result
