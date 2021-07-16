class InfoRowBig:
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




class InfoRowBigContinous:
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



class InfoRowBigLeaveOut:
    position0 = 0
    position1 = 0
    position2 = 0
    position3 = 0
    position4 = 0
    position5 = 0


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


class InfoRowSmall:
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


class InfoRowSmallContinous:
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


class InfoRowSmallLeaveOut:
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


