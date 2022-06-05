# import matplotlib.pyplot as plt



# intTotalProcess=int(input("Number of business process the RPA Bot will automate"))
# intTotalEmployee=int(input("How many FTEs currently work on the task(s)?"))
# intTotalTime=int(input("What percentage of the FTE(s) daily time is spent on this task?"))
# intTotalTime=intTotalTime/100
# intSalary=int(input("What is the average fully loaded salary of the FTE(s) performing this task?"))
# intCostBot=int(input("Est. Cost Per Bot implementation"))
# intMaintainanceCost=int(input("Estmated Maintenance"))

intTotalProcess=3
intTotalEmployee=6
intTotalTime=50/100
intSalary=65000
intCostBot=40000
intMaintainanceCost=12000
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

# left = left_ind
  
# # heights of bars  // roi
# height = listAnnualAccruedROI
  
# # labels for bars
  
# # plotting a bar chart
# plt.bar(left, height, tick_label = left,
#         width = 0.5, color = ['violet','indigo','blue','green','yellow'])
  
# # naming the x-axis
# plt.xlabel('x - axis')
# # naming the y-axis
# plt.ylabel('NET ACCURED ROI (%)')
# # plot title
# plt.title('NET ACCURED ROI')
  
# # function to show the plot
# plt.show()