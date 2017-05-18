# encoding: UTF-8
class EneHourParameter:
    # 股票代号
    # code=''
    # ENE指标上限
    # upper=0
    # ENE指标下限
    # lower=0
    # ENE小时数
    # hours=0

    def get_upper(self):
        return self.upper

    def set_upper(self, upper):
        self.upper = upper

    def get_lower(self):
        return self.lower

    def set_lower(self, lower):
        self.lower = lower

    def get_hours(self):
        return self.hours

    def set_hours(self, hours):
        self.hours = hours

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_start_time(self):
        return self.start_time
        
    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def getFrequency(self) :
        return self.frequency
    
    def setFrequency(self,frequency) :
        self.frequency = frequency