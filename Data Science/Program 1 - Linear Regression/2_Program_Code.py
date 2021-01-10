def solution(dataset):
    # storing x,y values from dataset
    x= [row[0] for row in dataset]
    y= [row[1] for row in dataset]

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

    return[b0, b1]
    
'''
Testing:

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
b0,b1 = solution(dataset)
print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))

Output --> Coefficients: B0=0.400, B1=0.800

'''
