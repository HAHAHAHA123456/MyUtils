zhiNumberList = [1, 2, 3, 5, 7, 11]
def static_odd_big_zhiNumber(list):
    oddNumber = 0
    bigNumber = 0
    zhiNumber = 0
    for li in list:
        if li % 2 == 1:
            oddNumber += 1
        if li >= 7:
            bigNumber += 1
        if li in zhiNumberList:
            zhiNumber += 1
    return oddNumber, bigNumber, zhiNumber


def staticCounts_Continous_leaveOut(dataList, number):
    idx = 0
    countsNumber = 0
    continousNumber = 0
    leave_outNumber = 0
    maxContinous = 0
    maxLeaveNumber = 0
    while idx < len(dataList):
        if number in dataList[idx]:
            countsNumber += 1
            continousNumber += 1
            leave_outNumber = 0
            if continousNumber > maxContinous:
                maxContinous = continousNumber
        else:
            continousNumber = 0
            leave_outNumber += 1
            if leave_outNumber > maxLeaveNumber:
                maxLeaveNumber = leave_outNumber
        idx += 1
    return countsNumber, maxContinous, maxLeaveNumber

def staticCounts_Continous_leaveOutFindMax(dataList, continousInfo, leaveOutInfo, number):
    idx = 0
    countsNumber = 0
    maxContinous = 0
    maxLeaveNumber = 0
    while idx < len(dataList):
        if number in dataList[idx]:
            countsNumber += 1
        if idx != len(dataList) - 1:
            if continousInfo[idx][number - 1] > maxContinous:
                maxContinous = continousInfo[idx][number - 1]
            if leaveOutInfo[idx][number - 1] > maxLeaveNumber:
                maxLeaveNumber = leaveOutInfo[idx][number - 1]
        idx += 1
    return countsNumber, maxContinous, maxLeaveNumber

def staticLotteryNumber(dataList):
    staticInfo_dict = {}
    for i in range(1, 13):
        tempDict = {}
        countsNumber, maxContinous, maxLeaveNumber = staticCounts_Continous_leaveOut(dataList=dataList, number=i)
        tempDict['countsNumber'] = countsNumber
        tempDict['maxContinous'] = maxContinous
        tempDict['maxLeaveNumber'] = maxLeaveNumber
        staticInfo_dict[str(i)] = tempDict
    return staticInfo_dict

def staticLotteryNumberWithInfo(dataList, continousInfo, leaveOutInfo):
    staticInfo_dict = {}
    for i in range(1, 13):
        tempDict = {}
        countsNumber, maxContinous, maxLeaveNumber = staticCounts_Continous_leaveOutFindMax(dataList=dataList,
                                                                                            continousInfo=continousInfo,
                                                                                            leaveOutInfo=leaveOutInfo,
                                                                                            number=i)
        tempDict['countsNumber'] = countsNumber
        tempDict['maxContinous'] = maxContinous
        tempDict['maxLeaveNumber'] = maxLeaveNumber
        staticInfo_dict[str(i)] = tempDict
    return staticInfo_dict

def direct1_staticCounts(dataList, number):
    idx = 0
    countsNumber = 0
    while idx < len(dataList):
        if number in list(dataList[idx]):
            countsNumber += 1
        idx += 1
    return countsNumber

def direct1_staticLotteryNumber(dataList):
    staticVariables = []
    temp_dict = {}
    for i in range(1, 13):
        staticVariables.append(direct1_staticCounts(dataList=dataList, number=i))
    for idx, values in enumerate(staticVariables, 1):
        temp_dict[idx] = values
    return temp_dict
    # vocab_to_int = {c:i for i, c in enumerate(vocab)}
    # int_to_vocab = dict(enumerate(vocab))
    # print(vocab_to_int, int_to_vocab)

if __name__ == '__main__':
    pass


