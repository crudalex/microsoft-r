from spreadsheet.IFormula import IFormula


class Plus(IFormula):
    left: IFormula
    right: IFormula
    thisCell: str

    def __init__(self, left: IFormula, right: IFormula):
        self.left = left
        self.right = right
        self.thisCell = ""

    def noRefs(self):
        return self.left.noRefs() and self.right.noRefs()

    def valueOf(self):
        return self.left.valueOf() + self.right.valueOf()

    def getCell(self):
        return self.thisCell

    def setCell(self, cellname: str):
        self.thisCell = cellname

    def isRef(self):
        return False

    def isPlus(self):
        return True
