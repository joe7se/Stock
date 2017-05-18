# -*- coding: UTF-8 -*- 

from MySQLUtil import MySQLUtil
from ENEHourParameter import EneHourParameter
from ENEParaHourRange import EneParaHourRange
from StockEneInfo import StockEneInfo
from CommonUtil import CommonUtil
import datetime

class ENEQuotaHourUtil:
    
    '''
    用来存储一个股票的所有信息
    '''
    _INFOLIST = []
    
    '''
     * 获取一个股票在指定ENE参数内的适宜程度
     *
     * @param eneParameter
     *            ENE参数
     * @return 适宜程度
    '''

    def get_Standard_Frequency(self, ene_param):
        times = 0
        mysql = MySQLUtil()
        # print ene_param.get_start_date()
        self._INFOLIST=mysql.getAllStockHourInfos(ene_param.get_code(), ene_param.get_start_time(),
                                                ene_param.get_end_time())
        length = len(self._INFOLIST)
#         print 'len:',length
        for i in range(length):
            index = length - 1 - i
            info = self._INFOLIST[index]
            avgClose = self.getAvgClose(info, index, ene_param.get_hours())
#             print "close: ",avgClose
            upper = self.getUpperIndex(ene_param.get_upper(), avgClose)
            # print upper
            lower = self.getLowerIndex(ene_param.get_lower(), avgClose)
            # print lower
            if info.getHigh() <= upper and info.getLow() >= lower:
                times = times + 1

        frequency = float(times) / length
#         print frequency
        return frequency
    
    '''
     * 获取一个股票最适宜的ENE参数
     * 
     * @param stockCode
     *            股票代号
     * @return 最适宜的ENE参数
    '''

    def get_Optimum_Param(self, ene_range):
        frequencyList = []
        paramList = []
        for i in range(ene_range.get_upper_min(), ene_range.get_upper_max() + 1):
            for j in range(ene_range.get_lower_min(), ene_range.get_lower_max() + 1):
                for k in ene_range.getHours():
                    # print str(i)+"---"+str(j)+"---"+str(k)
                    param = EneHourParameter()
                    param.set_code(ene_range.get_code())
                    param.set_hours(k)
                    param.set_lower(j)
                    param.set_upper(i)
                    param.set_start_time(ene_range.get_start_time())
                    param.set_end_time(ene_range.get_end_time())
                    frequency = self.get_Standard_Frequency(param)
#                     print frequency
                    param.setFrequency(frequency)
                    frequencyList.append(frequency)
                    paramList.append(param)

        commonutil = CommonUtil()
        indexList = commonutil.getArrayListMax(frequencyList)
        optimumParamList = []
        for index in indexList:
            param = paramList[index]
            optimumParamList.append(param)
#             print(frequencyList[index])
            print(param.get_code())
            print(param.get_upper())
            print(param.get_lower())
            print(param.get_hours())
            print(param.getFrequency())
            print '---------------------------'
        return optimumParamList
    
    '''
    测一个
    '''    
    def getAllStocksParam(self):
        mysqlutil = MySQLUtil()
        stocksCodes = mysqlutil.getAllStockCode()
        for index in stocksCodes:
            start = datetime.datetime.now()
#             print start
            eneparam = EneParaHourRange()
            eneparam.set_code(index)
            eneparam.setHours([12,16,20,24,28])
#             eneparam.setDaysMax(11)
#             eneparam.setDaysMin(9)
            eneparam.set_lower_max(10)
            eneparam.set_lower_min(5)
            eneparam.set_upper_max(10)
            eneparam.set_upper_min(5)
            eneparam.set_end_time(2016, 10, 25,0,0,0)
            eneparam.set_start_time(2016,10,8,0,0,0)
            optimumParamList = self.get_Optimum_Param(eneparam)
#             for n in range(0,len(optimumParamList)):
#                 fo = open("result.txt", "a")
#                 fo.write(optimumParamList[n].get_code()+" "+str(optimumParamList[n].get_upper())+" "+str(optimumParamList[n].get_lower())+" "+str(optimumParamList[n].get_days())+" "+str(optimumParamList[n].getFrequency())+"\n")
#                 fo.close()
#                 end = datetime.datetime.now()
    
    '''
     * 获取ENE指标上限
     * 
     * @param upper
     *            偏移程度
     * @param avgClose
     *            平均收盘价
     * @return
    '''

    def getUpperIndex(self, upper, avgClose):
        floatDegree = float(upper) / 100
        upperIndex = (1 + floatDegree) * avgClose
        return upperIndex

    '''
     * 获取ENE指标下限
     * 
     * @param lower
     *            偏移程度
     * @param avgClose
     *            平均收盘价
     * @return
    '''

    def getLowerIndex(self, lower, avgClose):
        floatDegree = float(lower) / 100
        lowerIndex = (1 - floatDegree) * avgClose
        return lowerIndex
    
    '''
     * 获取n小时股票收盘价的均值
     *
     * @param stockEneInfo
     *            股票数据
     * @param index
     *            股票数据在股票数据集合中的下标
     * @param days
     *            n小时
     * @return 收盘价均值
    '''

    def getAvgClose(self, stockEneInfo, index, hours):
#         date = stockEneInfo.getDate()
        code = stockEneInfo.getCode()
        
#         mysqlUtil = MySQLUtil()
#         hourInfo = mysqlUtil.getStockEneHourInfos(code,date,hours)
#         commonUtil = CommonUtil()
#         dateBefore = commonUtil.getDaysAfter(date, -days)
        closeList = []
        allClose = 0.0
        # print(len(_INFOLIST))
        
        for i in range(0, hours):

            if index >= i:
                infoBefore = self._INFOLIST[index - i]
#                 print 'date'
#                 print(infoBefore.getDate())
#                 print(infoBefore.getClose())
                closeList.append(infoBefore.getClose())
            else:
                break

#             if infoBefore.getDate() >= dateBefore:
#                 closeList.append(infoBefore.getClose());
                
        for close in closeList:
            allClose+=close

        avgClose = allClose / len(closeList)
        print "avg:"
        print avgClose
        return avgClose

    
p = ENEQuotaHourUtil()
eneparam = EneParaHourRange()
eneparam.set_code("sh600011")
eneparam.setHours([12,16])
#             eneparam.setDaysMax(11)
#             eneparam.setDaysMin(9)
eneparam.set_lower_max(10)
eneparam.set_lower_min(5)
eneparam.set_upper_max(10)
eneparam.set_upper_min(5)
eneparam.set_end_time(2016, 11, 11,10,0,0)
eneparam.set_start_time(2016,10,8,10,0,0)
p.get_Optimum_Param(eneparam)