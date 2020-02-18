# masksemi
Code for converting a label list in a scikit-like semi-supervised label list.

## Getting Started
#### Dependencies
You need Python 3.7 or later to use **masksemi**. You can find it at [python.org](https://www.python.org/).

You also need numpy package, which is available from [PyPI](https://pypi.org). If you have pip, just run:
```
pip install numpy
```
#### Installation
Clone this repo to your local machine using:
```
git clone https://github.com/caiocarneloz/masksemi.git
```

#### Features
Given the label list and a certain percentage, mask the amount of unlabeled data based on percentage and also encode the data for scikit usage with semi-supervised models. The percentage split is considered by class. This way, all classes will have the given percentage as labeled data.

#### Usage
Considering iris dataset labels:
```
array(['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
       'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
        ...,
       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',
       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',
       'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',
        ...,
       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',
       'Iris-virginica', 'Iris-virginica', 'Iris-virginica',
       'Iris-virginica', 'Iris-virginica', ...], dtype=object)
```
The maskData function is called by passing labels and the percentage of labeled data:
```
masked_labels = maskData(labels, 0.1)
```
The labels are encoded and masked:
```
array([-1, -1, -1,  0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0,
       -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1,
       -1,  0,  0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
       -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1,  1, -1,
       -1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1,
       -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1,
       -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1,
       -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  2,  2, -1, -1,
       -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  2])
```
