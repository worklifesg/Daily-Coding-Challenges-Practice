class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        #The problem is simple straight forward.
        # Lets say the first person arrives and sit at the kth position, then the person from 2 to k-1 will sit at the own positions somone else i.e. can and can't sit their seats i.e. prob is 0.5
        # So the last person is left with three options:
        # will definitely sit at their place, can't sit at their position and sit in the middle of k+1 to n. The last one will enter into loop so we avoid using it, so we are left two otions where the prob is 0.5
        #return 0.5 if n!=1 else 1.0
        x=[0.0]*2
        x[0]=1.0
        
        for i in range(2,n+1):
            x[(i-1)%2]=1.0/i+x[(i-2)%2]*(i-2)/i
        return x[(n-1)%2]
'''
Runtime: 792 ms, faster than 5.04% of Python3 online submissions for Airplane Seat Assignment Probability.
Memory Usage: 14.2 MB, less than 39.80% of Python3 online submissions for Airplane Seat Assignment Probability.
''' 
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        #The problem is simple straight forward.
        # Lets say the first person arrives and sit at the kth position, then the person from 2 to k-1 will sit at the own positions somone else i.e. can and can't sit their seats i.e. prob is 0.5
        # So the last person is left with three options:
        # will definitely sit at their place, can't sit at their position and sit in the middle of k+1 to n. The last one will enter into loop so we avoid using it, so we are left two otions where the prob is 0.5
        return 0.5 if n!=1 else 1.0
'''
Runtime: 32 ms, faster than 53.9% of Python3 online submissions for Airplane Seat Assignment Probability.
Memory Usage: 14.3 MB, less than 11.3% of Python3 online submissions for Airplane Seat Assignment Probability.
'''

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        #The problem is simple straight forward.
        # Lets say the first person arrives and sit at the kth position, then the person from 2 to k-1 will sit at the own positions somone else i.e. can and can't sit their seats i.e. prob is 0.5
        # So the last person is left with three options:
        # will definitely sit at their place, can't sit at their position and sit in the middle of k+1 to n. The last one will enter into loop so we avoid using it, so we are left two otions where the prob is 0.5
        #return 0.5 if n!=1 else 1.0
        #x=[0.0]*2
        #x[0]=1.0
        
        #for i in range(2,n+1):
         #   x[(i-1)%2]=1.0/i+x[(i-2)%2]*(i-2)/i
        #return x[(n-1)%2]
        
        return 1.0 if n==1 else 0.5

'''
Runtime: 28 ms, faster than 79.60% of Python3 online submissions for Airplane Seat Assignment Probability.
Memory Usage: 14 MB, less than 87.15% of Python3 online submissions for Airplane Seat Assignment Probability.
'''
