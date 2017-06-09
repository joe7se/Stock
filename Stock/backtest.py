import datetime
from sort import Sort


# volumeOfDate 最高成交量对应的日期
# volumeOfHigh 最高成交量对应的最高价
# highOfDate 当天的最高价

class BackTest:
    def __init__(self, today, timelen):
        self.sortObject = Sort()
        self.cursor = self.sortObject.getCursor()
        self.sortarr = self.sortObject.sort(today, timelen)
        self.today = today

    def getTimelen(self, code):
        for arrtemp in self.sortarr:
            if arrtemp[0]['code'] == code:
                if arrtemp[1] >= arrtemp[2] and arrtemp[1] >= arrtemp[3]:
                    return 1
                if arrtemp[2] >= arrtemp[1] and arrtemp[2] >= arrtemp[3]:
                    return 2
                if arrtemp[3] >= arrtemp[1] and arrtemp[3] >= arrtemp[2]:
                    return 3

    def getHighToday(self, cursor, code, date):
        year = date.year
        # print(date)
        high = 0
        cursor.execute("select high from stocksdayinfo" + str(year) + " WHERE code = '" + code + "' and date = '"
                       + date.strftime("%Y-%m-%d") + "'")
        for row in cursor:
            # print("row")
            high = row['high']
            # print(high)
        return high

    def isBuyPoint(self, nowdate, todayprice, volumeOfDate, priceOfvolume, cursor, code):
        # highOfDate = getHigh(date)
        # volumeOfHigh = getHigh(date)
        if (self.isValid(volumeOfDate, nowdate, priceOfvolume, cursor, code)):
            if (todayprice <= priceOfvolume * 0.9):
                return True
        return False

    def isSellPoint(self, nowprice, buyprice):
        # highOfDate = getHigh(date)
        if (nowprice >= buyprice * 1.15):
            return True
        return False

    def isValid(self, volumeOfDate, nowdate, priceOfvolume, cursor, code):
        # volumeOfHigh = getHigh(date1)
        # date1 = volumeOfDate
        date2 = nowdate
        date1 = datetime.datetime.strptime(str(volumeOfDate), "%Y-%m-%d")
        # date2 = datetime.datetime.strptime(str(nowdate), "%Y-%m-%d")

        while date1 <= date2:
            # current = date1.strftime("%Y-%m-%d")
            highOfCurrent = self.getHighToday(cursor, code, date1)
            if highOfCurrent > priceOfvolume:
                return False
            date1 += datetime.timedelta(days=1)
        return True

    def loopBackTest(self, cursorOfCode, cursorOfDate):

        arr = []
        for code in cursorOfCode:
            print(code)
            # tag表示能否买入
            tag = True
            dateOfBuy = "null"
            rate = 0
            rateList = [{'code': code}]
            price = 0
            timelen = self.getTimelen(code)
            cursor = self.cursor
            year = self.today.year
            cursor.execute("select date,high,volume from stocksdayinfo" + str(year) + " WHERE code = '" + code + "' ")
            volumearr = self.sortObject.getmaxVolume(cursor, self.today, timelen)
            volumeOfDate = volumearr['volumeOfDate']
            priceOfvolume = volumearr['volumeOfHigh']

            for date in cursorOfDate:
                nowprice = self.getHighToday(cursor, code, date)
                if nowprice == 0:
                    continue
                if self.isBuyPoint(date, nowprice, volumeOfDate, priceOfvolume, cursor, code) and tag:
                    tag = False
                    dateOfBuy = date
                    price = nowprice

                if dateOfBuy != "null":
                    # priceOfCurrent = getHigh(date)
                    rate = (nowprice - price) / price
                if self.isSellPoint(nowprice, price) and not tag:
                    tag = True
                    dateOfBuy = "null"
                rateList.append(rate)
            arr.append(rateList)
        return arr


# if __name__ == "__main__":
#     today = datetime.datetime(2017, 3, 16)
#     test = BackTest(today, 1)
#     codes = ['sz300585', 'sz300582']
#     dates = []
#
#     for i in range(0, 120):
#         d = 120 - i
#         temp = today + datetime.timedelta(days=-d)
#         dates.append(temp)
#
#     print(test.loopBackTest(codes, dates))
#     test.sortObject.conclose()
