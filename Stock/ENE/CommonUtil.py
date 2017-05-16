# encoding: UTF-8
import datetime

class CommonUtil():
    '''
    获取指定日期前后n天日期
    '''
    def getDaysAfter(self,date,days):
        someday = datetime.timedelta(days)
        day=date+someday
        date1 = datetime.date(day.year,day.month, day.day)
        return date1 
    
    '''
    获得一个List中的最大值的位置
    '''
    def getArrayListMax(self,list) :        
        indexList = []
        max = 0.0
        lenth=len(list)
        for i in range(0,lenth):
            temp = list[i]
            if temp > max:
                indexList=[]
                max = temp
                indexList.append(i)            
            elif temp == max:
                max = temp
                indexList.append(i)
        return indexList
     
     

# p = CommonUtil()

# print p.getArrayListMax(a)
# date=datetime.datetime(2016,12,21,0,0,0)
# print p.getDaysBefore(date, 2)

        
