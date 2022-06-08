from bokeh.plotting import figure
import numpy as np
import pandas as pd
import streamlit as st
import sqlite3


con = sqlite3.connect('testing_1.db')


cur = con.cursor()

last_row = cur.execute('select * from roi').fetchall()[-1]

print(last_row[0])
con.commit()
intAnnualAccruedROI=0
intTotalProcess=last_row[0]
intTotalEmployee=last_row[1]
intTotalTime=last_row[2]/100
intSalary=last_row[3]
intCostBot=last_row[4]
intMaintainanceCost=last_row[5]
ListCurrentCostFTE=[]
ListHoursWeek =[]
ListCostWeek=[]

ListToatlBotCost=[]
listNetROI=[]
listAnnualAccruedROI=[]
listBotCost=[]
intCurrentCostFTE=intTotalEmployee*intSalary*intTotalTime
intHoursWeek=40*intTotalEmployee*intTotalTime
intCostWeek=(intTotalEmployee*intTotalTime*intSalary)/52
intToatlBotCost=intCostBot*intTotalProcess
intNetROI=intCurrentCostFTE-intToatlBotCost
try:
    intAnnualAccruedROI=(intNetROI/intToatlBotCost)*100
except ZeroDivisionError:
    pass

ListToatlBotCost.append(intToatlBotCost)
ListCurrentCostFTE.append(intCurrentCostFTE)
ListHoursWeek.append(intHoursWeek)
ListCostWeek.append(intCostWeek)
listBotCost.append(intToatlBotCost)
listNetROI.append(intNetROI)
listAnnualAccruedROI.append(intAnnualAccruedROI)


for i in range(4):
    intCurrentCostFTE=intCurrentCostFTE
    intHoursWeek=intHoursWeek
    intCostWeek=intCostWeek
    intToatlBotCost=intMaintainanceCost

    intNetROI=intCurrentCostFTE-intToatlBotCost
        
    listBotCost.append(intToatlBotCost)
    listNetROI.append(intNetROI)
    ListCurrentCostFTE.append(intCurrentCostFTE)
    ListHoursWeek.append(intHoursWeek)
    ListCostWeek.append(intCostWeek)
    ListToatlBotCost.append(intToatlBotCost)



    ROISUM=sum(listNetROI)
    ROISUM2=sum(listBotCost)
    try:
        intAnnualAccruedROI=(ROISUM/ROISUM2)*100
    except ZeroDivisionError:
        pass
    listAnnualAccruedROI.append(intAnnualAccruedROI)

print(listNetROI,listAnnualAccruedROI)
left_ind=[]

for i in range(5):
    a="Year "+str(i+1)
    left_ind.append(a)
        # st.subheader(f"Year {(i+1)} - Net ROI is ${listNetROI[i]} - Net Accrued ROI is {round(listAnnualAccruedROI[i],2)}%, ---- {intCostWeek}")



li_yr=['Year 1','Year 2','Year 3','Year 4','Year 5',]
df = pd.DataFrame(list(zip(li_yr,ListCurrentCostFTE, ListHoursWeek, ListCostWeek, ListToatlBotCost,listNetROI, listAnnualAccruedROI)),
                columns =['Year','Current Costs for FTEs', 'Hours Per week for FTEs', 'Cost per Week for FTEs','Total Annual Cost','Net ROI', 'Annual Accrued ROI'])
st.table(df)









part11, part22 = st.columns(2)
with part11:
    # x = [1,2,3,4,5]
    # y = [462.5, 4225.0, 4387.5, 4550.0, 4712.5]
    x = [1, 2, 3, 4, 5]
    y = listAnnualAccruedROI
    p = figure(
        title='Annual Accrued ROI',
        x_axis_label='Year',
        y_axis_label='ROI %')

    p.line(x, y, legend_label='Trend', line_width=2)

    st.bokeh_chart(p, use_container_width=True)

# st.table(df)
with part22:
    x1 = [1, 2, 3, 4, 5]
    y1 = listNetROI
    # x1 = [1,2,3,4,5]
    # y1 = [462.5, 4225.0, 4387.5, 4550.0, 4712.5]
    p = figure(
        title='Net ROI ',
        x_axis_label='Year',
        y_axis_label='list Net ROI')

    p.line(x1, y1, legend_label='Trend', line_width=2)

    st.bokeh_chart(p, use_container_width=True)