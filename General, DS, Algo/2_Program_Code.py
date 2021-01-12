def solution(dataset):
    split_class = dict() #defining the dictionary to store values and labels
    for i in range(len(dataset)): #loop to check each value and associated label 
        values = dataset[i]
        label = values[-1]
        if (label not in split_class): #to create a label dictionary inside split_class
            split_class[label] = list()
        split_class[label].append(values) #store values inside the associated labels
    return split_class

'''
dataset = [[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 2], [8, 8, 2], [9, 9, 2]]
print(solution(dataset))

Output:
{0: [[1, 1, 0], [2, 2, 0], [3, 3, 0]], 1: [[4, 4, 1], [5, 5, 1], [6, 6, 1]], 2: [[7, 7, 2], [8, 8, 2], [9, 9, 2]]}
'''
