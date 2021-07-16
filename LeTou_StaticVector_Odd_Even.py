class InfoRowOdd:
    position0 = 0
    position1 = 0
    position2 = 0


    def __init__(self):
        pass

    def getInfo(self):
        return self.position0, self.position1, self.position2

    def check(self, currentList):
        if 0 in currentList:
            self.position0 = 1
        else:
            self.position0 = 0

        if 1 in currentList:
            self.position1 = 1
        else:
            self.position1 = 0

        if 2 in currentList:
            self.position2 = 1
        else:
            self.position2 = 0



class InfoRowOddContinous:
    position0 = 0
    position1 = 0
    position2 = 0


    def __init__(self):
        pass

    def getInfo(self):
        return self.position0, self.position1, self.position2

    def check(self, currentList):
        if 0 in currentList:
            self.position0 += 1
        else:
            self.position0 = 0

        if 1 in currentList:
            self.position1 += 1
        else:
            self.position1 = 0

        if 2 in currentList:
            self.position2 += 1
        else:
            self.position2 = 0



class InfoRowOddLeaveOut:
    position0 = 0
    position1 = 0
    position2 = 0


    def __init__(self):
        pass
    def getInfo(self):
        return self.position0, self.position1, self.position2
    def check(self, currentList):
        if 0 not in currentList:
            self.position0 += 1
        else:
            self.position0 = 0

        if 1 not in currentList:
            self.position1 += 1
        else:
            self.position1 = 0

        if 2 not in currentList:
            self.position2 += 1
        else:
            self.position2 = 0


class InfoRowEven:
    position0 = 0
    position1 = 0
    position2 = 0

    def __init__(self):
        pass

    def getInfo(self):
        return self.position0, self.position1, self.position2

    def check(self, currentList):
        if 0 in currentList:
            self.position0 = 1
        else:
            self.position0 = 0

        if 1 in currentList:
            self.position1 = 1
        else:
            self.position1 = 0

        if 2 in currentList:
            self.position2 = 1
        else:
            self.position2 = 0


class InfoRowEvenContinous:
    position0 = 0
    position1 = 0
    position2 = 0

    def __init__(self):
        pass

    def getInfo(self):
        return self.position0, self.position1, self.position2

    def check(self, currentList):
        if 0 in currentList:
            self.position0 += 1
        else:
            self.position0 = 0

        if 1 in currentList:
            self.position1 += 1
        else:
            self.position1 = 0

        if 2 in currentList:
            self.position2 += 1
        else:
            self.position2 = 0


class InfoRowEvenLeaveOut:
    position0 = 0
    position1 = 0
    position2 = 0

    def __init__(self):
        pass

    def getInfo(self):
        return self.position0, self.position1, self.position2

    def check(self, currentList):
        if 0 not in currentList:
            self.position0 += 1
        else:
            self.position0 = 0

        if 1 not in currentList:
            self.position1 += 1
        else:
            self.position1 = 0

        if 2 not in currentList:
            self.position2 += 1
        else:
            self.position2 = 0


