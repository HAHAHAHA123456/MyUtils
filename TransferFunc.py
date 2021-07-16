def transferNumber(number):
    if number >= 6:
        return 1
    else:
        return 0

def transferBigNumPosition(number):
    if number == 1 or number == 4:
        return 1
    else:
        return number

def transferVectorNumber(vectorList):
    newList = []
    for ele in vectorList:
        if ele >= 6:
            newList.append(2)
        elif ele == 0:
            newList.append(0)
        else:
            newList.append(1)
    return newList