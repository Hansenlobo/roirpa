import sqlite3

con = sqlite3.connect('testing_1.db')
cur = con.cursor()

# cur.execute('''CREATE TABLE roi
#                (intTotalProcess real, intTotalEmployee real, intTotalTime real, intSalary real, intCostBot real,intMaintainanceCost real)''')


# cur.execute("INSERT INTO roi VALUES (2,4,40,70000,30000,10001)")

# for row in cur.execute('SELECT * FROM roi ORDER BY rowid DESC LIMIT 1;'):
#         print(row)
last_row = cur.execute('select * from roi').fetchall()[-1]

print(last_row[0])
con.commit()


intTotalProcess=last_row[0]
intTotalEmployee=last_row[1]
intTotalTime=last_row[2]/100
intSalary=last_row[3]
intCostBot=last_row[4]
intMaintainanceCost=last_row[5]
# intYearProjection=int(input("Years Projected"))
listNetROI=[]
listAnnualAccruedROI=[]
listBotCost=[]
intCurrentCostFTE=intTotalEmployee*intSalary*intTotalTime
intHoursWeek=40*intTotalEmployee*intTotalTime
intCostWeek=(intTotalEmployee*intTotalTime*intSalary)/52
intToatlBotCost=intCostBot*intTotalProcess
# print(intCurrentCostFTE,intHoursWeek,intCostWeek,intToatlBotCost)
intNetROI=intCurrentCostFTE-intToatlBotCost
intAnnualAccruedROI=(intNetROI/intToatlBotCost)*100

listBotCost.append(intToatlBotCost)
listNetROI.append(intNetROI)
listAnnualAccruedROI.append(intAnnualAccruedROI)

# print(intNetROI,intAnnualAccruedROI)
# print("==================================")
# print(listNetROI,listAnnualAccruedROI)


for i in range(4):
    # print("inside loop ",i)
    intCurrentCostFTE=intCurrentCostFTE
    intHoursWeek=intHoursWeek
    intCostWeek=intCostWeek
    intToatlBotCost=intMaintainanceCost
    # print(intCurrentCostFTE,intHoursWeek,intCostWeek,intToatlBotCost)

    intNetROI=intCurrentCostFTE-intToatlBotCost
    
    listBotCost.append(intToatlBotCost)
    listNetROI.append(intNetROI)
    
    ROISUM=sum(listNetROI)
    ROISUM2=sum(listBotCost)
    intAnnualAccruedROI=(ROISUM/ROISUM2)*100
    listAnnualAccruedROI.append(intAnnualAccruedROI)

print(listNetROI,listAnnualAccruedROI)
left_ind=[]
for i in range(5):
    a="Year "+str(i+1)
    left_ind.append(a)
    print(f"Year {(i+1)} - Net ROI is ${listNetROI[i]} - Net Accrued ROI is {round(listAnnualAccruedROI[i],2)}%")

