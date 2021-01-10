### Problem Understanding and Algorithm Flow

* To write a code for this problem, concepts related to computing mean, variance and covariance is needed.
* A function is defined where it takes dataset (x,y) as input parameters and various sub-functions are defined for mean, variance and covariance
* **The mean of values is defined as:**

<h3 align='center'>
<img src="http://latex.codecogs.com/svg.latex?x_{mean}=\frac{\sum_{i=1}x_i}{count(x)}" title="http://latex.codecogs.com/svg.latex?x_{mean}=\frac{\sum_{i=1}x_i}{count(x)}" />
</h3>

* **The variance of dataset is defined as:**

<h3 align='center'>
<img src="http://latex.codecogs.com/svg.latex?variance&space;=&space;\sum_{i=1}^n&space;(x_i-x_{mean})^2" title="http://latex.codecogs.com/svg.latex?variance = \sum_{i=1}^n (x_i-x_{mean})^2" />
</h3>

* **The covariance is defined as:**

<h3 align='center'>
<img src="http://latex.codecogs.com/svg.latex?covariance&space;=&space;\sum_{i=1}^n&space;[(x_i-x_{mean})\times(y_i-y_{mean})]" title="http://latex.codecogs.com/svg.latex?covariance = \sum_{i=1}^n [(x_i-x_{mean})\times(y_i-y_{mean})]" />
</h3>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Using simple linear regression techniques, the coefficients ```b0, b1``` are computed as follows:

<h3 align='center'>
<img src="http://latex.codecogs.com/svg.latex?b_1&space;=&space;\frac{covariance}{variance}&space;=&space;\frac{\sum_{i=1}^n&space;[(x_i-x_{mean})\times(y_i-y_{mean})]}{\sum_{i=1}^n&space;(x_i-x_{mean})^2}" title="http://latex.codecogs.com/svg.latex?b_1 = \frac{covariance}{variance} = \frac{\sum_{i=1}^n [(x_i-x_{mean})\times(y_i-y_{mean})]}{\sum_{i=1}^n (x_i-x_{mean})^2}" />
</h3>

<h3 align='center'>
<img src="http://latex.codecogs.com/gif.latex?\dpi{110}&space;b_0&space;=&space;y_{mean}-b_1&space;\times&space;x_{mean}" title="http://latex.codecogs.com/gif.latex?\dpi{110} b_0 = y_{mean}-b_1 \times x_{mean}" />
</h3>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

**Algorithm Flow:**

- [ ] Input dataset in form of x and y and store x values and y values separately
- [ ] Define sub functions for **mean, variance, and covariance**
- [ ] Use these sub functions to compute ```b0, b1```
- [ ] Variance sub-function will need input values and mean sub-function
- [ ] Covariance sub-function will require both input values and both input parameters mean values
