from python.stock import Stock
from numbers_parser import Document


def main():
    stock = Stock()
    stock.set_ticker("Bac")
    print(stock.get_last_dividend())

    doc = Document("../docs/Example.numbers")
    sheets = doc.sheets()
    tables = sheets["Sheet 1"].tables()
    table = tables["Table 1"]

    # row, column syntax
    print("Cell C2 contains", table.cell(2, 1))
    # Excel/Numbers-style cell references
    print("Cell C2 contains", table.cell("B3"))
    print("Cell C2 contains", table.cell("C2"))


if __name__ == '__main__':
    main()
