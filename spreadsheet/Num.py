from spreadsheet.IFormula import IFormula


class Num(IFormula):
    value: int
    thisCell: str

    def __init__(self, value: int):
        self.value = value
        self.thisCell = ""

    def noRefs(self):
        return True

    def valueOf(self):
        return self.value

    def getCell(self):
        return self.thisCell

    def setCell(self, cellname: str):
        self.thisCell = cellname

    def isRef(self):
        return False

    def isPlus(self):
        return False
