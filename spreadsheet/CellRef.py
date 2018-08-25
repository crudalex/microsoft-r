from spreadsheet.IFormula import IFormula


class CellRef(IFormula):
    refCell: str
    thisCell: str

    def __init__(self, cellname: str):
        self.refCell = cellname
        self.thisCell = ""

    def noRefs(self):
        return False  # boolean

    def valueOf(self):
        raise RuntimeError("Unresolved cell reference")

    def getCell(self):
        return self.thisCell

    def setCell(self, cellname: str):
        self.thisCell = cellname

    def isRef(self):
        return True

    def isPlus(self):
        return False
