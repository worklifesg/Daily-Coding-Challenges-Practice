### Program 2 - Coding Practice ![](https://img.shields.io/badge/Level-Medium-yellow)

---------------------------------------------------------------------------------------------------------------------------------------------------

*Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form ![](http://latex.codecogs.com/gif.latex?\dpi{110}&space;f(x)&space;=&space;a&space;x^2&plus;b&space;x&space;&plus;c) to each element x in the array.*

**The returned array must be in sorted order and should also return the minimum value obtained.**

- [ ] The function defined should have only <b> 4 </b> input parameters - ***dataset, a, b, c***
- [ ] Sorting function must be applied inside the function and not with the testing case
- [ ] Can only use standard defined python libraries (No import libraries allowed)

***Testing Case (General):***
* dataset = [-4,-3,-2,2,3,4] with a =1 , b = 3 , c = 5
* Result is: 
  ```
  ([3, 5, 9, 15, 23, 33], 3)
  ```
* dataset = [-4,-3,-2,2,3,4] with a =-1 , b = 3 , c = 5
* Result is:
  ```
  ([-23, -13, -5, 1, 5, 7], -23)
  ```
------------------------------------------------------------------------------------------------------------------------------------------------
