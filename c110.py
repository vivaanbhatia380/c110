import statistics
import random
import pandas as pd 
import csv 
import plotly.figure_factory as ff
df=pd.read_csv('average.csv')
data=df['average'].tolist()
populationmean=statistics.mean(data)
populationstd=statistics.stdev(data)
print('mean',populationmean)
print('std',populationstd)


def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def showfig (meanlist):
    df=meanlist
    fig=ff.create_distplot([df],['average'],show_hist=False)
    fig.show()

def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    print('samplemean',statistics.mean(meanlist))
setup()
