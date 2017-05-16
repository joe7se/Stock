# encoding: UTF-8
class EneParameter:
    # 股票代号
    # code=''
    # ENE指标上限
    # upper=0
    # ENE指标下限
    # lower=0
    # ENE天数
    # days=0

    def get_upper(self):
        return self.upper

    def set_upper(self, upper):
        self.upper = upper

    def get_lower(self):
        return self.lower

    def set_lower(self, lower):
        self.lower = lower

    def get_days(self):
        return self.days

    def set_days(self, days):
        self.days = days

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_start_date(self):
        return self.start_date
        
    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def getFrequency(self) :
        return self.frequency
    
    def setFrequency(self,frequency) :
        self.frequency = frequency