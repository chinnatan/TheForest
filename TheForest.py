import csv
import numpy as np
import matplotlib.pyplot as plt

def theforest():
    """this function will open and read file, return data."""
    yeardata = []
    north = []
    northeast = []
    float_north = []
    float_northeast = []

    ifile  = open('DatabaseCSV/พื้นที่ป่าประเทศไทยปี 2516 - 2558.csv', 'r')
    reader = csv.reader(ifile)

    for row in reader:
        yeardata.append(row[0])
        north.append(row[1])
        northeast.append(row[2])

    for i in north[1:20]:
        i = i.replace(",", "")
        float_north.append(float(i))

    for i in northeast[1:20]:
        i = i.replace(",", "")
        float_northeast.append(float(i))

    return yeardata[1:20], float_north, float_northeast, north, northeast

plotgraph = theforest() # Call Function

num_graph = 19
ind = np.arange(num_graph)  # the x locations for the groups
width = 0.10       # the width of the bars

fig, plot = plt.subplots()
rects1 = plot.bar(ind, plotgraph[1], width, color='b')
rects2 = plot.bar(ind + width, plotgraph[2], width, color='r')

# add some text for labels, title and axes ticks
plot.set_ylabel('Analyzed')
plot.set_title('Forestry analyzed by region')
plot.set_xticks(ind + width)
plot.set_xticklabels(plotgraph[0])
plot.set_yticklabels(('0.00', '10,000,000.00', '20,000,000.00', '30,000,000.00', '40,000,000.00', '50,000,000.00', '60,000,000.00', '70,000,000.00', '80,000,000.00'))

plot.legend((rects1[0], rects2[0]), ('North', 'North East'))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        # plot.text(rect.get_x() + rect.get_width()/2., 2.05*height,
                # '%d' % int(height),
                # ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
