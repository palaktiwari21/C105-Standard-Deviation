import csv

with open ('class1.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
total_marks=0
total_enteries=len(file_data)
for marks in file_data:
    total_marks+=float(marks[1])
mean=total_marks/total_enteries
print('Mean Is : '+str(mean))
import plotly.express as px
import pandas as pd
df =pd.read_csv('class1.csv')
fig=px.scatter(df,x='Student Number',y='Marks')
fig.update_layout(shapes=[dict(type='line',y0=mean,y1=mean,x0=0,x1=total_enteries)])
fig.update_yaxes(rangemode='tozero')
fig.show()