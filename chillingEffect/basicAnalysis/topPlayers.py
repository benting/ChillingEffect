# top ranking nodes for each type

def readData(inputPath):
    dmcaSenderDic = {}
    defameSenderDic = {}
    courtSenderDic = {}
    otherSenderDic = {}
    tradeMarkSenderDic = {}
    dmcaRecipientDic = {}
    defameRecipientDic = {}
    courtRecipientDic = {}
    otherRecipientDic = {}
    tradeMarkRecipientDic = {}
    dmcaPrincipleDic = {}
    defamePrincipleDic = {}
    courtPrincipleDic = {}
    otherPrincipleDic = {}
    tradeMarkPrincipleDic = {}
    infile = open(inputPath)
    for line in infile:
        line = line.strip()
        notice = line.split('\t')  # [id, sendDate, senderName, recipientName, principalName, type]
        type = notice[5]
        sender = notice[2]
        recipient = notice[3]
        principle = notice[4]
        if type == 'Dmca':
            if not dmcaSenderDic.has_key(sender):
                dmcaSenderDic[sender] = 0
            dmcaSenderDic[sender] = dmcaSenderDic[sender] + 1
            if not dmcaRecipientDic.has_key(recipient):
                dmcaRecipientDic[recipient] = 0
            dmcaRecipientDic[recipient] = dmcaRecipientDic[recipient] + 1
            if not dmcaPrincipleDic.has_key(principle):
                dmcaPrincipleDic[principle] = 0
            dmcaPrincipleDic[principle] = dmcaPrincipleDic[principle] + 1
        elif type == 'Defamation':
            if not defameSenderDic.has_key(sender):
                defameSenderDic[sender] = 0
            defameSenderDic[sender] = defameSenderDic[sender] + 1
            if not defameRecipientDic.has_key(recipient):
                defameRecipientDic[recipient] = 0
            defameRecipientDic[recipient] = defameRecipientDic[recipient] + 1
            if not defamePrincipleDic.has_key(principle):
                defamePrincipleDic[principle] = 0
            defamePrincipleDic[principle] = defamePrincipleDic[principle] + 1
        elif type == 'CourtOrder':
            if not courtSenderDic.has_key(sender):
                courtSenderDic[sender] = 0
            courtSenderDic[sender] = courtSenderDic[sender] + 1
            if not courtRecipientDic.has_key(recipient):
                courtRecipientDic[recipient] = 0
            courtRecipientDic[recipient] = courtRecipientDic[recipient] + 1
            if not courtPrincipleDic.has_key(principle):
                courtPrincipleDic[principle] = 0
            courtPrincipleDic[principle] = courtPrincipleDic[principle] + 1
        elif type == 'Other':
            if not otherSenderDic.has_key(sender):
                otherSenderDic[sender] = 0
            otherSenderDic[sender] = otherSenderDic[sender] + 1
            if not otherRecipientDic.has_key(recipient):
                otherRecipientDic[recipient] = 0
            otherRecipientDic[recipient] = otherRecipientDic[recipient] + 1
            if not otherPrincipleDic.has_key(principle):
                otherPrincipleDic[principle] = 0
            otherPrincipleDic[principle] = otherPrincipleDic[principle] + 1
        elif type == 'Trademark':
            if not tradeMarkSenderDic.has_key(sender):
                tradeMarkSenderDic[sender] = 0
            tradeMarkSenderDic[sender] = tradeMarkSenderDic[sender] + 1
            if not tradeMarkRecipientDic.has_key(recipient):
                tradeMarkRecipientDic[recipient] = 0
            tradeMarkRecipientDic[recipient] = tradeMarkRecipientDic[recipient] + 1
            if not tradeMarkPrincipleDic.has_key(principle):
                tradeMarkPrincipleDic[principle] = 0
            tradeMarkPrincipleDic[principle] = tradeMarkPrincipleDic[principle] + 1
        else:
            continue
            print 'type error'
            print type
    return dmcaSenderDic, defameSenderDic, courtSenderDic, otherSenderDic, tradeMarkSenderDic, dmcaRecipientDic, defameRecipientDic, courtRecipientDic, otherRecipientDic, tradeMarkRecipientDic, dmcaPrincipleDic, defamePrincipleDic, courtPrincipleDic, otherPrincipleDic, tradeMarkPrincipleDic

if __name__ == '__main__':
    inputPath = '/Users/JuntingYe/Desktop/network/dataset/chillingMetadata'
    outputFigPath = '/Users/JuntingYe/Desktop/network/dataset/chillingMetadata.pdf'
    dmcaSenderDic, defameSenderDic, courtSenderDic, otherSenderDic, tradeMarkSenderDic, dmcaRecipientDic, defameRecipientDic, courtRecipientDic, otherRecipientDic, tradeMarkRecipientDic, dmcaPrincipleDic, defamePrincipleDic, courtPrincipleDic, otherPrincipleDic, tradeMarkPrincipleDic = readData(inputPath)
    
    dmcaSenderDic.pop('', None)
    defameSenderDic.pop('', None)
    courtSenderDic.pop('', None)
    otherSenderDic.pop('', None)
    tradeMarkSenderDic.pop('', None)
    dmcaRecipientDic.pop('', None)
    defameRecipientDic.pop('', None)
    courtRecipientDic.pop('', None)
    otherRecipientDic.pop('', None)
    tradeMarkRecipientDic.pop('', None)
    dmcaPrincipleDic.pop('', None)
    defamePrincipleDic.pop('', None)
    courtPrincipleDic.pop('', None)
    otherPrincipleDic.pop('', None)
    tradeMarkPrincipleDic.pop('', None)
    
    dmcaSenderL = sorted(dmcaSenderDic.items(), key=lambda x: x[1], reverse=True)
    defameSenderL = sorted(defameSenderDic.items(), key=lambda x: x[1], reverse=True)
    courtSenderL = sorted(courtSenderDic.items(), key=lambda x: x[1], reverse=True)
    otherSenderL = sorted(otherSenderDic.items(), key=lambda x: x[1], reverse=True)
    tradeMarkSenderL = sorted(tradeMarkSenderDic.items(), key=lambda x: x[1], reverse=True)
    dmcaRecipientL = sorted(dmcaRecipientDic.items(), key=lambda x: x[1], reverse=True)
    defameRecipientL = sorted(defameRecipientDic.items(), key=lambda x: x[1], reverse=True)
    courtRecipientL = sorted(courtRecipientDic.items(), key=lambda x: x[1], reverse=True)
    otherRecipientL = sorted(otherRecipientDic.items(), key=lambda x: x[1], reverse=True)
    tradeMarkRecipientL = sorted(tradeMarkRecipientDic.items(), key=lambda x: x[1], reverse=True)
    dmcaPrincipleL = sorted(dmcaPrincipleDic.items(), key=lambda x: x[1], reverse=True)
    defamePrincipleL = sorted(defamePrincipleDic.items(), key=lambda x: x[1], reverse=True)
    courtPrincipleL = sorted(courtPrincipleDic.items(), key=lambda x: x[1], reverse=True)
    otherPrincipleL = sorted(otherPrincipleDic.items(), key=lambda x: x[1], reverse=True)
    tradeMarkPrincipleL = sorted(tradeMarkPrincipleDic.items(), key=lambda x: x[1], reverse=True)
    
    
    print '##########Sender'
    print "Top DMCA Senders"
    for i in range(0, min(20,len(dmcaSenderL))):
        print dmcaSenderL[i][0] + '\t' + str(dmcaSenderL[i][1])
    print "Top Defame Senders"
    for i in range(0, min(20,len(defameSenderL))):
        print defameSenderL[i][0] + '\t' + str(defameSenderL[i][1])
    print "Top Court Senders"
    for i in range(0, min(20,len(courtSenderL))):
        print courtSenderL[i][0] + '\t' + str(courtSenderL[i][1])
    print "Top Trade Mark Senders"
    for i in range(0, min(20,len(tradeMarkSenderL))):
        print tradeMarkSenderL[i][0] + '\t' + str(tradeMarkSenderL[i][1])
    print "Top Other Senders"
    for i in range(0, min(20,len(otherSenderL))):
        print otherSenderL[i][0] + '\t' + str(otherSenderL[i][1])
        
    print '##########Recipient'
    print "Top DMCA Recipients"
    for i in range(0, min(20,len(dmcaRecipientL))):
        print dmcaRecipientL[i][0] + '\t' + str(dmcaRecipientL[i][1])
    print "Top Defame Recipients"
    for i in range(0, min(20,len(defameRecipientL))):
        print defameRecipientL[i][0] + '\t' + str(defameRecipientL[i][1])
    print "Top Court Recipients"
    for i in range(0, min(20,len(courtRecipientL))):
        print courtRecipientL[i][0] + '\t' + str(courtRecipientL[i][1])
    print "Top Trade Mark Recipients"
    for i in range(0, min(20,len(tradeMarkRecipientL))):
        print tradeMarkRecipientL[i][0] + '\t' + str(tradeMarkRecipientL[i][1])
    print "Top Other Recipients"
    for i in range(0, min(20,len(otherRecipientL))):
        print otherRecipientL[i][0] + '\t' + str(otherRecipientL[i][1])

    print '##########Principle'
    print "Top DMCA Principles"
    for i in range(0, min(20,len(dmcaPrincipleL))):
        print dmcaPrincipleL[i][0] + '\t' + str(dmcaPrincipleL[i][1])
    print "Top Defame Principles"
    for i in range(0, min(20,len(defamePrincipleL))):
        print defamePrincipleL[i][0] + '\t' + str(defamePrincipleL[i][1])
    print "Top Court Principles"
    for i in range(0, min(20,len(courtPrincipleL))):
        print courtPrincipleL[i][0] + '\t' + str(courtPrincipleL[i][1])
    print "Top Trade Mark Principles"
    for i in range(0, min(20,len(tradeMarkPrincipleL))):
        print tradeMarkPrincipleL[i][0] + '\t' + str(tradeMarkPrincipleL[i][1])
    print "Top Other Principles"
    for i in range(0, min(20,len(otherPrincipleL))):
        print otherPrincipleL[i][0] + '\t' + str(otherPrincipleL[i][1])
        
    print len(dmcaPrincipleL)
    print len(defamePrincipleL)
    print len(courtPrincipleL)
    print len(otherPrincipleL)
    print len(tradeMarkPrincipleL)