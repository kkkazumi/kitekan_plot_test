import numpy as np
import matplotlib.pyplot as plt


color_list = ["blue","green","red"]
label_list = ["low mood","medium mood","high mood"]
linestyle_list = ["dashdot","dashed","solid"]

quiz_new_val = [80,80,80,80,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        240,240,240,240,
        1,1,1,1,10,10,10,10,
        10,10,10,10,10,10,10,10,
        10,10,10,10,10,10,10,10,
        5,5,5,5]

quiz_norm_val = [80,80,80,80,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,
        240,240,240,240,
        80,80,80,80,
        80,80,80,80]

#TODO define bono_norm_val
bono_norm_val = [1,1,1,1,
        1,1,1,1]

def get_data(mode):
    if(mode=="quiz"):
        data = np.loadtxt("func_check.csv",delimiter=",")
    elif(mode=="quiz_new"):
        data = np.loadtxt("func_check.csv",delimiter=",")
    elif(mode=="bono"):
        data = np.loadtxt("func_check_bono.csv",delimiter=",")
    return data

def x_conv(mode,x,func_num):
    if(mode=="quiz"):
        if((func_num > 27) and (func_num<32)):
            conv_x = x * quiz_norm_val[func_num] - 80.0
        else:
            conv_x = x * quiz_norm_val[func_num]
    elif(mode=="quiz_new"):
        if((func_num > 27) and (func_num<32)):
            conv_x = x * quiz_new_val[func_num] - 80.0
        else:
            conv_x = x * quiz_new_val[func_num]
    elif(mode=="bono"):
        #conv_x = x * bono_norm_val[func_num]
        conv_x = x
    return conv_x

def get_xrange(mode,func_num):
    if(mode=="quiz"):
        x_max = quiz_norm_val[func_num]
        if((func_num > 27) and (func_num<32)):
            x_min = - 80
        else:
            x_min = 0
    else:
        x_max = 1
        x_min = 0

    return np.linspace(x_min,x_max,100) 

def draw_func(mode,f,e,ax,show_flg=True,x_limit=None,y_limit=None):
    data=get_data(mode)
    x = get_xrange(mode,4*f+e)
    for m in range(3):
        col_num = 12*f+3*e+m
        print(col_num)
        col_data = data[col_num,:]
        ax.plot(x,col_data,color=color_list[m],label=label_list[m],linestyle=linestyle_list[m])
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
    print("input mode: \"quiz\" or \"bono\"")
    mode=input()
    
    for t in range(10):
        fig, ax = plt.subplots(figsize = (8,6))
        print("input func number from 0 to 9")
        f=int(input())
        print("input signal number from 0 to 3")
        e=int(input())
        draw_func(mode,f,e,ax)


