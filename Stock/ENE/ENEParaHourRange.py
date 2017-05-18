# encoding: UTF-8
from __builtin__ import str

class EneParaHourRange:
    # 股票代号
    # code=''
    # 上限的最高值
    # upperMax=0
    # 上限的最低值
    # upperMin=0
    # 下限的最高值
    # lowerMax=0
    # 下限的最低值
    # lowerMin=0
    # 小时的最高值
    # hoursMax=0
    # 小时的最低值
    # hoursMin=0
    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_upper_max(self):
        return self.upper_max;

    def set_upper_max(self, upper_max):
        self.upper_max = upper_max

    def get_upper_min(self):
        return self.upper_min

    def set_upper_min(self, upper_min):
        self.upper_min = upper_min

    def get_lower_max(self):
        return self.lower_max

    def set_lower_max(self, lower_max):
        self.lower_max = lower_max

    def get_lower_min(self):
        return self.lower_min

    def set_lower_min(self, lower_min):
        self.lower_min = lower_min

    def getHours(self) :
        return self.hoursList
    
    def setHours(self,hoursList) :
        self.hoursList = hoursList

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, year, month, day, hour, minute, second):
        self.start_time = str(year)+'-'+str(month)+'-'+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, year, month, day, hour, minute, second):
        self.end_time = str(year)+'-'+str(month)+'-'+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)

