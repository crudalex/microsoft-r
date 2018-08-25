from pprint import pprint

from spreadsheet.CellRef import CellRef
from spreadsheet.Num import Num
from spreadsheet.Plus import Plus
from spreadsheet.Spreadsheet import Spreadsheet

if __name__ == '__main__':
    s: Spreadsheet = Spreadsheet()
    s.editContents("a10", Num(5))
    s.editContents("b10", Num(3))
    s.editContents("c10", Plus(CellRef("a10"), CellRef("b10")))

    a = s.lookupValue("c10")

    s.editContents("a10", Num(9))
    b = s.lookupValue("c10")

    s.editContents("a10", CellRef("c10"))

    try:
        c = s.lookupValue("a10")
    except Exception as e:
        pprint(e)

    s.editContents("a10", CellRef("a10"))
    try:
        d = s.lookupValue("a10")
    except Exception as e:
        pprint(e)
