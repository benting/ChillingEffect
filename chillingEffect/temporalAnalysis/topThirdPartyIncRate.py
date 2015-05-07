import datetime
import matplotlib.pyplot as plt

def week2dateSingle(weekId):
    days = weekId * 7
    start = datetime.date(2010, 1, 1)
    delta1 = datetime.timedelta(days)
    end1 = start + delta1
    return str(end1)

def getDateId(dateTime):
    dateV = dateTime.split('T')[0]
    if len(dateV) != 10:
#         print 'date error'
#         print dateTime
        return -1
    ele = dateV.split('-')
    assert len(ele) == 3, 'date format error'
    end = datetime.date(int(ele[0]), int(ele[1]), int(ele[2]))
    start = datetime.date(2010, 1, 1)
    return (end - start).days / 7

def readData(inputPath, topThirdParties):
    allDic = {}
    thirdpartyDic = {}
    infile = open(inputPath)
    for line in infile:
        line = line.strip()
        notice = line.split('\t')  # [id, sendDate, senderName, recipientName, principalName, type]
        sender = notice[2]
        type = notice[5]
        dateId = getDateId(notice[1])
        if dateId == -1 or dateId > 250:
            continue
        
        if not allDic.has_key(dateId):
            allDic[dateId] = 0
        allDic[dateId] = allDic[dateId] + 1
        
        if sender in topThirdParties:
            if not thirdpartyDic.has_key(dateId):
                thirdpartyDic[dateId] = 0
            thirdpartyDic[dateId] = thirdpartyDic[dateId] + 1
        
    return allDic, thirdpartyDic

def readTopThirdParties(topThirdPartyPath):
    topThirdParties = set()
    infile = open(topThirdPartyPath)
    for line in infile:
        line = line.strip()
        units = line.split('\t')
        topThirdParties.add(units[0])
    infile.close()
    return topThirdParties

def plotThirdPartyCompare(dmcaDic, defameDic, outputFigPath):
    dmcaMax = max(dmcaDic.keys())
    dmcaMin = min(dmcaDic.keys())
    maxdateId = dmcaMax
    mindateId = dmcaMin
    dmcaL = []
    for i in range(0, maxdateId):
        if i in dmcaDic.keys():
            dmcaL.append(dmcaDic[i])
        else:
            dmcaL.append(0)
    
    third = []
    for i in range(0, maxdateId):
        if i in defameDic.keys():
            third.append(defameDic[i])
        else:
            third.append(0)
            
    x = [i for i in range(0, maxdateId)]
#     _, ax = plt.subplots(1, 1)
#     plt.figure()
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.plot(x, dmcaL, "r-", label='# of All Notices')
    plt.plot(x, third, "b-", label='# of Top 10 Third Parties\' Nitices')
    ax.set_xticklabels([week2dateSingle(0),week2dateSingle(50),week2dateSingle(100),week2dateSingle(150),week2dateSingle(200),week2dateSingle(250)])
    
    plt.ylabel("count")
    plt.xlabel("weeks")
#     plt.title("Temporal Distribution of notices")
#     plt.yscale('log')
    plt.grid(True)
    plt.legend(loc=2)
    plt.savefig(outputFigPath)
#     plt.show()

if __name__ == '__main__':
    basepath = '/Users/JuntingYe/Desktop/network/dataset/'
    topThirdPartyPath = basepath + 'topThirdParties'
    sourceDataPath = basepath + 'chillingMetadata'
    outputPlotPath = basepath + 'thirdPartyPlot.pdf'
    topThirdParties = readTopThirdParties(topThirdPartyPath)
    allDic, thirdpartyDic = readData(sourceDataPath, topThirdParties)
    plotThirdPartyCompare(allDic, thirdpartyDic, outputPlotPath)