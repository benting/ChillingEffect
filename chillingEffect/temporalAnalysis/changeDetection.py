
import matplotlib.pyplot as plt
import changefinder
import numpy as np

def readTS(infilepath):
    ts = [0 for i in range(0,250)]
    infile = open(infilepath)
    for line in infile:
        line = line.strip()
        weekId = int(line)
        if weekId < 0 or weekId >= 250:
            continue
        ts[weekId] = ts[weekId] + 1
    infile.close()
    return ts

def changeDetect(data):
    cf = changefinder.ChangeFinder(r=0.5, order=1, smooth=7)
    ret = []
    for i in data:
        score = cf.update(i)
        ret.append(score)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ret)
    ax2 = ax.twinx()
    ax2.plot(data,'r')
    plt.show()

if __name__ == '__main__':
    numB = 332
    basepath = '/Users/JuntingYe/Desktop/network/dataset/individuals/'
    for i in range(0, numB):
        ts = readTS(basepath + str(i))
        changeDetect(ts)