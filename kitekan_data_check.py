import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd
from func_check_draw import draw_func,x_conv
from adjustText import adjust_text


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

def plot_observed_data(x,y,ax):
  x_sml,x_mid,x_big=x
  y_sml,y_mid,y_big=y
  ax.scatter(x_sml,y_sml,color='blue',alpha=0.5,marker="x",label="sml("+str(len(x_sml))+"dots)")
  ax.scatter(x_mid,y_mid,color='green',alpha=0.5,marker="^",label="mid("+str(len(x_mid))+"dots)")
  ax.scatter(x_big,y_big,color='red',alpha=0.5,marker="o",label="big("+str(len(x_big))+"dots)")


def plot_setting(axs,factor_type,signal_type):
    for ax in axs:
        ax.legend()
        ax.set_ylabel("face data("+face_type_list[signal_type]+")")
        ax.set_xlabel("factor data("+factor_type_list[factor_type]+")")


def show_graph(username,factor_data,signal_data,factor_type,signal_type,mental_data,thr,y_limit=None):
    _x_data = factor_data[:,factor_type]
    func_num = 4*factor_type + signal_type
    x_data = x_conv(_x_data,func_num)
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

      x_all = x_sml,x_mid,x_big
      y_all = y_sml,y_mid,y_big

      fig = plt.figure(figsize=(25,12))
      ax1 = fig.add_subplot(2, 3, 1)
      ax2 = fig.add_subplot(2, 3, 2)
      ax3 = ax2.twinx()
      ax4 = fig.add_subplot(2, 3, 3)
      ax5 = fig.add_subplot(2, 3, 4)
      ax6 = fig.add_subplot(2, 3, 6)

      x=np.linspace(0,1,100)

      xlim=[x_min-(x_max-x_min)*0.1,x_max+(x_max-x_min)*0.1]
      ylim=[y_min-(y_max-y_min)*0.1,y_max+(y_max-y_min)*0.1]
      
      plot_observed_data(x_all,y_all,ax1)
      plot_observed_data(x_all,y_all,ax2)
      for i in range(len(x_data)):
          ax1.annotate(str(i), xy = (x_data[i],y_data[i]), size = 8, color = "black")
      plot_observed_data(x_all,y_all,ax4)
      plot_observed_data(x_all,y_all,ax5)
      plot_observed_data(x_all,y_all,ax6)

      #plot_observed_data(x_all,y_all,ax5)

      ax5.plot(x_conv(np.linspace(0,1,100),func_num),y_res_sml,color='blue',label="sml")
      ax5.plot(x_conv(np.linspace(0,1,100),func_num),y_res_mid,color='green',label="mid")
      ax5.plot(x_conv(np.linspace(0,1,100),func_num),y_res_big,color='red',label="big")

      ax6.plot(x_conv(np.linspace(0,1,100),func_num),y_res_sml,color='blue',label="sml")
      ax6.plot(x_conv(np.linspace(0,1,100),func_num),y_res_mid,color='green',label="mid")
      ax6.plot(x_conv(np.linspace(0,1,100),func_num),y_res_big,color='red',label="big")

      draw_func(factor_type,signal_type,ax1,show_flg=False)
      draw_func(factor_type,signal_type,ax4,show_flg=False)

      if(y_limit is not None):
        draw_func(factor_type,signal_type,ax3,show_flg=False,x_limit=xlim,y_limit=y_limit)
        ax3.set_ylim(y_limit)
      else:
        draw_func(factor_type,signal_type,ax3,show_flg=False)

      ax1.set_xlim(xlim)
      ax1.set_ylim(ylim)

      ax2.set_xlim(xlim)
      ax2.set_ylim(ylim)
      ax3.set_ylabel("output of basis function("+face_type_list[signal_type]+")")
      
      ax5.set_xlim(xlim)
      ax5.set_ylim(ylim)

    plot_setting([ax1,ax2,ax4,ax5,ax6],factor_type,signal_type)
    
    plt.legend()
    plt.title("mental thr is "+str(thr[1])+" and "+str(thr[2]))

    filename="./plot/graph_u"+str(username)+"_f"+str(factor_type)+"_s"+str(signal_type)+".png"
    #plt.savefig(filename)
    #plt.tight_layout()
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
        #print("input y min")
        #ymin=float(input())
        #print("input y max")
        #ymax=float(input())
        #ylim=[ymin,ymax]
        #show_graph(username,factor_data,signal_data,f,e,mental_data,thr,y_limit=ylim)