class CyclicFormulaException(Exception):
    cellname: str

    def __init__(self, cellname: str):
        self.cellname = cellname
