import pandas as pd

factor_type_list=["trial num","rate of win","rate of encourage behavior","rate of sympathetic behavior", "rate of teasing behavior","rate of un-related behavior","rate of no behavior","total point","consecutive wins","consecutive loses"]
filename = "./1/factor_before.csv"
data = pd.read_csv(filename,header=None,names=factor_type_list,delimiter="\t")

for t in range(10):
    print("select quiz number")
    num = int(input())
    print(data.iloc[num])
