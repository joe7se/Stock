# -*- coding: UTF-8 -*- 
'''
Created on 2016年12月21日

@author: Administrator
'''
from EneParameter import EneParameter
from StockEneInfo import StockEneInfo
from CommonUtil import CommonUtil
from MySQLUtil import MySQLUtil
from EneParameterRange import EneParameterRange
import datetime


class EneQuotaUtil:
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
        self._INFOLIST=mysql.getStockEneInfos(ene_param.get_code(), ene_param.get_start_date(),
                                                ene_param.get_end_date())
        length = len(self._INFOLIST)
#         print 'len:',length
        for i in range(length):
            index = length - 1 - i
            info = self._INFOLIST[index]
            avgClose = self.getAvgClose(info, index, ene_param.get_days())
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
                for k in ene_range.getDays():
                    # print str(i)+"---"+str(j)+"---"+str(k)
                    param = EneParameter()
                    param.set_code(ene_range.get_code())
                    param.set_days(k)
                    param.set_lower(j)
                    param.set_upper(i)
                    param.set_start_date(ene_range.get_start_date())
                    param.set_end_date(ene_range.get_end_date())
                    frequency = self.get_Standard_Frequency(param)
                    print frequency
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
            print(param.get_days())
            print(param.getFrequency())
            print '---------------------------'
        return optimumParamList

    '''
    把所有股票的最优参数写入到txt中
    '''    
    def getAllStocksParam(self):
        mysqlutil = MySQLUtil()
        stocksCodes = mysqlutil.getAllStockCode()
        for index in stocksCodes:
            start = datetime.datetime.now()
#             print start
            eneparam = EneParameterRange()
            eneparam.set_code(index)
            eneparam.setDays([4,5,6,7,8,9,10])
#             eneparam.setDaysMax(11)
#             eneparam.setDaysMin(9)
            eneparam.set_lower_max(12)
            eneparam.set_lower_min(9)
            eneparam.set_upper_max(12)
            eneparam.set_upper_min(9)
            eneparam.set_end_date(2016, 10, 25)
            eneparam.set_start_date(2013,10,8)
            optimumParamList = self.get_Optimum_Param(eneparam)
            for n in range(0,len(optimumParamList)):
                fo = open("result.txt", "a")
                fo.write(optimumParamList[n].get_code()+" "+str(optimumParamList[n].get_upper())+" "+str(optimumParamList[n].get_lower())+" "+str(optimumParamList[n].get_days())+" "+str(optimumParamList[n].getFrequency())+"\n")
                fo.close()
                end = datetime.datetime.now()
#                 print (end-start).seconds
    '''
     * 回测
     *
     * @param money
     *            ENE参数
     * @return profit
    '''

    def get_profit(self, ene_param, money, up_degree, down_degree, days_interval):
        last_price = 0
        purchase_num = 0
        purchase_index = 0
        all_money = money
        mysqlutil = MySQLUtil()
        self._INFOLIST = mysqlutil.getStockEneInfos(ene_param.get_code(), ene_param.get_start_date(),
                                                ene_param.get_end_date())

        for index in range(len(self._INFOLIST)):
            info = self._INFOLIST[index]
            avgClose = self.getAvgClose(info, index, ene_param.get_days())
            upper = self.getUpperIndex(ene_param.get_upper(), avgClose)
            lower = self.getLowerIndex(ene_param.get_lower(), avgClose)

            if self.is_to_purchase(info.getClose(), last_price, down_degree, lower):
                last_price = info.getClose()
                unit = 100 * info.getClose()
                purchase_num += int(all_money / unit)
                all_money = all_money % unit
                print unit
                print purchase_num
                print "买入------"+str(purchase_num*100*info.getClose())
                print all_money
                purchase_index = index

            # 判断一个是超过上次买入价格的程度或者达到上轨线需要卖出，一个是超过天数需要卖出
            if self.is_to_sale(info.getClose(), last_price, up_degree, upper) or index - purchase_index >= days_interval:
                earn_money = purchase_num * 100 * info.getClose()
                print "得到------"+str(earn_money)
                all_money += earn_money
                purchase_num = 0

        all_money += purchase_num * 100 * self._INFOLIST[len(self._INFOLIST) - 1].getClose()

        print "获利： %s \n" % (all_money-money)

    '''
    * 决定是否需要买入
    *
    * @param now_price
    *               当前股票价格
    * @param last_price
    *               上次购买时股票价格
    * @param degree
    *               用户决定跌多少程度买入
    * @param lower
    *               当前下轨线股票价格
    * @return is_to_purchase
    *               是否需要买入
    '''
    def is_to_purchase(self, now_price, last_price, degree, lower):
        is_to_purchase = False
        if last_price == 0:
            if now_price <= lower:
                is_to_purchase = True
        else:
            degree_percentenge = float((100 - degree)/100)
            price_limit = last_price * degree_percentenge
            if now_price <= price_limit:
                is_to_purchase = True

            if now_price <= lower:
                is_to_purchase = True

        return is_to_purchase

    '''
    * 决定是否需要卖出
    *
    * @param now_price
    *               当前股票价格
    * @param last_price
    *               上次购买时股票价格
    * @param degree
    *               用户决定涨多少程度卖出
    * @param upper
    *               当前股票上轨线
    * @return is_to_sale
    *               是否需要卖出
    '''
    def is_to_sale(self, now_price, last_price, degree, upper):
        is_to_sale = False
        if last_price == 0:
            return False

        degree_percentenge = float(100 + degree)/100
        price_limit = last_price * degree_percentenge
        if now_price >= price_limit:
            is_to_sale = True
#             print "符合用户设置条件"
        if now_price >= upper:
            is_to_sale = True
#             print "达到上轨"
        return is_to_sale

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
     * 获取n天股票收盘价的均值
     *
     * @param stockEneInfo
     *            股票数据
     * @param index
     *            股票数据在股票数据集合中的下标
     * @param days
     *            n天
     * @return 收盘价均值
    '''

    def getAvgClose(self, stockEneInfo, index, days):
        date = stockEneInfo.getDate()
        commonUtil = CommonUtil()
        dateBefore = commonUtil.getDaysAfter(date, -days)
        closeList = []
        allClose = 0.0
        # print(len(_INFOLIST))
        for i in range(0, days):

            if index >= i:
                infoBefore = self._INFOLIST[index - i]
            else:
                break

            if infoBefore.getDate() >= dateBefore:
                closeList.append(infoBefore.getClose());

        for close in closeList:
            allClose += close

        avgClose = allClose / len(closeList)
        return avgClose

p = EneQuotaUtil()
p.getAllStocksParam()
# ene = EneParameter();
# ene.set_days(5);
# ene.set_lower(9);
# ene.set_upper(10);
# ene.set_code("sh600000");
# ene.set_end_date("2016-10-25")
# ene.set_start_date("2013-10-8")
# print p.get_Standard_Frequency(ene);
# eneparam = EneParameterRange()
# eneparam.setCode("sh600011")
# eneparam.setDaysMax(11)
# eneparam.setDaysMin(9)
# eneparam.setLowerMax(10)
# eneparam.setLowerMin(8)
# eneparam.setUpperMax(12)
# eneparam.setUpperMin(10)
# p.get_Optimum_Param(eneparam)
