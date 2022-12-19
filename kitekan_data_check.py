import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd
from func_check_draw import draw_func

#print("input mode all/each/set(what is it?)/check")
#mode=input()

def get_spl(x_data,y_data):
  f_sci = interpolate.interp1d(x_data,y_data,kind="cubic")

USER_NUM = 9
FACTOR_NUM =4 
FACE_TYPE = 4

DIR_PATH = "./"
face_type_list=["happy","surprised","angry","sad"]
factor_type_list=["trial num","rate of win","rate of encourage behavior","rate of sympathetic behavior", "rate of teasing behavior","rate of un-related behavior","rate of no behavior","total point","consecutive wins","consecutive loses"]

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
def ret_data(df):
  ##sorted x and y
  x_data=np.array(df["factor"])+0.0001
  y_data=np.array(df["signal"])
  mental_data=np.array(df["mental"])

  x_data_2=x_data[np.argsort(x_data)]
  y_data_2=y_data[np.argsort(x_data)]
  mental_2=mental_data[np.argsort(x_data)]

  res = np.polyfit(x_data_2,y_data_2,2)
  x=np.linspace(0,1,100)
  y_res=np.poly1d(res)(x)
  return res,x_data_2,y_data_2,y_res

def show_graph(username,factor_data,signal_data,factor_type,signal_type,mental_data,thr):
    x_data = factor_data[:,factor_type]
    y_data = signal_data[:,signal_type]
    
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
      ret_sml,x_sml,y_sml,y_res_sml=ret_data(df_sml)
      ret_mid,x_mid,y_mid,y_res_mid=ret_data(df_mid)
      ret_big,x_big,y_big,y_res_big=ret_data(df_big)

      x=np.linspace(0,1,100)

      #plt.plot(x,y_res_sml,color='blue',label="sml",linestyle="dotted")
      #plt.plot(x,y_res_mid,color='green',label="mid",linestyle="dashed")
      #plt.plot(x,y_res_big,color='red',label="big",linestyle="solid")
      draw_func(factor_type,signal_type,show_flg=False)
      
      plt.scatter(x_sml,y_sml,color='blue',alpha=0.5,marker="x",label="sml("+str(len(x_sml))+"dots)")
      plt.scatter(x_mid,y_mid,color='green',alpha=0.5,marker="^",label="mid("+str(len(x_mid))+"dots)")
      plt.scatter(x_big,y_big,color='red',alpha=0.5,marker="o",label="big("+str(len(x_big))+"dots)")

      plt.xlim(x_min-(x_max-x_min)*0.1,x_max+(x_max-x_min)*0.1)
      plt.ylim(y_min-(y_max-y_min)*0.1,y_max+(y_max-y_min)*0.1)
      
    plt.legend()
    
    plt.title("mental thr is "+str(thr[1])+" and "+str(thr[2]))

    plt.ylabel("face data("+face_type_list[signal_type]+")")
    plt.xlabel("factor data("+factor_type_list[factor_type]+")")

    filename="./plot/graph_u"+str(username)+"_f"+str(factor_type)+"_s"+str(signal_type)+".png"
    #plt.savefig(filename)
    plt.show()
    print("u",username,"f",factor_type,"s",signal_type)
    plt.clf()

#main

if __name__ == '__main__':
    print("check user 1")
    username = 1
    thr=[0,0.35,0.55,1]

    for t in range(10):
        print("input func number from 0 to 9")
        f=int(input())
        print("input signal number from 0 to 3")
        e=int(input())

        factor_data,signal_data,mental_data,df_mental = get_data(username)
        show_graph(username,factor_data,signal_data,f,e,mental_data,thr)
