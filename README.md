# 3D-Bin-Packing-Problem
This project aims at solving 3D-Bin-Packing problem, a combinatorial NP-hard problem.
The whole 3D Packing implementation based on the following two papers:
- Li, Xueping & Zhao, Zhaoxia & Zhang, Kaike. (2014). [A genetic algorithm for the three-dimensional bin packing problem with heterogeneous bins](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/Reference/3DBPP_ISERC_Final.revHEAD.pdf). IIE Annual Conference and Expo 2014. 
- Dube, Erick & Kanavathy, Leon & K@i, Leon & Za, Owave. (2006). [Optimizing Three-Dimensional Bin Packing Through Simulation](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/Reference/erick_dube_507-034.pdf). 

Mathematical Formulation of 3D-Bin-Packing-Problem:
---------------------
**The following variables are used for the mathematical formulation:**

<img src="https://render.githubusercontent.com/render/math?math=n"> = number of items, 
<img src="https://render.githubusercontent.com/render/math?math=UB=n"> = maximum number of bins

<img src="https://render.githubusercontent.com/render/math?math=x_{ij} = 1"> if item <img src="https://render.githubusercontent.com/render/math?math=i"> is assigned to bin <img src="https://render.githubusercontent.com/render/math?math=j">, otherwise 
<img src="https://render.githubusercontent.com/render/math?math=x_{ij} = 0"> for 
<img src="https://render.githubusercontent.com/render/math?math=i = 0, ..., n-1, j = 0, ..., UB - 1">

<img src="https://render.githubusercontent.com/render/math?math=y_{j} = 1"> if bin <img src="https://render.githubusercontent.com/render/math?math=j"> is used, otherwise 
<img src="https://render.githubusercontent.com/render/math?math=y_{j} = 0"> for 
<img src="https://render.githubusercontent.com/render/math?math=j = 0, ..., UB - 1">

<img src="https://render.githubusercontent.com/render/math?math=(l_{i}, w_{i}, h_{i})">: parameters indicating the length, width, and height of item 
<img src="https://render.githubusercontent.com/render/math?math=i">

<img src="https://render.githubusercontent.com/render/math?math=(L_{j}, W_{j}, H_{j})">: parameters indicating the length, width, and height of bin 
<img src="https://render.githubusercontent.com/render/math?math=j">

<img src="https://render.githubusercontent.com/render/math?math=c_{i}">: weight of item <img src="https://render.githubusercontent.com/render/math?math=i">, 
<img src="https://render.githubusercontent.com/render/math?math=C_{j}">: capacity of bin <img src="https://render.githubusercontent.com/render/math?math=j">

<img src="https://render.githubusercontent.com/render/math?math=(x_{i}, y_{i}, z_{i})">: continuous variables for coordinates of item 
<img src="https://render.githubusercontent.com/render/math?math=i">'s left-bottom-behind corner

<img src="https://render.githubusercontent.com/render/math?math=M">: a large enough number

<img src="https://render.githubusercontent.com/render/math?math=o_{i1}, o_{i2}, o_{i3}, o_{i4}, o_{i5}, o_{i6}">: binary variables, indicating orientations of item 
<img src="https://render.githubusercontent.com/render/math?math=i">. The values equal to 1 if item <img src="https://render.githubusercontent.com/render/math?math=i"> has orientation <img src="https://render.githubusercontent.com/render/math?math=1, 2, 3, 4, 5, 6">, respectively, otherwise equal to 0. The figure below shows 6 orientations of one item:
![Image 1](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/Reference/6%20ways%20of%20placing.jpg)

<img src="https://render.githubusercontent.com/render/math?math=a_{im}, b_{im}, c_{im}">: binary variables, indicating the relative placement of item 
<img src="https://render.githubusercontent.com/render/math?math=i"> to item <img src="https://render.githubusercontent.com/render/math?math=m">, variables will be 1 if item <img src="https://render.githubusercontent.com/render/math?math=i"> is to the right of, in front of, or on the top of item 
<img src="https://render.githubusercontent.com/render/math?math=m">, respectively; otherwise, 0. The figure below shows non-intersection conditions of two items:
![Image 2](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/Reference/Non-intersection%20conditions.png)

**The objective is to maximize the packing rate of the variable bin:**
<img src="https://render.githubusercontent.com/render/math?math=\max \frac{\sum_{0}^{UB-1}(l_{i} \times w_{i} \times h_{i})x_{ij}}{(L_{j} \times W_{j} \times H_{j})}">

**The constraints are as follows:**

Each item in one bin: <img src="https://render.githubusercontent.com/render/math?math=\sum_{j=0}^{UB-1} x_{ij} = 1">

Capacity constraint of each bin: <img src="https://render.githubusercontent.com/render/math?math=\sum_{i=0}^{UB-1} c_{i} x_{ij} \leq C_{j} y_{j}"> 

Non-intersection between two items: 
- <img src="https://render.githubusercontent.com/render/math?math=a_{im} %2B b_{im} %2B c_{im} = 1">
- x-axis: <img src="https://render.githubusercontent.com/render/math?math=x_{i} %2B w_i(o_{i1} %2B o_{i4}) %2B l_i(o_{i2} %2B o_{i5}) %2B h_i(o_{i3} %2B o_{i6}) \leq x_{m} %2B M(1-a_{im}), i \neq m">
- y-axis: <img src="https://render.githubusercontent.com/render/math?math=y_{i} %2B l_i(o_{i1} %2B o_{i6}) %2B w_i(o_{i2} %2B o_{i3}) %2B h_i(o_{i4} %2B o_{i5}) \leq y_{m} %2B M(1-b_{im}), i \neq m">
- z-axis: <img src="https://render.githubusercontent.com/render/math?math=z_{i} %2B h_i(o_{i1} %2B o_{i2}) %2B l_i(o_{i3} %2B o_{i4}) %2B w_i(o_{i5} %2B o_{i6}) \leq z_{m} %2B M(1-c_{im}), i \neq m">

All items within the bin dimension:
- x-axis:
- y-axis:
- z-axis:

Basic Logic of 3D-Bin-Packing Model:
---------------------
The core logic of this model is heuristic algorithm. To be specific, a list of items are placed into various sizes of bins simultaneously.
