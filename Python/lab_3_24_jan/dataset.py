import pandas as pd

data = pd.read_csv("C:/Users/DDas/Downloads/pokemon.csv")
data.head(10)
print(data.tail(5))


data = pd.read_excel("C:/Users/DDas/Downloads/pokemon.csv.xlsx")

print(data.describe())
req_cols = [1,12]
new_df = pd.read_excel("C:/Users/DDas/Downloads/pokemon.csv.xlsx",usecols=req_cols)
print(new_df)

# print(data.iloc[1:12,12:12])

#create a dataframe consisting of type = fire and water count the number 
#of pokemons within each category of type 
cols_req=[1,2]
dataframe = pd.read_excel("C:/Users/DDas/Downloads/pokemon.csv.xlsx",usecols=cols_req)
print(dataframe(dataframe['type'=='fire']))
dictt2={"Name":["Jai","Veeru","Raj","Aman"],
       "Age":[27,24,28,25],
       "Address":["Delhi","Kanpur","Allahabad","Patna"],
       "Qualification":["MSc","MA","MCA","Phd"]
      }
df4=pd.DataFrame(dictt2)
print(df4)
print(df4[["Name","Qualification"]])
row2=df4.iloc[2,1]
print(row2)
data=pd.read_csv("C:/Users/KIIT/Documents/DataSheets/Pokemon.csv")
#data3=pd.read_excel(path)
data.head(5)
data.tail(5)
data=pd.read_excel("C:/Users/KIIT/Documents/DataSheets/Poke2.xlsx")
data.head(3)
data.describe()
print(data.columns)
print(data[["Name","Legendary"]])
a1=data["Name"]
a2=data[["Name","Legendary"]]
print(type(a1))
print(type(a2))
print(type(data))
print(data.iloc[0,4])
print(data.iloc[2,1])
data.iloc[2:8,3:6]
for index, row in data.iterrows():
    print(index,row["Legendary"])
    for index, row in data.iterrows():
        if row["Legendary"]==True:
            print(index,row[["Name","Legendary"]])
            print(data['Type 1'].value_counts())
print(data['Type 2'].value_counts())
dff = pd.DataFrame(columns=["Fire","Water"],index=["Count"])
f,w = 0,0
for ty1,ty2 in zip(data["Type 1"],data["Type 2"]):
    if ty1=="Fire" or ty2=="Fire":
        f+=1
    elif ty1=="Water" or ty2=="Water":
        w+=1
dff["Fire"] = f
dff["Water"] = w
dff
d1=(data[['Name','Type 1','Type 2']]) 
d2=pd.DataFrame(d1)
for index , row in d2.iterrows():
    if row['Type 1']=='Fire' or row['Type 2']=='Fire' or row['Type 1']=='Water' or row['Type 2']=='Water':
        print(index , row[['Name','Type 1','Type 2']])
        d3=pd.DataFrame(d1)
for index , row in d3.iterrows():
    if (row['Type 1']=='Fire' and row['Type 2']=='Water') or (row['Type 1']=='Water' and row['Type 2']=='Fire'):
        print(index , row[['Name','Type 1','Type 2']])


