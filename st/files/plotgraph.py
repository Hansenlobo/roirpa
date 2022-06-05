import matplotlib.pyplot as plt

# x-coordinates of left sides of bars  //year
left = ["Year 1","Year 2","Year 3","Year 4","Year 5"]
  
# heights of bars  // roi
height = [33.33333333333333, 128.57142857142858, 200.0, 255.55555555555554, 300.0]
  
# labels for bars
  
# plotting a bar chart
plt.bar(left, height, tick_label = left,
        width = 0.5, color = ['violet','indigo','blue','green','yellow'])
  
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('NET ACCURED ROI (%)')
# plot title
plt.title('NET ACCURED ROI')
  
# function to show the plot
plt.show()