import csv

def theforest():
    ifile  = open('Database CSV/พื้นที่ป่าประเทศไทยปี 2516 - 2558.csv', 'r')
    reader2 = csv.reader(ifile)

    rownum = 0
    for row in reader2:
        # Save header row.
        if rownum == 0:
            header = row
        else:
            colnum = 0
            for col in row:
                print(("%s: %s") % (header[colnum], col))
                colnum += 1
        rownum += 1

    ifile.close()

theforest()
