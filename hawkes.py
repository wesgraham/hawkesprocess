# -*- coding: utf-8 -*-
"""hawkes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dGk7paj8x2oULAFlWT8V2-ejU1U1ui54
"""

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def david_hawkes(lambda_0, alpha, beta, T, i, t):
  k = 0
  lambda_star = lambda_0
  while k <= i:
    lambda_star = lambda_star + alpha*np.exp(-beta*(t - T[k]))
    k = k +1
  return lambda_star

def wes_hawkes(lambda_0, alpha, beta, bigTboi):
  if beta<=alpha:
    print("you messed up bro")
  else:
    t = 0
    i = 0
    k = 0
    x = 0
    T = [0]
    while(t < bigTboi):
      if i >= 1: 
        lambda_star = david_hawkes(lambda_0, alpha, beta, T, i ,t)
        u_hat = np.random.sample()
        squiggly = -np.log(u_hat)/lambda_star
        t = t + squiggly
        u = np.random.sample()
        if(u <= (david_hawkes(lambda_0, alpha, beta, T, i, t)/lambda_star)):
          i = i + 1
          T.append(t)
      else:
        lambda_star = lambda_0
        u_hat = np.random.sample()
        squiggly = -np.log(u_hat)/lambda_star
        t = t + squiggly
        i = i + 1
        T.append(t)

    if T[-1] <= bigTboi:
      return T
    else:
      return T[:-1]

y = wes_hawkes(0.2, 0.4, 0.5, 100)
y

plt.scatter(y)

