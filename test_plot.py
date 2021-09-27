#!/usr/bin/env python
#! coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


print("hello world!")

%matplotlib inline
plt.plot(*np.random.randn(2, 1000))