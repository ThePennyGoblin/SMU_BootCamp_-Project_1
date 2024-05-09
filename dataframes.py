import pandas as pd

MainDF = pd.read_csv("Total.csv")

print(type(MainDF))
print(MainDF.keys())

DF2000 = MainDF.loc[MainDF["Year"]==2000]

print(DF2000)

# Data Frames To help with splitting up the data 
def DF_Year_2000(): 
    DF2000 = MainDF.loc[MainDF["Year"]==2000]
    
    return (DF2000)

def DFYear2005():
    print(MainDF.loc[MainDF["Year"]==2005])


def DFYear2010():
    print(MainDF.loc[MainDF["Year"]==2010])


def DFYear2015():
    print(MainDF.loc[MainDF["Year"]==2015])


def DFYear2019():
    print(MainDF.loc[MainDF["Year"]==2000])

print(DF_Year_2000())