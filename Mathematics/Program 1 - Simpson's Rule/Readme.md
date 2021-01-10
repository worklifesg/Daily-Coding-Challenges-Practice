### Program 1 - Coding Practice

---------------------------------------------------------------------------------------------------------------------------------------------------

***For a given dataset [x,y] on Receiver Operating Characteristics (ROC) curve, find the area under ROC using Simpson's Rule (Approximation with Parabola):***

- [ ] The function defined for calculation should have two input parameters X,Y (of array size N)
- [ ] Considering every k<sup>th</sup> point in dataset, estimate area under ROC curve.
- [ ] Can only use standard defined python libraries (No import allowed)

***Testing Case (General):***

* X = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
* Y = [0, 0.25, 0.33, 0.43, 0.56, 0.65, 0.77, 0.84, 0.87, 0.92, 1]
* The answer should be 0.614

***Testing Case (General):***

* X = [-4,-2,0,2,4,6,8]
* Y = [1,3,4,4,6,9,14]
* The answer should be 66

***Testing Case (e<sup>x</sup>) :***

* X = [0,0.25,0.5,0.75,1,1.25]
* Y = [1,1.2840,1.6487,2.1170,2.7183]
* The answer should be 1.7183

***Testing Case [ln(x)]:***

* X = [1,2,3,4,5]
* Y = [0,0.6931,1.0986,1.3863,1.6094]
* The answer should be 4.0414


