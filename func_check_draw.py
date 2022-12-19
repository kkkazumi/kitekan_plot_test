import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("func_check.csv",delimiter=",")

color_list = ["blue","green","red"]

#for f in range(10):
#  for e in range(4):

for t in range(10):
    print("input func number from 0 to 9")
    f=int(input())
    print("input signal number from 0 to 3")
    e=int(input())
    for m in range(3):
        col_num = 12*f+3*e+m
        print(col_num)
        col_data = data[col_num,:]
        plt.plot(col_data,color=color_list[m])
    plt.show()
    plt.clf()

