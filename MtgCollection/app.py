import pandas as pd
from glob import glob
from collections import defaultdict

collection = defaultdict(int)

aesi = pd.read_csv('Aesi.csv', delimiter=';', header=[0])
tricky = pd.read_csv('TrickyTerrain.csv', delimiter=';', header=[0])

for file in [aesi, tricky]:
    for row in file.iloc:
        print(row['Name'], row['Qty'], row['Edition'])
        collection[(row['Name'], row['Edition'])] += row['Qty']

for file in glob('./*.xls'):
    xls = pd.read_excel(file)
    for row in xls.iloc:
        print(row['Item Name'], row['Quantity'], row['Set Code'])
        collection[(row['Item Name'], row['Set Code'])] += row['Quantity']


frame = {'Name': [], 'Edition': [], 'Quantity': []}
for (name, edition), q in collection.items():
    frame['Name'].append(name)
    frame['Edition'].append(edition)
    frame['Quantity'].append(q)

frame = pd.DataFrame(frame)
frame.to_excel('myCollection.xlsx')