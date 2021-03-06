### Program 1 - Coding Practice ![](https://img.shields.io/badge/Level-Easy-green)

---------------------------------------------------------------------------------------------------------------------------------------------------

*Write a function that can split the data by its labels or class values*

- [ ] The function defined should have only one input parameter - ***dataset***
- [ ] Assumption: The last value in the dataset is the class value 
- [ ] Can only use standard defined python libraries (No import libraries allowed)
- [ ] Must work for multi-class dataset as well.

***Testing Case (General):***
* dataset = [[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 1], [5, 5, 1], [6, 6, 1]]
* Result is: 
  ```
  {0: [[1, 1, 0], [2, 2, 0], [3, 3, 0]], 1: [[4, 4, 1], [5, 5, 1], [6, 6, 1]]}
  ```
* dataset = [[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 2], [8, 8, 2], [9, 9, 2]]
* Result is:
  ```
  {0: [[1, 1, 0], [2, 2, 0], [3, 3, 0]], 1: [[4, 4, 1], [5, 5, 1], [6, 6, 1]], 2: [[7, 7, 2], [8, 8, 2], [9, 9, 2]]}
  ```
------------------------------------------------------------------------------------------------------------------------------------------------

***Links:***

[Problem Understanding and Algorithm Flow](https://github.com/worklifesg/Daily-Coding-Challenges-Practice/blob/main/General%2C%20DS%2C%20Algo/Progam%201%20-%20Split%20values%20by%20class/1_Problem_Understanding_Algorithm.md)

[Program Code](https://github.com/worklifesg/Daily-Coding-Challenges-Practice/blob/main/General%2C%20DS%2C%20Algo/Progam%201%20-%20Split%20values%20by%20class/2_Program_Code.py)
