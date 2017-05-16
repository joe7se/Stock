#-*- coding:utf-8 -*-
import MySQLdb
from MySQLHelperUtil import MySQLHelperUtil
from StockEneInfo import StockEneInfo

class MySQLUtil():
    '''获取数据库的连接'''
    def getConnection(self):
        connection = False
        try:
            connection = MySQLdb.connect(host="114.212.245.165",port=3306,user="stock",passwd="NJU2017",db="stock",charset="utf8")
#             print "connect database successfully" 
        except Exception, data: 
            connection = False
            print "connect database failed, %s" % data  
        return connection
    
    '''释放数据库连接'''
    def releaseConnection(self,connection):
        if connection != False:
            connection.close()
          
    '''获取所有股票的code'''
    def getAllStockCode(self):
        stocksCode = []
        connection = self.getConnection()
        cursor = connection.cursor()
        sql = "select code from stockscodes"
        
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                code = row[0]
                stocksCode.append(code)
        except:
            print "Error: unable to fecth data"
        self.releaseConnection(connection)
        return stocksCode  
    
    '''获取某一个股票的信息'''   
    def getStockEneInfos(self,stockCode, start_date, end_date):
        stockEneInfos = []
        helper = MySQLHelperUtil()
        stockName = helper.getStockInfoTableName(stockCode)
        connection = self.getConnection()
        cursor = connection.cursor()
        sql = "select * from " + stockName + " where code = '%s' and date between '%s' and '%s'" % (stockCode, start_date, end_date)
        
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                code = row[0]
                date = row[1]
                high = row[3]
                low = row[5]
                open = row[2]
                close = row[4]
                stockEneInfo = StockEneInfo()
                stockEneInfo.setCode(code)
                stockEneInfo.setDate(date)
                stockEneInfo.setHigh(high)
                stockEneInfo.setLow(low)
                stockEneInfo.setOpen(open)
                stockEneInfo.setClose(close)
                stockEneInfos.append(stockEneInfo)
        except:
            print "Error: unable to fecth data"
        self.releaseConnection(connection)
        return stockEneInfos
#         print stockEneInfos[0].getDate()
# p=MySQLUtil()
# p.getStockEneInfos("sh600011")
