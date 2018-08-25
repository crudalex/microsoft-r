from spreadsheet.IFormula import IFormula


class ISpreadsheet:

    def editContents(self, cellname: str, expr: IFormula):
        pass

    def lookupValue(self, forcell: str):
        pass
