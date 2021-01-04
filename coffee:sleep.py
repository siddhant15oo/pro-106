import plotly.express as px
import csv
import numpy as np

def getDataSoares(data_path):
    sleep_in_hours=[]
    coffee_in_ml=[]
    with open(data_path)as csv_files:
       # csv_reader=reader(csv_files)
       csv_reader=csv.DictReader(csv_files)
       for i in csv_reader:
             coffee_in_ml.append(float(i["sleep in hours"]))
            #continue formula
             sleep_in_hours.append(float(i["Coffee in ml"]))
    return{'x':sleep_in_hours,'y':coffee_in_ml}

def findCorrelation (datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])

    print("correlation between coffee in ml and sleep in hours is: ",correlation[0,1])


def setup():
    data_path='/Users/jaiagnani/python1/pro-106/coffe:sleep.csv'
    datasource=getDataSoares(data_path)
    findCorrelation(datasource)

setup()