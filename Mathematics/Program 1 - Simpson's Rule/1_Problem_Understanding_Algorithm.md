### Problem Understanding and Algorithm Flow

* To write a code for this problem, mathematical equation for Simpson's rule is important to know. 
* Here we are talking about Simpson's 1/3 integration rule (Parabolic Approximation)
* Area under the curve (parabola) equation for one area block can be found by

<h3 align='center'>
<img src="http://latex.codecogs.com/gif.latex?\dpi{110}&space;A_k=\frac{1}{3}\Delta&space;x&space;[f(x_k)&plus;4f(x_k&plus;h)&plus;f(x_k&plus;2h)]" title="http://latex.codecogs.com/gif.latex?\dpi{110} A_k=\frac{1}{3}\Delta x [f(x_k)+4f(x_k+h)+f(x_k+2h)]" />
</h3>

where ![1](https://latex.codecogs.com/gif.latex?\Delta&space;x) is the difference of consecutive ***![1](https://latex.codecogs.com/gif.latex?x_k) datapoints***

Moreover, ![1](https://latex.codecogs.com/gif.latex?f(x)) represents the ***y values***

***Integration can be found as sum of area under the curve and can be defined as following:***

<h3 align='center'>
<img src="http://latex.codecogs.com/gif.latex?\dpi{110}&space;I&space;\cong&space;\sum&space;A_k&space;=&space;\frac{1}{3}\Delta&space;x\sum_{i=1}^{N/2}[f(x_{2i-2})&plus;4f(x_{2i-1})&plus;f(x_{2i})]" title="http://latex.codecogs.com/gif.latex?\dpi{110} I \cong \sum A_k = \frac{1}{3}\Delta x\sum_{i=1}^{N/2}[f(x_{2i-2})+4f(x_{2i-1})+f(x_{2i})]" />
</h3>

**For Instance:**

For Y = [1,3,4,4,6,9,14] I can choose for (let's say i=1):

* ![](http://latex.codecogs.com/gif.latex?\dpi{110}&space;f(x_{2i-2})) means Y[0] = 1
* ![](http://latex.codecogs.com/gif.latex?\dpi{110}&space;f(x_{2i-1})) means Y[1] = 3
* ![](http://latex.codecogs.com/gif.latex?\dpi{110}&space;f(x_{2i})) means Y[2] = 4

For i = 2

* ![](http://latex.codecogs.com/gif.latex?\dpi{110}&space;f(x_{2i-2})) means Y[2] = 4
* ![](http://latex.codecogs.com/gif.latex?\dpi{110}&space;f(x_{2i-1})) means Y[3] = 4
* ![](http://latex.codecogs.com/gif.latex?\dpi{110}&space;f(x_{2i})) means Y[4] = 6

And so on...So the to implement this function we need to divide our dataset is a set of three values, so the final tuple looks like:

```
([1,3,4],[4,4,6],[6,9,14])
```
----------------------------------------------------------------------------------------------------------------------------------------------------------------

**Algorithm Flow**

- [ ] Find ![1](https://latex.codecogs.com/gif.latex?\Delta&space;x)  between consecutive x datapoints using ```zip``` method
- [ ] Create a tuple for y values as indicated above
- [ ] Compute the function ![](http://latex.codecogs.com/gif.latex?\dpi{110}&space;\frac{[f(x_{2i-2})&plus;4f(x_{2i-1})&plus;f(x_{2i})]}{3})
- [ ] Multiply the above function with the ![1](https://latex.codecogs.com/gif.latex?\Delta&space;x) for every index (```for```) and store the result
- [ ] Return the final computed result
