class NotSoRandom(object):
    def seed(self, a):
        """Seed the world's most mysterious random number generator."""
        self.seedval = a
    def random(self):
        """Look, random numbers!"""
        self.seedval = (self.seedval * 3) % 19
        return self.seedval

    def dataset_generation(self,n1,n2,nums): #n1 seed for x and n2 seed for y

        #generated x,y values
        seed(n1)
        x = [random() for _ in range(nums)]
        seed(n2)
        y = [random() for _ in range(nums)]
        #max values for x,y
        max_x=max(x)
        max_y=max(y)
        #loop for normalization
        for i in range(len(x)):
            x[i]=round((x[i]/max_x),2)
            y[i]=round((y[i]/max_y),2)
        #dataset creation
        dataset = []
        for row in range(len(x)):
            dataset.append([x[row],y[row]])
        
        return dataset
'''
#declaring the functions in the class
_inst = NotSoRandom()
seed = _inst.seed
random = _inst.random
dataset_generation=_inst.dataset_generation

print(dataset_generation(42,21,5))
[[0.71, 0.33], [1.0, 1.0], [0.76, 0.89], [0.06, 0.56], [0.18, 0.61]]
'''
