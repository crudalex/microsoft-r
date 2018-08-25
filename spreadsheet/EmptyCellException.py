class EmptyCellException(Exception):
    cellname: str

    def __init__(self, name: str):
        self.cellname = name
