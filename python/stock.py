import yfinance as yf


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
