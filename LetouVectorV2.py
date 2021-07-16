import numpy as np
import tensorflow as tf
import os
from queue import Queue
np.set_printoptions(threshold=np.inf)
import LeTou_StaticFunc as static
import pymysql

batch_sizeToPredict = 1
batch_size = 1

def transferNumber(vectorList):
    newList = []
    for ele in vectorList:
        if ele >= 100:
            newList.append(100)
        else:
            newList.append(ele)
    return newList

def transferPrimeNumber(vectorList):
    newList = []
    for ele in vectorList:
        if ele >= 100:
            newList.append(100)
        else:
            newList.append(ele)
    return newList

def getTotalData():
    db = pymysql.connect(host="localhost", user='root', password='123456', db='mysql', port=3306)
    cursor = db.cursor()
    sql_2007 = "SELECT * FROM letou_2007"
    sql_2008 = "SELECT * FROM letou_2008"
    sql_2009 = "SELECT * FROM letou_2009"
    sql_2010 = "SELECT * FROM letou_2010"
    sql_2011 = "SELECT * FROM letou_2011"
    sql_2012 = "SELECT * FROM letou_2012"
    sql_2013 = "SELECT * FROM letou_2013"
    sql_2014 = "SELECT * FROM letou_2014"
    sql_2015 = "SELECT * FROM letou_2015"
    sql  = "SELECT * FROM letou_2016"
    sql2 = "SELECT * FROM letou_2017"
    sql3 = "SELECT * FROM letou_2018"
    sql4 = "SELECT * FROM letou_cnn"
    sql5 = "SELECT * FROM letou_2021"
    try:
        cursor.execute(sql_2007)
        results_2007 = cursor.fetchall()
        cursor.execute(sql_2008)
        results_2008 = cursor.fetchall()
        cursor.execute(sql_2009)
        results_2009 = cursor.fetchall()
        cursor.execute(sql_2010)
        results_2010 = cursor.fetchall()
        cursor.execute(sql_2011)
        results_2011 = cursor.fetchall()
        cursor.execute(sql_2012)
        results_2012 = cursor.fetchall()
        cursor.execute(sql_2013)
        results_2013 = cursor.fetchall()
        cursor.execute(sql_2014)
        results_2014 = cursor.fetchall()
        cursor.execute(sql_2015)
        results_2015 = cursor.fetchall()

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
    except:
        print("Error: unable to fecth data")
    results = list(results_2007)
    results.extend(list(results_2008))
    results.extend(list(results_2009))
    results.extend(list(results_2010))
    results.extend(list(results_2011))
    results.extend(list(results_2012))
    results.extend(list(results_2013))
    results.extend(list(results_2014))
    results.extend(list(results_2015))
    results.extend(list(results_tuple1))
    results.extend(list(results_tuple2))
    results.extend(list(results_tuple3))
    results.extend(list(results_tuple4))
    results.extend(list(results_tuple5))
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

def makeData(batch_sizeToPredict, batch_size, isTrain, isValidation):
    results = getTotalData()
    if isTrain:
        results = results[0: -1]
    elif isValidation:
        results = results[-150: -20]
    elif (not isTrain) and (not isValidation):
        # results = results
        results = results[-100 - batch_sizeToPredict:]
    print(len(results))

    totalElementsDictList = []
    infoRow = InfoRow()
    infoRowLeaveOut = InfoRowLeaveOut()
    infoRowContinous = InfoRowContinous()
    infoRowBlue = InfoRowBlue()
    infoRowLeaveOutBlue = InfoRowLeaveOutBlue()
    infoRowContinousBlue = InfoRowContinousBlue()

    for info in results:
        tempList = []
        tempExtendList = []
        staticList = []
        tempDict = {}
        for element in info[1].split(','):
            tempList.append(int(element))
            tempExtendList.append(int(element))
        staticList.extend(static.static_odd_big_zhiNumber(tempExtendList[0: 5]))
        staticList.extend(static.static_even_small_compositeNumber(tempExtendList[0: 5]))

        #处理数据字典
        tempDict['dataValueRed'] = tempExtendList[0: 5]
        tempDict['dataValueBlue'] = tempExtendList[5: 7]
        tempDict['static'] = staticList
        tempDict['date'] = info[2]
        tempDict['sequenceNum'] = info[3]

        infoRow.check(transferNumber(tempDict['dataValueRed']))
        infoRowLeaveOut.check(transferNumber(tempDict['dataValueRed']))
        infoRowContinous.check(transferNumber(tempDict['dataValueRed']))
        infoRowBlue.check(transferNumber(tempDict['dataValueBlue']))
        infoRowLeaveOutBlue.check(transferNumber(tempDict['dataValueBlue']))
        infoRowContinousBlue.check(transferNumber(tempDict['dataValueBlue']))

        tempDict['infoVector'] = list(infoRow.getInfo())
        tempDict['infoTableLeaveout'] = list(infoRowLeaveOut.getInfo())
        tempDict['infoTableContinous'] = list(infoRowContinous.getInfo())
        tempDict['infoVectorBlue'] = list(infoRowBlue.getInfo())
        tempDict['infoTableLeaveoutBlue'] = list(infoRowLeaveOutBlue.getInfo())
        tempDict['infoTableContinousBlue'] = list(infoRowContinousBlue.getInfo())
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
    XExtend = XExtend[-batches * batch_size:]
    YExtend = YExtend[-batches * batch_size:]

    newTotalNums = len(XExtend)
    print(newTotalNums)
    random_index = np.random.permutation(newTotalNums)
    normal_index = range(0, newTotalNums)
    XExtend = np.asarray(XExtend)
    YExtend = np.asarray(YExtend)

    output_filename = os.path.join("./TFRecord_lottery", "train2" + '.tfrecords')
    with tf.python_io.TFRecordWriter(output_filename) as tfrecord_writer:
        for idx in range(0, batches):
            startIdx = idx * batch_size
            endIdx = startIdx + batch_size
            if isTrain:
                batch_idx = normal_index[startIdx: endIdx]
            else:
                batch_idx = normal_index[startIdx: endIdx]
            # features = image_to_tfexample(XExtend[batch_idx], YExtend[batch_idx])
            example = image_to_tfexample(XExtend[batch_idx], YExtend[batch_idx])
            tfrecord_writer.write(example.SerializeToString())
            yield XExtend[batch_idx], YExtend[batch_idx]

def int64_feature(values):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=values))

def image_to_tfexample(XData, YData):
    Xinfo = XData[0][0]
    Yinfo = YData[0]
    print(Xinfo)
    print(Xinfo['infoVector'])
    # Abstract base class for protocol messages.
    return tf.train.Example(features=tf.train.Features(feature={
        'XinfoVector': int64_feature(Xinfo['infoVector']),
        'XinfoTableLeaveout': int64_feature(Xinfo['infoTableLeaveout']),
        'XinfoTableContinous': int64_feature(Xinfo['infoTableContinous']),
        'XinfoVectorBlue': int64_feature(Xinfo['infoVectorBlue']),
        'XinfoTableLeaveoutBlue': int64_feature(Xinfo['infoTableLeaveoutBlue']),
        'XinfoTableContinousBlue': int64_feature(Xinfo['infoTableContinousBlue']),
    }))


class InfoRowBlue:
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

    def __init__(self):
        pass

    def getInfo(self):
        return self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9, self.position10, self.position11, self.position12

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


class InfoRowContinousBlue:
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

    def __init__(self):
        pass

    def getInfo(self):
        return self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9, self.position10, self.position11, self.position12

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


class InfoRowLeaveOutBlue:
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

    def __init__(self):
        pass
    def getInfo(self):
        return self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9, self.position10, self.position11, self.position12
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


def seperateNUmber(listParam):
    onePosition = 0
    twoPosition = 0
    threePosition = 0
    for ele in listParam:
        if ele <= 21:
            onePosition += 1
        elif ele > 21 and ele <= 28:
            twoPosition += 1
        elif ele > 28:
            threePosition += 1
    return onePosition, twoPosition, threePosition

zhiNumberList = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
def primeNumberNum(listParam):
    num = 0
    for ele in listParam:
        if ele in zhiNumberList:
            num += 1
    return num



if __name__ == '__main__':

    testStep = 0
    totalBigNumList = []
    # for xExtend, yExtend in makeData(batch_size=batch_size,
    #                                  batch_sizeToPredict=batch_sizeToPredict,
    #                                  isTrain=True,
    #                                  isValidation = False):
    #     if yExtend[0]['dataValueRed'] == [1, 2, 4, 6, 28]:
    #         print(yExtend)
        # staticVariables = []
        # for element in x:
        #     staticVariables.append(static.staticLotteryNumber(element))
        # print(staticVariables)
        # print(len(staticVariables))

    #     if yExtend[0]['static'][1] == 5:
    #         # print(xExtend)
    #         dataValue = yExtend[0]['dataValueRed']
    #         sequenceNum = yExtend[0]['sequenceNum']
    #         print("{}      {}      {}      {}".format(dataValue, seperateNUmber(dataValue), primeNumberNum(dataValue), sequenceNum))
    #         totalBigNumList.append(yExtend[0]['dataValueRed'])
    #         # print("*"*50)
    # print(len(totalBigNumList))

    # for xExtend, yExtend in makeData(batch_size=batch_size,
    #                                  batch_sizeToPredict=batch_sizeToPredict,
    #                                  isTrain=True,
    #                                  isValidation=False):
    #     print(xExtend)
    #     print(yExtend)
    #     print("---"*60)

    for serialized_example in tf.python_io.tf_record_iterator('./TFRecord_lottery/train2.tfrecords'):
        example = tf.train.Example()
        example.ParseFromString(serialized_example)
        x_1 = np.array(example.features.feature['XinfoVector'].int64_list.value)
        x_2 = np.array(example.features.feature['XinfoTableLeaveout'].int64_list.value)
        x_3 = np.array(example.features.feature['XinfoTableContinous'].int64_list.value)
        x_4 = np.array(example.features.feature['XinfoVectorBlue'].int64_list.value)
        x_5 = np.array(example.features.feature['XinfoTableLeaveoutBlue'].int64_list.value)
        x_6 = np.array(example.features.feature['XinfoTableContinousBlue'].int64_list.value)
        print(x_1)
        print(x_2)
        print(x_3)
        print(x_4)
        print(x_5)
        print(x_6)
        print("-"*70)
