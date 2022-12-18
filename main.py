import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
import scipy
from scikit.learn import sklearn


def main():
  #csv_file_name = input ("The name of the csv file:")

  df = pd.read_csv("cart_incline_energy.csv")  #reads the file
  print(df)
  time = df["time"]
  force = df["force"]
  plt.figure()
  plt.plot(time, force)
  plt.show()


def regression(x, y):
  regtype = input(
    "regression line? (linear, ln, quadratic, exponential, other)")
  if regtype == "linear":
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression().fit(time, force)
    reg.score(time, force)
    reg.coef_
    reg.intercept_

    #a, b = np.polyfit(x, y, 1)
    #plt.plot(x, a*x+b)
  elif regtype == "quadratic":
    a, b, c = np.ployfit(x, y, 2)
    plt.plot(x, a * x * x + b * x + c)
  elif regtype == "ln":
    popt, pcov = scipy.optimize.curve_fit(lambda t, a, b: a + b * np.log(t), x,
                                          y)

    plt.plot(x, popt[0] + popt[1] * np.log(x))

  plt.scatter(x, y, 'red')
  plt.show()


if __name__ == '__main__':
  #direction = input ("The file diretory of the csv file:")
  #os.getcwd()
  #os.chdir(direction)
  regression(np.array([1, 2, 4, 8, 16]), np.array([1, 2, 3, 4, 5]))
  main()
