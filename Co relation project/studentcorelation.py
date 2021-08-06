import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    studentmarks=[]
    dayspresent=[]
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            studentmarks.append(float(row["Marks In Percentage"])) 
            dayspresent.append(float(row["Days Present"])) 
    return{"x":studentmarks,"y":dayspresent}
    
def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Corelation between Student Marks vs Number of Days Present",corelation[0,1])

def setup():
    data_path="studentData.csv"
    dataSource=getDataSource(data_path)
    findCorelation(dataSource)

setup()
