import numpy as np
np.set_printoptions(threshold=np.inf)
import pymysql

from sys import path
path.append(r"C:/MyUtils")
import StaticFunc as static
import TransferFunc as transferFunc
from tensorflow.contrib import slim

batch_sizeToPredict = 10
batch_size = 1
maxNum = 64

def transferNumber(vectorList):
    newList = []
    for ele in vectorList:
        if ele >= maxNum:
            newList.append(maxNum)
        else:
            newList.append(ele)
    return newList

def getTotalData():
    db = pymysql.connect("localhost", 'root', '123456', 'lottery')
    cursor = db.cursor()
    sql = "SELECT * FROM lotteryData_2015"
    sql2 = "SELECT * FROM lotteryData_2016"
    sql3 = "SELECT * FROM lotteryData_2017"
    sql4 = "SELECT * FROM lotteryData_2018"
    sql5 = "SELECT * FROM lotteryData_2019"
    sql6 = "SELECT * FROM lotteryData_2020"
    try:
        cursor.execute(sql)
        results_tuple1 = cursor.fetchall()
        cursor.execute(sql2)
        results_tuple2 = cursor.fetchall()
        cursor.execute(sql3)
        results_tuple3 = cursor.fetchall()
        cursor.execute(sql4)
        results_tuple4 = cursor.fetchall()
        cursor.execute(sql5)
        results_tuple5 = cursor.fetchall()
        cursor.execute(sql6)
        results_tuple6 = cursor.fetchall()
    except:
        print("Error: unable to fecth data")
    results = list(results_tuple1)
    results.extend(list(results_tuple2))
    results.extend(list(results_tuple3))
    results.extend(list(results_tuple4))
    results.extend(list(results_tuple5))
    results.extend(list(results_tuple6))
    return results

class InfoRowContinous:
    position1 = 0
    position2 = 0
    position3 = 0
    position4 = 0
    position5 = 0
    position6 = 0
    position7 = 0
    position8 = 0
    position9 = 0
    position10 = 0
    position11 = 0
    def __init__(self):
        pass
    def getInfo(self):
        return self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9, self.position10, self.position11
    def check(self, currentList):
        if 1 in currentList:
            self.position1 += 1
        else:
            self.position1 = 0

        if 2 in currentList:
            self.position2 += 1
        else:
            self.position2 = 0

        if 3 in currentList:
            self.position3 += 1
        else:
            self.position3 = 0

        if 4 in currentList:
            self.position4 += 1
        else:
            self.position4 = 0

        if 5 in currentList:
            self.position5 += 1
        else:
            self.position5 = 0

        if 6 in currentList:
            self.position6 += 1
        else:
            self.position6 = 0

        if 7 in currentList:
            self.position7 += 1
        else:
            self.position7 = 0

        if 8 in currentList:
            self.position8 += 1
        else:
            self.position8 = 0

        if 9 in currentList:
            self.position9 += 1
        else:
            self.position9 = 0

        if 10 in currentList:
            self.position10 += 1
        else:
            self.position10 = 0

        if 11 in currentList:
            self.position11 += 1
        else:
            self.position11 = 0


class InfoRow:
    position1 = 0
    position2 = 0
    position3 = 0
    position4 = 0
    position5 = 0
    position6 = 0
    position7 = 0
    position8 = 0
    position9 = 0
    position10 = 0
    position11 = 0
    def __init__(self):
        pass
    def getInfo(self):
        return self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9, self.position10, self.position11
    def check(self, currentList):
        if 1 in currentList:
            self.position1 = 1
        else:
            self.position1 = 0

        if 2 in currentList:
            self.position2 = 1
        else:
            self.position2 = 0

        if 3 in currentList:
            self.position3 = 1
        else:
            self.position3 = 0

        if 4 in currentList:
            self.position4 = 1
        else:
            self.position4 = 0

        if 5 in currentList:
            self.position5 = 1
        else:
            self.position5 = 0

        if 6 in currentList:
            self.position6 = 1
        else:
            self.position6 = 0

        if 7 in currentList:
            self.position7 = 1
        else:
            self.position7 = 0

        if 8 in currentList:
            self.position8 = 1
        else:
            self.position8 = 0

        if 9 in currentList:
            self.position9 = 1
        else:
            self.position9 = 0

        if 10 in currentList:
            self.position10 = 1
        else:
            self.position10 = 0

        if 11 in currentList:
            self.position11 = 1
        else:
            self.position11 = 0

class InfoRowLeaveout:
    position1 = 0
    position2 = 0
    position3 = 0
    position4 = 0
    position5 = 0
    position6 = 0
    position7 = 0
    position8 = 0
    position9 = 0
    position10 = 0
    position11 = 0
    def __init__(self):
        pass
    def getInfo(self):
        return self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9, self.position10, self.position11
    def check(self, currentList):
        if 1 not in currentList:
            self.position1 += 1
        else:
            self.position1 = 0

        if 2 not in currentList:
            self.position2 += 1
        else:
            self.position2 = 0

        if 3 not in currentList:
            self.position3 += 1
        else:
            self.position3 = 0

        if 4 not in currentList:
            self.position4 += 1
        else:
            self.position4 = 0

        if 5 not in currentList:
            self.position5 += 1
        else:
            self.position5 = 0

        if 6 not in currentList:
            self.position6 += 1
        else:
            self.position6 = 0

        if 7 not in currentList:
            self.position7 += 1
        else:
            self.position7 = 0

        if 8 not in currentList:
            self.position8 += 1
        else:
            self.position8 = 0

        if 9 not in currentList:
            self.position9 += 1
        else:
            self.position9 = 0

        if 10 not in currentList:
            self.position10 += 1
        else:
            self.position10 = 0

        if 11 not in currentList:
            self.position11 += 1
        else:
            self.position11 = 0

def makeData(batch_sizeToPredict, batch_size, isTrain):
    results = getTotalData()
    if isTrain:
        results = results[0: -5890]
    else:
        # results = results[-10000: -5890]
        results = results[-5890: ]

    totalElementsDictList = []
    infoRow = InfoRow()
    infoRowLeaveout = InfoRowLeaveout()
    infoRowContinous = InfoRowContinous()
    for info in results:
        tempList = []
        tempExtendList = []
        tempDict = {}
        for element in info[1].split(','):
            tempList.append(int(element))
            tempExtendList.append(int(element))
        tempList.sort()
        tempExtendList.sort()
        tempExtendList.extend(static.static_odd_big_zhiNumber(tempList))
        infoRow.check(tempList)
        infoRowLeaveout.check(tempList)
        infoRowContinous.check(tempList)

        #处理数据字典
        tempDict['dataValue'] = tempExtendList
        tempDict['date'] = info[2]
        tempDict['sequenceNum'] = info[3]
        tempDict['infoVector'] = transferNumber(list(infoRow.getInfo()))
        tempDict['infoTableLeaveout'] = transferNumber(list(infoRowLeaveout.getInfo()))
        tempDict['infoTableContinous'] = transferNumber(list(infoRowContinous.getInfo()))
        totalElementsDictList.append(tempDict)

    XExtend = []
    YExtend = []
    idx2 = 0

    totalElementsNums = len(totalElementsDictList)
    while idx2 < totalElementsNums - batch_sizeToPredict:
        tempXExtend = []
        for i in range(idx2, idx2 + batch_sizeToPredict):
            tempXExtend.append(totalElementsDictList[i])
        XExtend.append(tempXExtend)
        YExtend.append(totalElementsDictList[idx2 + batch_sizeToPredict])
        idx2 += 1
    totalNums = len(XExtend)
    batches = totalNums // batch_size
    XExtend = XExtend[:batches * batch_size]
    YExtend = YExtend[:batches * batch_size]
    newTotalNums = len(XExtend)
    print(newTotalNums)
    random_index = np.random.permutation(newTotalNums)
    normal_index = range(0, newTotalNums)
    XExtend = np.asarray(XExtend)
    YExtend = np.asarray(YExtend)

    for idx in range(0, batches):
        startIdx = idx * batch_size
        endIdx = startIdx + batch_size
        if isTrain:
            batch_idx = random_index[startIdx: endIdx]
        else:
            batch_idx = normal_index[startIdx: endIdx]
        yield XExtend[batch_idx], YExtend[batch_idx]

if __name__ == '__main__':

    testStep = 0
    for xExtend, yExtend in makeData(batch_size=batch_size,
                                     batch_sizeToPredict=batch_sizeToPredict,
                                     isTrain=True
                                    ):
        # staticVariables = []
        # for element in x:
        #     staticVariables.append(static.staticLotteryNumber(element))
        # print(staticVariables)
        # print(len(staticVariables))
        print(xExtend)
        print("t"*50)
        print(yExtend)
        print("*"*50)