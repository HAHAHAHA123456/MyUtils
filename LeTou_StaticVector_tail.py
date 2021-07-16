class InfoRowTail:
    position0 = 0
    position1 = 0
    position2 = 0
    position3 = 0
    position4 = 0
    position5 = 0
    position6 = 0
    position7 = 0
    position8 = 0
    position9 = 0

    def __init__(self):
        pass

    def getInfo(self):
        return self.position0, self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9

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





class InfoRowTailContinous:
    position0 = 0
    position1 = 0
    position2 = 0
    position3 = 0
    position4 = 0
    position5 = 0
    position6 = 0
    position7 = 0
    position8 = 0
    position9 = 0


    def __init__(self):
        pass

    def getInfo(self):
        return self.position0, self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9

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



class InfoRowTailLeaveOut:
    position0 = 0
    position1 = 0
    position2 = 0
    position3 = 0
    position4 = 0
    position5 = 0
    position6 = 0
    position7 = 0
    position8 = 0
    position9 = 0


    def __init__(self):
        pass
    def getInfo(self):
        return self.position0, self.position1, self.position2, self.position3, self.position4, self.position5, self.position6, self.position7, self.position8, self.position9
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


