# -*- coding: utf-8 -*-
import json

def readFiles(inpath,URLsDic):
    notices = []
    urlId = 0
    infile = open(inpath)
    for line in infile:
#         print line
        line = line.strip()
        data = json.loads(line)
        data = data[data.keys()[0]]
        if data.has_key('id'):
            id = data['id']
        else:
            id = '-1'
        if data.has_key('date_sent'):
            sendDate = data['date_sent']
        else:
            sendDate = '-1'
            
        if data.has_key('sender_name'):
            senderName = data['sender_name']
        else:
            senderName = '-1'
            
        if data.has_key('recipient_name'):
            recipientName = data['recipient_name']
        else:
            recipientName = '-1'
            
        if data.has_key('principal_name'):
            principalName = data['principal_name']
        else:
            principalName = '-1'
            
        if data.has_key('type'):
            type = data['type']
        else:
            type = '-1'
            
#         if data.has_key('works'):
#             works = data['works']
#         else:
#             works = '-1'
        
#         if works != '-1' and len(works) != 0 and works[0].has_key('infringing_urls'):
#             infringingURLs = data['works'][0]['infringing_urls']
#         else:
#             infringingURLs = '-1'
#             
#         if works != '-1' and len(works) != 0 and works[0].has_key('copyrighted_urls'):
#             copyrightedURLs = data['works'][0]['copyrighted_urls']
#         else:
#             copyrightedURLs = '-1'
        if sendDate==None:
            sendDate = ''
        if senderName==None:
            senderName = ''
        if recipientName==None:
            recipientName = ''
        if principalName==None:
            principalName = ''
        notice = [id, sendDate, senderName.replace('\t', ' '), recipientName.replace('\t', ' '), principalName.replace('\t', ' '), type]
#         notice = [id, sendDate, senderName, recipientName, principalName, type, [], []]
#         if infringingURLs != '-1':
#             for url in infringingURLs:
#                 url = url['url']
#                 if not URLsDic.has_key(url):
#                     URLsDic[url] = urlId
#                     urlId = urlId + 1
#                 notice[6].append(URLsDic[url])
#         if copyrightedURLs != '-1':
#             for url in copyrightedURLs:
#                 url = url['url']
#                 if not URLsDic.has_key(url):
#                     URLsDic[url] = urlId
#                     urlId = urlId + 1
#                 notice[7].append(URLsDic[url])
        notices.append(notice)
    infile.close()
    return notices

def writeFiles(outputPath,notices):
    outfile = open(outputPath+'chillingMetadata','a')
    for notice in notices:
#         print notice
        outfile.write(str(notice[0])+'\t'+str(notice[1].encode('utf-8'))+'\t'+str(notice[2].encode('utf-8'))+'\t'+str(notice[3].encode('utf-8'))+'\t'+str(notice[4].encode('utf-8'))+'\t'+str(notice[5].encode('utf-8'))+'\n')
#         infringingURLs = notice[6]
#         for url in infringingURLs:
#             outfile.write(str(url)+';')
#         copyrightedURLs = notice[7]
#         for url in copyrightedURLs:
#             outfile.write(str(url)+';')
#         outfile.write('\n')
    outfile.close() 
    
def writeDic(outputPath,URLsDic):
    outfile = open(outputPath+'urlMapping','w')
    for key in URLsDic.keys():
        outfile.write(str(key)+'\t'+URLsDic[key]+'\n')
    outfile.close() 
    
if __name__ == '__main__':
    sourceDataPath = '/Volumes/大房/chillingEffectDataset/'
    outputPath = '/Users/JuntingYe/Desktop/network/dataset/'
    URLsDic = {}
    for i in range(1,2100000,100000):
        print i
#     for i in range(1, 100000, 100000):
        filePath = sourceDataPath + "chilling" + str(i) + "_" + str(i + 100000 - 1) + "Cleaned"
        notices = readFiles(filePath,URLsDic)
        writeFiles(outputPath,notices)
#     writeDic(outputPath,URLsDic)
