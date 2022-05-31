import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config(
    page_title="ROI browser title")

st.title("ROI Calculator")

part1, part2 = st.columns(2)

with part1:
    intTotalProcess = st.number_input("Number of business process the RPA Bot will automate : ", min_value=0, format='%d')
    intTotalEmployee = st.number_input("How many FTEs currently work on the task(s) : ", min_value=0, format='%d')
    intTotalTime = st.number_input("What % of the FTE(s) daily time is spent on this task : ",min_value=0,format='%d')

with part2:
    intSalary = st.number_input("What is the average fully loaded salary of the FTE(s) : ",min_value=0,format='%d')
    intCostBot = st.number_input("Est. Cost Per Bot implementation : ",min_value=0,format='%d')
    intMaintainanceCost = st.number_input("Estmated Maintenance : ",min_value=0,format='%d')


intAnnualAccruedROI=0
intTotalProcess=intTotalProcess
intTotalEmployee=intTotalEmployee
intTotalTime=intTotalTime/100
intSalary=intSalary
intCostBot=intCostBot
intMaintainanceCost=intMaintainanceCost
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




li_1=[162.5, 1225.0, 1387.5, 1550.0, 1712.5]
li_2=[262.5, 2225.0, 2387.5, 2550.0, 2712.5]
li_3=[362.5, 3225.0, 3387.5, 3550.0, 7312.5]
li_4=[462.5, 4225.0, 4387.5, 4550.0, 4712.5]


# df = pd.DataFrame(
#     list(zip(li_1, li_2, li_3, li_4, listNetROI, listAnnualAccruedROI)),
#     columns=('Year %d' % i for i in range(1,7)), index=['Current Costs for FTEs', 'Hours Per week for FTEs', 'Cost per Week for FTEs','Net ROI','Annual Accrued ROI'])


# df = pd.DataFrame(
#     list(zip(li_1, li_2, li_3, li_4, listNetROI, listAnnualAccruedROI)),
#     columns=('Current Costs for FTEs', 'Hours Per week for FTEs', 'Cost per Week for FTEs','Net ROI','Annual Accrued ROI'), index=['Year %d' % i for i in range(1,5)])





# st.table(df)