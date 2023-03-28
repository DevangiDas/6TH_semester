# 1. Given a state as input determine year-wise the highest crime district.
import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv("D:/Programing_works/6th_semester_work/Python/Class_evaluation/india-crime.csv")
print(data.head())

state = input("Enter the state:")
for x in range (1,13):
    max = 0
    dis = ''
    for index, row in data.iterrows():
        if row.STATEUT==state and row.Year==2000+x and row.DISTRICT!='TOTAL' and row.DISTRICT!='DELHI UT TOTAL':
            if (row.Rape + row.KidnappingandAbduction + row.DowryDeaths + row.Assaultonwomenwithintenttooutragehermodesty + row.InsulttomodestyofWomen + row.CrueltybyHusbandorhisRelatives + row.ImportationofGirls)>max:
                max = row.Rape + row.KidnappingandAbduction + row.DowryDeaths + row.Assaultonwomenwithintenttooutragehermodesty + row.InsulttomodestyofWomen + row.CrueltybyHusbandorhisRelatives + row.ImportationofGirls
                dis = row.DISTRICT
    print("Year:", 2000+x, "\nDistrict : ",dis)