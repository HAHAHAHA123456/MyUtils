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

def transferNumber(vectorList):
    newList = []
    for ele in vectorList:
        if ele >= 6:
            newList.append(2)
        elif ele == 0:
            newList.append(0)
        else:
            newList.append(1)
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
    position12 = 0
    position13 = 0
    position14 = 0
    position15 = 0
    position16 = 0
    position17 = 0
    position18 = 0
    position19 = 0
    position20 = 0
    position21 = 0
    position22 = 0
    position23 = 0
    position24 = 0
    position25 = 0
    position26 = 0
    position27 = 0
    position28 = 0
    position29 = 0
    position30 = 0
    position31 = 0
    position32 = 0
    position33 = 0
    position34 = 0
    position35 = 0
    def __init__(self):
        pass

    def getInfo(self):
        return self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9, self.position10, self.position11, self.position12, self.position13, self.position14, self.position15, self.position16, self.position17, self.position18, self.position19, self.position20, self.position21, self.position22, self.position23, self.position24, self.position25, self.position26, self.position27, self.position28, self.position29, self.position30, self.position31, self.position32, self.position33, self.position34, self.position35,

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

        if 12 in currentList:
            self.position12 = 1
        else:
            self.position12 = 0

        if 13 in currentList:
            self.position13 = 1
        else:
            self.position13 = 0

        if 14 in currentList:
            self.position14 = 1
        else:
            self.position14 = 0

        if 15 in currentList:
            self.position15 = 1
        else:
            self.position15 = 0

        if 16 in currentList:
            self.position16 = 1
        else:
            self.position16 = 0

        if 17 in currentList:
            self.position17 = 1
        else:
            self.position17 = 0

        if 18 in currentList:
            self.position18 = 1
        else:
            self.position18 = 0

        if 19 in currentList:
            self.position19 = 1
        else:
            self.position19 = 0

        if 20 in currentList:
            self.position20 += 1
        else:
            self.position20 = 0

        if 21 in currentList:
            self.position21 = 1
        else:
            self.position21 = 0

        if 22 in currentList:
            self.position22 = 1
        else:
            self.position22 = 0

        if 23 in currentList:
            self.position23 = 1
        else:
            self.position23 = 0

        if 24 in currentList:
            self.position24 = 1
        else:
            self.position24 = 0

        if 25 in currentList:
            self.position25 = 1
        else:
            self.position25 = 0

        if 26 in currentList:
            self.position26 = 1
        else:
            self.position26 = 0

        if 27 in currentList:
            self.position27 = 1
        else:
            self.position27 = 0

        if 28 in currentList:
            self.position28 = 1
        else:
            self.position28 = 0

        if 29 in currentList:
            self.position29 = 1
        else:
            self.position29 = 0

        if 30 in currentList:
            self.position30 = 1
        else:
            self.position30 = 0

        if 31 in currentList:
            self.position31 = 1
        else:
            self.position31 = 0

        if 32 in currentList:
            self.position32 = 1
        else:
            self.position32 = 0

        if 33 in currentList:
            self.position33 = 1
        else:
            self.position33 = 0

        if 34 in currentList:
            self.position34 = 1
        else:
            self.position34 = 0

        if 35 in currentList:
            self.position35 = 1
        else:
            self.position35 = 0

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
    position12 = 0
    position13 = 0
    position14 = 0
    position15 = 0
    position16 = 0
    position17 = 0
    position18 = 0
    position19 = 0
    position20 = 0
    position21 = 0
    position22 = 0
    position23 = 0
    position24 = 0
    position25 = 0
    position26 = 0
    position27 = 0
    position28 = 0
    position29 = 0
    position30 = 0
    position31 = 0
    position32 = 0
    position33 = 0
    position34 = 0
    position35 = 0
    def __init__(self):
        pass

    def getInfo(self):
        return self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9, self.position10, self.position11, self.position12, self.position13, self.position14, self.position15, self.position16, self.position17, self.position18, self.position19, self.position20, self.position21, self.position22, self.position23, self.position24, self.position25, self.position26, self.position27, self.position28, self.position29, self.position30, self.position31, self.position32, self.position33, self.position34, self.position35,

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

        if 12 in currentList:
            self.position12 += 1
        else:
            self.position12 = 0

        if 13 in currentList:
            self.position13 += 1
        else:
            self.position13 = 0

        if 14 in currentList:
            self.position14 += 1
        else:
            self.position14 = 0

        if 15 in currentList:
            self.position15 += 1
        else:
            self.position15 = 0

        if 16 in currentList:
            self.position16 += 1
        else:
            self.position16 = 0

        if 17 in currentList:
            self.position17 += 1
        else:
            self.position17 = 0

        if 18 in currentList:
            self.position18 += 1
        else:
            self.position18 = 0

        if 19 in currentList:
            self.position19 += 1
        else:
            self.position19 = 0

        if 20 in currentList:
            self.position20 += 1
        else:
            self.position20 = 0

        if 21 in currentList:
            self.position21 += 1
        else:
            self.position21 = 0

        if 22 in currentList:
            self.position22 += 1
        else:
            self.position22 = 0

        if 23 in currentList:
            self.position23 += 1
        else:
            self.position23 = 0

        if 24 in currentList:
            self.position24 += 1
        else:
            self.position24 = 0

        if 25 in currentList:
            self.position25 += 1
        else:
            self.position25 = 0

        if 26 in currentList:
            self.position26 += 1
        else:
            self.position26 = 0

        if 27 in currentList:
            self.position27 += 1
        else:
            self.position27 = 0

        if 28 in currentList:
            self.position28 += 1
        else:
            self.position28 = 0

        if 29 in currentList:
            self.position29 += 1
        else:
            self.position29 = 0

        if 30 in currentList:
            self.position30 += 1
        else:
            self.position30 = 0

        if 31 in currentList:
            self.position31 += 1
        else:
            self.position31 = 0

        if 32 in currentList:
            self.position32 += 1
        else:
            self.position32 = 0

        if 33 in currentList:
            self.position33 += 1
        else:
            self.position33 = 0

        if 34 in currentList:
            self.position34 += 1
        else:
            self.position34 = 0

        if 35 in currentList:
            self.position35 += 1
        else:
            self.position35 = 0


class InfoRowLeaveOut:
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
    position12 = 0
    position13 = 0
    position14 = 0
    position15 = 0
    position16 = 0
    position17 = 0
    position18 = 0
    position19 = 0
    position20 = 0
    position21 = 0
    position22 = 0
    position23 = 0
    position24 = 0
    position25 = 0
    position26 = 0
    position27 = 0
    position28 = 0
    position29 = 0
    position30 = 0
    position31 = 0
    position32 = 0
    position33 = 0
    position34 = 0
    position35 = 0
    def __init__(self):
        pass
    def getInfo(self):
        return self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9, self.position10, self.position11, self.position12, self.position13, self.position14, self.position15, self.position16, self.position17, self.position18, self.position19, self.position20, self.position21, self.position22, self.position23, self.position24, self.position25, self.position26, self.position27, self.position28, self.position29, self.position30, self.position31, self.position32, self.position33, self.position34, self.position35,
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

        if 12 not in currentList:
            self.position12 += 1
        else:
            self.position12 = 0

        if 13 not in currentList:
            self.position13 += 1
        else:
            self.position13 = 0

        if 14 not in currentList:
            self.position14 += 1
        else:
            self.position14 = 0

        if 15 not in currentList:
            self.position15 += 1
        else:
            self.position15 = 0

        if 16 not in currentList:
            self.position16 += 1
        else:
            self.position16 = 0

        if 17 not in currentList:
            self.position17 += 1
        else:
            self.position17 = 0

        if 18 not in currentList:
            self.position18 += 1
        else:
            self.position18 = 0

        if 19 not in currentList:
            self.position19 += 1
        else:
            self.position19 = 0

        if 20 not in currentList:
            self.position20 += 1
        else:
            self.position20 = 0

        if 21 not in currentList:
            self.position21 += 1
        else:
            self.position21 = 0

        if 22 not in currentList:
            self.position22 += 1
        else:
            self.position22 = 0

        if 23 not in currentList:
            self.position23 += 1
        else:
            self.position23 = 0

        if 24 not in currentList:
            self.position24 += 1
        else:
            self.position24 = 0

        if 25 not in currentList:
            self.position25 += 1
        else:
            self.position25 = 0

        if 26 not in currentList:
            self.position26 += 1
        else:
            self.position26 = 0

        if 27 not in currentList:
            self.position27 += 1
        else:
            self.position27 = 0

        if 28 not in currentList:
            self.position28 += 1
        else:
            self.position28 = 0

        if 29 not in currentList:
            self.position29 += 1
        else:
            self.position29 = 0

        if 30 not in currentList:
            self.position30 += 1
        else:
            self.position30 = 0

        if 31 not in currentList:
            self.position31 += 1
        else:
            self.position31 = 0

        if 32 not in currentList:
            self.position32 += 1
        else:
            self.position32 = 0

        if 33 not in currentList:
            self.position33 += 1
        else:
            self.position33 = 0

        if 34 not in currentList:
            self.position34 += 1
        else:
            self.position34 = 0

        if 35 not in currentList:
            self.position35 += 1
        else:
            self.position35 = 0

def makeData(batch_sizeToPredict, batch_size, isTrain):
    results = getTotalData()
    if isTrain:
        results = results[-34000: -5890]
    else:
        results = results[-5890: ]

    totalElementsDictList = []
    infoRow = InfoRow()
    infoRowLeaveOut = InfoRowLeaveOut()
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
        infoRowLeaveOut.check(tempList)
        infoRowContinous.check(tempList)

        #处理数据字典
        tempDict['dataValue'] = tempExtendList
        tempDict['date'] = info[2]
        tempDict['sequenceNum'] = info[3]
        # tempDict['infoVector'] = transferNumber(list(infoRowLeaveOut.getInfo()))
        tempDict['infoVector'] = list(infoRow.getInfo())
        tempDict['infoTableLeaveout'] = list(infoRowLeaveOut.getInfo())
        tempDict['infoTableContinous'] = list(infoRowContinous.getInfo())
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
                                     isTrain=False
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