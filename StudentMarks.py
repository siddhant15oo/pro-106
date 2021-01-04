import plotly.express as px
import csv
import numpy as np

def getDataSoares(data_path):
    days_present=[]
    marks_percentage=[]
    with open(data_path)as csv_files:
       # csv_reader=reader(csv_files)
       csv_reader=csv.DictReader(csv_files)
       for i in csv_reader:
             days_present.append(float(i["Days Present"]))
            #continue formula
             marks_percentage.append(float(i["Marks In Percentage"]))
    return{'x':days_present,'y':marks_percentage}

def findCorrelation (datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])

    print("correlation between temperature and Ice-cream is: ",correlation[0,1])


def setup():
    data_path='/Users/jaiagnani/python1/pro-106/Student:Marks.csv'
    datasource=getDataSoares(data_path)
    findCorrelation(datasource)

setup()