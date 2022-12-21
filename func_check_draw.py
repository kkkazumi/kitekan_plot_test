import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("func_check.csv",delimiter=",")

color_list = ["blue","green","red"]
label_list = ["sml","mid","big"]

#for f in range(10):
#  for e in range(4):

norm_val = [80,80,80,80,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        240,240,240,240,
        80,80,80,80,
        80,80,80,80]

def x_conv(x,func_num):
    if((func_num > 27) and (func_num<32)):
        conv_x = x * norm_val[func_num] - 80.0
    else:
        conv_x = x * norm_val[func_num]
    return conv_x

def get_xrange(func_num):
    x_max = norm_val[func_num]
    if((func_num > 27) and (func_num<32)):
        x_min = - 80
    else:
        x_min = 0
    return np.linspace(x_min,x_max,100) 

def draw_func(f,e,ax,show_flg=True,x_limit=None,y_limit=None):
    x = get_xrange(4*f+e)
    for m in range(3):
        col_num = 12*f+3*e+m
        print(col_num)
        col_data = data[col_num,:]
        ax.plot(x,col_data,color=color_list[m],label=label_list[m])
        if(y_limit is not None):
            x_max=xlim[1]
            x_min=xlim[0]
            np.where(xlim)
            print("ylim",y_limit)
            ax.set_ylim(y_limit)
        #else:
        #    ax.plot(x,col_data,color=color_list[m],label=label_list[m])
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


