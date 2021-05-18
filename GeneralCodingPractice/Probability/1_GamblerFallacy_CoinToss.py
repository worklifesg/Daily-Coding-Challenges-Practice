########### Gambler Fallacy Coding #############
'''
Write a function that computes fair coin toss total number of heads and tails for k times tosses

In this problem, consider a "fair" coin toss which is iid (independent identical distributed) which means that every coin toss is indepedent of each other and probability of heads or tails for every toss is the same.
Thus we can say p(H)=p(T)=0.5

So there are two possible solutions:
    1. "Fair" coin toss means if toss is performed k times then we can expect k/2 heads and k/2 tails,
        assuming that the past is not given.
    2. If past is given or fized then forst solution is not applicable anymore, thus the probabilities of head 
       and tails is calculated from the future remainder tosses and added to the past to identify the total 
       number of heads and tails.
'''

def gamblerfallacy(past,k):
    #if past[0]==0:
        #if past[1]==0:
            #past_H=k/2
            #past_T=k/2
    past_H = past[0]+(k-(past[0]+past[1]))/2
    past_T = past[1]+(k-(past[0]+past[1]))/2
    #if past=[0,0] then past_H=past_T and is reduced to k/2
    return past_H,past_T

# Test Cases

past=[80,20]
k=200
print("The total number of heads and tails after %f tosses are %f and %f respectively"%(k,gamblerfallacy(past,k)[0],gamblerfallacy(past,k)[1]))

'''
Finished in 32 ms
The total number of heads and tails after 200.000000 tosses are 130.000000 and 70.000000 respectively
'''
