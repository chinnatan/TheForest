import csv
import numpy as np
import matplotlib.pyplot as plt

def frist_graph():
    """this function open file, read file and return data it."""
    yeardata = []
    north, float_north = [], []
    northeast, float_northeast = [], []
    east, float_east = [], []
    central, float_central = [], []
    south, float_south = [], []

    ifile  = open('DatabaseCSV/พื้นที่ป่าประเทศไทยปี 2516 - 2558.csv', 'r')
    reader = csv.reader(ifile)

    for row in reader:
        yeardata.append(row[0]), north.append(row[1]), northeast.append(row[2]), east.append(row[3]), central.append(row[4]), south.append(row[5])
        
    for i in north[1:20]:
        i = i.replace(",", "")
        float_north.append(float(i))

    for i in northeast[1:20]:
        i = i.replace(",", "")
        float_northeast.append(float(i))

    for i in east[1:20]:
        i = i.replace(",", "")
        float_east.append(float(i))

    for i in central[1:20]:
        i = i.replace(",", "")
        float_central.append(float(i))

    for i in south[1:20]:
        i = i.replace(",", "")
        float_south.append(float(i))

    return yeardata[1:20], float_north, float_northeast, float_east, float_central, float_south

def second_graph():
    """this function open file, read file and return data it."""
    data = []

    ifile  = open('DatabaseCSV/พื้นที่ป่าที่ได้รับการฟื้นฟูโดยกรมป่าไม้ปี 2007-2015.csv', 'r')
    reader = csv.reader(ifile)
    included_cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for row in reader:
        data.append([row[i] for i in included_cols])
    print(data[0][0])

frist_plotgraph = frist_graph() # Call Function
second_plotgraph = second_graph() # Call Function

def theforest():
    """this function will plot graph and show it."""
    num_graph = 19
    ind = np.arange(num_graph)  # the x locations for the groups
    width = 0.10       # the width of the bars

    # Frist Graph
    fig, plot = plt.subplots()
    rects1 = plot.bar(ind, frist_plotgraph[1], width, color='b')
    rects2 = plot.bar(ind + width, frist_plotgraph[2], width, color='orangered')
    rects3 = plot.bar(ind + (width * 2), frist_plotgraph[3], width, color='m')
    rects4 = plot.bar(ind + (width * 3), frist_plotgraph[4], width, color='y')
    rects5 = plot.bar(ind + (width * 4), frist_plotgraph[5], width, color='navy')
    plot.set_ylabel('Analyzed')
    plot.set_title('Forestry analyzed by region')
    plot.set_xticks(ind + (width * 2.5))
    plot.set_xticklabels(frist_plotgraph[0])
    plot.set_yticklabels(('0.00', '10,000,000.00', '20,000,000.00', '30,000,000.00', '40,000,000.00', '50,000,000.00', '60,000,000.00', '70,000,000.00', '80,000,000.00'))
    plot.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('North', 'North East', 'East', 'Central', 'South'))

    # Second Graph
    # fig, plot2 = plt.subplots()
    # rects1 = plot2.bar(ind, second_plotgraph[1], width, color='b')
    # rects2 = plot2.bar(ind + width, second_plotgraph[2], width, color='orangered')
    # rects3 = plot2.bar(ind + (width * 2), second_plotgraph[3], width, color='m')
    # rects4 = plot2.bar(ind + (width * 3), second_plotgraph[4], width, color='y')
    # rects5 = plot2.bar(ind + (width * 4), second_plotgraph[5], width, color='navy')
    # plot2.set_ylabel('Analyzed')
    # plot2.set_title('Forest areas that have been reclaimed by the forest department.')
    # plot2.set_xticks(ind + (width * 2.5))
    # plot2.set_xticklabels(second_plotgraph[0])
    # plot2.set_yticklabels(('0.00', '10,000,000.00', '20,000,000.00', '30,000,000.00', '40,000,000.00', '50,000,000.00', '60,000,000.00', '70,000,000.00', '80,000,000.00'))
    # plot2.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('North', 'North East', 'East', 'Central', 'South'))

    plt.show()

theforest()
