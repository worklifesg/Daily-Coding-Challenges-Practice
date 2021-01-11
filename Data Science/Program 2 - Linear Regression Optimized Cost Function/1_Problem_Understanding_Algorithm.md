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

Using computed coefficients ```b0, b1```, we can calculate ```h(x)```. Here it is same as ```y(x)``` but to avoid confusion we use different term.

<h3 align='center'>
<img src="http://latex.codecogs.com/gif.latex?\dpi{110}&space;h(x)&space;=&space;b_0&plus;b_1&space;x" title="http://latex.codecogs.com/gif.latex?\dpi{110} h(x) = b_0+b_1 x" />
</h3>

The cost function ```J(x)``` is defined as: 
<h3 align='center'>
<img src="http://latex.codecogs.com/gif.latex?\dpi{110}&space;J(x)&space;=&space;\frac{1}{2m}&space;\sum_{i=1}^m(h(x)_i-y_i)^2" title="http://latex.codecogs.com/gif.latex?\dpi{110} J(x) = \frac{1}{2m} \sum_{i=1}^m(h(x)_i-y_i)^2" />
</h3>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

**Algorithm Flow:**

- [ ] The objective here is to find optimized coefficients that will yield minimized cost function
- [ ] Input dataset in form of x and y and store x values and y values separately
- [ ] Define sub functions for **mean, variance, and covariance**
- [ ] Use these sub functions to compute ```b0, b1```
- [ ] Using ```b0, b1``` find ```h(x)``` and using ```h(x)``` find the cost function
