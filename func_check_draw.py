import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("func_check.csv",delimiter=",")

color_list = ["blue","green","red"]

#for f in range(10):
#  for e in range(4):

norm_val = [80,80,80,80,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        240,240,240,240,
        80,80,80,80,
        80,80,80,80]

def get_xrange(func_num):
    x_max = norm_val[func_num]
    if((func_num > 27) and (func_num<32)):
        x_min = - 80
    else:
        x_min = 0
    return np.linspace(x_min,x_max,100) 

def draw_func(f,e,show_flg=True):
    x = get_xrange(4*f+e)
    for m in range(3):
        col_num = 12*f+3*e+m
        print(col_num)
        col_data = data[col_num,:]
        plt.plot(x,col_data,color=color_list[m])
    if(show_flg == True):
        plt.show()
        plt.clf()

if __name__ == '__main__':
    for t in range(10):
        print("input func number from 0 to 9")
        f=int(input())
        print("input signal number from 0 to 3")
        e=int(input())
        draw_func(f,e)


