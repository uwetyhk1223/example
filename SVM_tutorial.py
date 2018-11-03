import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

print(digits.data)

print(digits.target)

print(digits.images[0])
