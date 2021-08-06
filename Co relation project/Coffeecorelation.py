import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee=[]
    sleep=[]
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"])) 
            sleep.append(float(row["sleep in hours"])) 
    return{"x":coffee,"y":sleep}
    
def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Corelation between Coffe drank vs Time slept",corelation[0,1])

def setup():
    data_path="CoffeeData.csv"
    dataSource=getDataSource(data_path)
    findCorelation(dataSource)

setup()
