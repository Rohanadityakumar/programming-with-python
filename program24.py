import matplotlib.pyplot as grph
#values of x-coordinates towards left side
x=[1,2,3,4,5]
#values of y-coordinates toward up
y=[43,52,25,36,20]
#names for bars
name=['mon','tue','wed','thur','fri']
#plotting bar graph
grph.bar(x,y,tick_label=name,width=0.8,color=['red','blue','green','yellow','orange'])
#naming x-axis
grph.xlabel('Days')
#naming y-axis
grph.ylabel('Students')
#naming graph
grph.title('BAR GRAPH')
grph.show()