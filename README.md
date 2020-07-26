# 3D-Bin-Packing-Problem
This project aims at solving 3D-Bin-Packing problem, a combinatorial NP-hard problem.
The whole 3D Packing implementation based on the following two papers:
- Li, Xueping & Zhao, Zhaoxia & Zhang, Kaike. (2014). [A genetic algorithm for the three-dimensional bin packing problem with heterogeneous bins](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/Reference/3DBPP_ISERC_Final.revHEAD.pdf). IIE Annual Conference and Expo 2014. 
- Dube, Erick & Kanavathy, Leon & K@i, Leon & Za, Owave. (2006). [Optimizing Three-Dimensional Bin Packing Through Simulation](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/Reference/erick_dube_507-034.pdf). 

Download & Usage:
----------------

The code based on [enzoruiz](https://github.com/enzoruiz/3dbinpacking) implementation in Python. I made some improvements for better packing rate.

Download the whole [main_model](https://github.com/Janet-19/3d-bin-packing-problem/tree/master/main_model) folder. Open [example.ipynb](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/main_model/example.ipynb) in Jupyter Notebook to see an example. You can change any parameter in the file for your usage. If you use PyCharm, just change filename extension from .ipynb to .py.

**Basic parameters of items and bins:**

Here are some basic parameters that need your setup towards items and bins:
- Bin(name, length, width, height, capacity)
  - For each bin, you need to enter its name, length, width, height, and capacity (the maximum weight it can hold).
- Item(name, length, width, height, weight)
  - For each item, you need to enter its name, length, width, height, and weight.

**Basic usage of Packer class:**
1. Create a variable of Packer() class. Click [here](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/main_model/packer.ipynb) to see Packer() definition.
2. Use *packer.add_bin()* and *packer.add_item()* to add items that needed packing and optional box types. Then, use *packer.pack()* to perform the whole packing process.
3. After packing, fitted and unfitted items in each bin and the bin with the highest packing rate will be printed.

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
- <img src="https://render.githubusercontent.com/render/math?math=a_{im} %2B a_{mi} %2B b_{im} %2B b_{mi} %2B c_{im} %2B c_{mi} \geq 1, i \neq m">
- x-axis: <img src="https://render.githubusercontent.com/render/math?math=x_{i} %2B w_i(o_{i1} %2B o_{i4}) %2B l_i(o_{i2} %2B o_{i5}) %2B h_i(o_{i3} %2B o_{i6}) \leq x_{m} %2B M(1-a_{im}), i \neq m">
- y-axis: <img src="https://render.githubusercontent.com/render/math?math=y_{i} %2B l_i(o_{i1} %2B o_{i6}) %2B w_i(o_{i2} %2B o_{i3}) %2B h_i(o_{i4} %2B o_{i5}) \leq y_{m} %2B M(1-b_{im}), i \neq m">
- z-axis: <img src="https://render.githubusercontent.com/render/math?math=z_{i} %2B h_i(o_{i1} %2B o_{i2}) %2B l_i(o_{i3} %2B o_{i4}) %2B w_i(o_{i5} %2B o_{i6}) \leq z_{m} %2B M(1-c_{im}), i \neq m">

All items within the bin dimension:
- x-axis: <img src="https://render.githubusercontent.com/render/math?math=(x_{i} %2B w_i(o_{i1} %2B o_{i4}) %2B l_i(o_{i2} %2B o_{i5}) %2B h_i(o_{i3} %2B o_{i6})) x_{ij} \leq L_{j}">
- y-axis: <img src="https://render.githubusercontent.com/render/math?math=(y_{i} %2B l_i(o_{i1} %2B o_{i6}) %2B w_i(o_{i2} %2B o_{i3}) %2B h_i(o_{i4} %2B o_{i5})) x_{ij} \leq W_{j}">
- z-axis: <img src="https://render.githubusercontent.com/render/math?math=(z_{i} %2B h_i(o_{i1} %2B o_{i2}) %2B l_i(o_{i3} %2B o_{i4}) %2B w_i(o_{i5} %2B o_{i6})) x_{ij} \leq H_{j}">

One orientation of each item: <img src="https://render.githubusercontent.com/render/math?math=o_{i1} %2B o_{i2} %2B o_{i3} %2B o_{i4} %2B o_{i5} %2B o_{i6} = 1">

Basic Logic of 3D-Bin-Packing Model:
---------------------

The core logic of 3D-bin-packing model based on heuristic algorithm. To be specific:
- From a list of items, items are sorted from the biggest to the smallest and be placed in such ordering into a list of bins simultaneously.
- Orientation selection module: 
  - Each item has 1-6 orientations to choose when it can be placed into a certain bin. Orientation selection module can choose the best orientation type when facing several optinal orientations.
- Placement selection module: 
  - Here a pivot point is used to determine item's position. The pivot is an (x, y, z) coordinate which represents a point in a particular 3D bin at which an attempt to pack an item will be made. The back lower left corner of the item will be placed at the pivot. If the item cannot be packed at the pivot position then it is rotated until it can be packed at the pivot point or until we have tried all 6 possible rotation types. If after rotating it, the item still cannot be packed at the pivot point, then we move on to packing another item and add the unpacked item to a list of items that will be packed after an attempt to pack the remaining items is made. The first pivot in an empty bin is always (0,0,0). When one item can be placed into multiple optinal pivot point, placement selection module can help make a choice.
- Item stacking module:
  - Here I tried item stacking module when one item is being placed into a certain box. Item stacking module helps determin whether to stack similar items before placement action.
  - Since stacking module did not significantly increase the packing rate, I deleted it in the end.
- After all items in item list are placed into bins in bin list, the bin size with the highest packing rate will be chosen as final decision.

