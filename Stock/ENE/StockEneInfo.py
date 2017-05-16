# encoding: UTF-8
#import datetime,calendar

class StockEneInfo :
    #股票的代号 code
    #股票的日期 date
    #股票的最高价 high
    #股票的最低价 low
    #股票的开盘价 open
    #股票的收盘价 close
    
    def getCode(self) :
        return self.code
    
    def setCode(self, code) :
        self.code = code
    
    def getDate(self) :
        return self.date
    
    def setDate(self, date) :
        self.date = date
    
    def getHigh(self) :
        return self.high
    
    def setHigh(self, high) :
        self.high = high
    
    def getLow(self) :
        return self.low
    
    def setLow(self, low) :
        self.low = low
    
    def getOpen(self) :
        return self.open
    
    def setOpen(self, open) :
        self.open = open
    
    def getClose(self) :
        return self.close
    
    def setClose(self, close) :
        self.close = close
    
