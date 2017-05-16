# encoding: UTF-8
import re
 
class MySQLHelperUtil:
    def getStockInfoTableName(self,stockCode):
        pattern = re.compile(r'\d+')
        m = pattern.search(stockCode)
        tableName = "stocksdaykinfo"
        if m:
            code = long(m.group())
#             print code
        index = str(code%10)
        tableName+=index
        return tableName
              
# p=MySQLHelperUtil()
# print p.getStockInfoTableName('sh600023')