import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd
from func_check_draw import draw_func,x_conv
from adjustText import adjust_text
from change_kitekan import check_kitekan

mode="quiz_new"

USER_NUM = 1 
FACTOR_NUM =15 
FACE_TYPE = 4

DIR_PATH = "./new_factor_test/"
face_type_list=["happy","surprised","angry","sad"]
factor_type_list=["trial num","rate of win","rate of encourage behavior","rate of sympathetic behavior", "rate of teasing behavior","rate of un-related behavior","rate of no behavior","total point","win-lose","num of encourage behavior","num of sympathetic behavior", "num of teasing behavior","num of un-related behavior","num of no behavior","motion-intensity"]

def annotate_eq(res,ax,position,color):
  a="{:.2f}".format(res[0])
  b="{:.2f}".format(res[1])
  c="{:.2f}".format(res[2])
  equ=str(a)+"x^2 + "+str(b)+"x + "+str(c)
  print(equ)
  ax.annotate(equ,xy=position,size=10,color=color)

def get_data(username):
  factor_file = DIR_PATH+str(username)+"/factor_before.csv"
  signal_file = DIR_PATH+str(username)+"/signal_before.csv"
  mental_file = DIR_PATH+str(username)+"/kibun_before.csv"
  factor_data = np.loadtxt(factor_file,delimiter="\t")
  signal_data = np.loadtxt(signal_file,delimiter="\t")
  mental_data = np.loadtxt(mental_file,delimiter="\t")
  df_mental = pd.DataFrame(mental_data,columns=["mental"])
  return factor_data,signal_data,mental_data,df_mental

#def ret_data(x_data,y_data,mental_data):
def ret_data(df,func_num):
  ##sorted x and y
  x_data=np.array(df["factor"])+0.0001
  y_data=np.array(df["signal"])
  mental_data=np.array(df["mental"])

  x_data_2=x_data[np.argsort(x_data)]
  y_data_2=y_data[np.argsort(x_data)]
  mental_2=mental_data[np.argsort(x_data)]

  res = np.polyfit(x_data_2,y_data_2,2)
  x=x_conv(mode,np.linspace(0,1,100),func_num)
  y_res=np.poly1d(res)(x)
  return res,x_data_2,y_data_2,y_res

def plot_observed_data(x,y,ax):
  x_sml,x_mid,x_big=x
  y_sml,y_mid,y_big=y
  ax.scatter(x_sml,y_sml,color='blue',alpha=0.5,marker="x",label="low mood("+str(len(x_sml))+"dots)")
  ax.scatter(x_mid,y_mid,color='green',alpha=0.5,marker="^",label="medium mood("+str(len(x_mid))+"dots)")
  ax.scatter(x_big,y_big,color='red',alpha=0.5,marker="o",label="high mood("+str(len(x_big))+"dots)")

def plot_setting(axs,factor_type,signal_type):
    for ax in axs:
        ax.legend()
        ax.set_ylabel("signal data("+face_type_list[signal_type]+")")
        ax.set_xlabel("factor data("+factor_type_list[factor_type]+")")

def select_data(data):
    #good_list_filename = "/home/kazumi/prog/test/face_timeseries/good_list.csv"
    #_good_array= np.loadtxt(good_list_filename,delimiter=",",dtype='int')
    #good_list = _good_array.tolist()
    select_num_list=[0,2,4,6,8,11,12,14,15,16,17,18,20,22,27,28,29]
    #print(good_list)
    selected_data=data[select_num_list]
    #print(selected_data)
    return select_num_list,selected_data

#TODO: should mode is included here?
def show_graph(username,factor_data,signal_data,factor_type,signal_type,_mental_data_all,thr,y_limit=None):
    select_flg = True 
    if(select_flg == True):
        _x = factor_data[:,factor_type]
        select_num_list,_x_data = select_data(_x)
        func_num = 4*factor_type + signal_type
        x_data = x_conv(mode,_x_data,func_num)
        _y = signal_data[:,signal_type]
        _,y_data = select_data(_y)
        _,mental_data=select_data(_mental_data_all)
    else:
        _x_data = factor_data[:,factor_type]
        func_num = 4*factor_type + signal_type
        x_data = x_conv(mode,_x_data,func_num)
        y_data = signal_data[:,signal_type]
        mental_data=_mental_data_all
    
    x_max = np.max(x_data)
    x_min = np.min(x_data)
    y_max = np.max(y_data)
    y_min = np.min(y_data)

    df=pd.DataFrame(x_data,columns=["factor"])
    df["signal"]=y_data
    df["mental"]=mental_data

    df_sml=df.query(str(thr[1])+'>mental>='+str(thr[0]))
    val_sml=int(df_sml["factor"].count())
    df_mid=df.query(str(thr[2])+'>mental>='+str(thr[1]))
    val_mid=int(df_mid["factor"].count())
    df_big=df.query(str(thr[3])+'>=mental>='+str(thr[2]))
    val_big=int(df_big["factor"].count())

    if(val_sml*val_mid*val_big>0):

      x_lim=x_conv(mode,np.array([0,1]),func_num)
      ret_sml,x_sml,y_sml,y_res_sml=ret_data(df_sml,func_num)
      ret_mid,x_mid,y_mid,y_res_mid=ret_data(df_mid,func_num)
      ret_big,x_big,y_big,y_res_big=ret_data(df_big,func_num)

      x_all = x_sml,x_mid,x_big
      y_all = y_sml,y_mid,y_big

      SML=0
      MID=1
      BIG=2
      print(factor_type_list[factor_type],"sml")
      check_kitekan(x_sml,y_sml,factor_type_list[factor_type],SML,x_lim)
      print(factor_type_list[factor_type],"mid")
      check_kitekan(x_mid,y_mid,factor_type_list[factor_type],MID,x_lim)
      print(factor_type_list[factor_type],"big")
      check_kitekan(x_big,y_big,factor_type_list[factor_type],BIG,x_lim)

      x=np.linspace(0,1,100)

      xlim=[x_min-(x_max-x_min)*0.1,x_max+(x_max-x_min)*0.1]
      ylim=[y_min-(y_max-y_min)*0.1,y_max+(y_max-y_min)*0.1]
      
#main

if __name__ == '__main__':
    #userlist= [1,2,4,5,6,7,8,9]
    userlist= [1]
    thr=[0,0.35,0.55,1]
    print("userlist",userlist)
    print("please check userlist. select_data() は現状User1にしか使えません. enter and continue.")
    input()

    for t in range(FACTOR_NUM):
        print("input func number from 0 to 9")
        f=int(input())
        #print("input signal number from 0 to 3")
        #e=int(input())
        #f=t
        e=0

        for username in userlist: 
            print(username)
            factor_data,signal_data,mental_data,df_mental = get_data(username)
            show_graph(username,factor_data,signal_data,f,e,mental_data,thr)
