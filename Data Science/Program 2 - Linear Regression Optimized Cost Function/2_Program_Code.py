def solution(dataset):
    m = len(dataset) # number of x,y paris in our training set

    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]

    #mean sub-function
    def mean(values):
        return sum(values)/float(len(values))
    #variance sub-function
    def variance(values,mean):
        return sum([(x-mean)**2 for x in values])
    #covariance sub-function
    def covar(x,mean_x,y,mean_y):
        covar=0.0
        #loop to store the covariance function of each ith values
        for i in range(len(x)):
            covar += (x[i]-mean_x)*(y[i]-mean_y)
        return covar
    
    #computing mean of x,y
    x_mean = mean(x)
    y_mean = mean(y)

    #computing b1
    b1 = covar(x,x_mean,y,y_mean) / variance(x, x_mean)

    #using b1, computing b0
    b0 = y_mean - b1*x_mean

    h=[] #defining an empty array to store y(x) for a line using b0 and b1

    for i in range(len(x)): #loop to store all line values
        func= b0+b1*x[i]
        h.append(func)
    
    sum_func =[] #defining empty array to sum the internal cost function equation
    for k in range(len(y)): #loop to compute summation term
        func2=(h[k]-y[k])**2
        sum_func.append(func2)

    total_sum = sum(sum_func) #total sum for all terms
    cost_function = (1/(2*m))*total_sum #cost function

    return cost_function

'''
Test cases:

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
print('Result of cost function is: ',solution(dataset))

Result of cost function is:  0.2400000000000001

dataset = [[2, 1], [2, 4], [5, 4], [5, 8], [9, 8], [9, 11]]
print('Result of cost function is: ',solution(dataset))

Result of cost function is:  1.4442567567567566
'''
