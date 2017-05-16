# encoding: UTF-8

class EneParameterRange:
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
    # 天数的最高值
    # daysMax=0
    # 天数的最低值
    # daysMin=0
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

    def getDays(self) :
        return self.daysList
    
    def setDays(self,daysList) :
        self.daysList = daysList
        
#     def get_days_max(self):
#         return self.days_max
# 
#     def set_days_max(self, days_max):
#         self.days_max = days_max
# 
#     def get_days_min(self):
#         return self.days_min;
# 
#     def set_days_min(self, days_min):
#         self.days_min = days_min

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, year, month, day):
        self.start_date = str(year)+'-'+str(month)+'-'+str(day)

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, year, month, day):
        self.end_date = str(year)+'-'+str(month)+'-'+str(day)

