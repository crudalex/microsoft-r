from collections import deque

from spreadsheet import CellRef
from spreadsheet.CyclicFormulaException import CyclicFormulaException
from spreadsheet.EmptyCellException import EmptyCellException
from spreadsheet.IFormula import IFormula
from spreadsheet.ISpreadsheet import ISpreadsheet
from spreadsheet.Plus import Plus


class Spreadsheet(ISpreadsheet):
    data = dict()

    def __init__(self):
        pass

    def editContents(self, cellname: str, expr: IFormula):
        expr.setCell(cellname)
        self.data[cellname] = expr

    def lookupValue(self, forcell: str):
        theCell = self.data.get(forcell)
        if (theCell != None):
            return self.lookupValueWithCycles(self.data.get(forcell), deque())

        else:
            raise EmptyCellException(forcell)

    def lookupValueWithCycles(self, theCell: IFormula, referenced: deque):
        if theCell is None:
            raise EmptyCellException(theCell.getCell())
            return

        if theCell.noRefs():
            return theCell.valueOf()

        if theCell.isPlus():
            plus: Plus = theCell
            return int(self.lookupValueWithCycles(plus.right, referenced)) + int(
                self.lookupValueWithCycles(plus.left, referenced))

        if theCell.isRef():
            cellref: CellRef = theCell
            nextCell = cellref.refCell

            if nextCell in referenced:
                raise CyclicFormulaException(nextCell)
                return

            referenced.append(nextCell)
            nextFormula = self.data.get(nextCell)

            if nextFormula is None:
                raise EmptyCellException(nextCell)
                return

            return self.lookupValueWithCycles(nextFormula, referenced)
