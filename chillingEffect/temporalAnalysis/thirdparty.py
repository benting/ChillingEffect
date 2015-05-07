
def readData(inputPath):
    senderDetailDic = {}
    infile = open(inputPath)
    count = 0
    for line in infile:
        line = line.strip()
        notice = line.split('\t')  # [id, sendDate, senderName, recipientName, principalName, type]
        sender = notice[2]
        recipient = notice[3]
        principle = notice[4]
        if len(principle)>1 and sender!=principle:
            count = count + 1
        if not senderDetailDic.has_key(sender):
            senderDetailDic[sender] = {}
            
        if not senderDetailDic[sender].has_key(principle):
            senderDetailDic[sender][principle] = 0
            
        senderDetailDic[sender][principle] = senderDetailDic[sender][principle] + 1
    print count
    return senderDetailDic

if __name__ == '__main__':
    threshold = 1000
    basepath = '/Users/JuntingYe/Desktop/network/dataset/'
    inputPath = basepath + 'chillingMetadata'
    outputpath = basepath + 'thirdparties'
    senderDetailDic = readData(inputPath)
    
    senderDetailL = sorted(senderDetailDic.items(), key=lambda x:len(x[1]), reverse=True)
    outputfile = open(outputpath, 'w')
    for ele in senderDetailL:
        if len(ele[1]) < 2:
            break
        outputfile.write(ele[0] + '\t' + str(len(ele[1])) + '\n')  # name of anti-piracy business, # of senders
    outputfile.close()
