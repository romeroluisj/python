import yfinance as yf


"""
# Ex lines from main:
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
"""


class Stock:

    def __init__(self):
        self.ticker = ""

    def set_ticker(self, ticker):
        self.ticker = ticker

    def get_ticker(self):
        return self.ticker

    def get_last_dividend(self):
        json_object = yf.Ticker(self.ticker).info
        return json_object["lastDividendValue"]
