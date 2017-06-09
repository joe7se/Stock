import pymysql
import time
import datetime

# 最高成交量
maxVolume = 0
# 最高成交量对应的日期
volumeOfDate = "null"
# 最高成交量对应的最高价
volumeOfHigh = 0
# 更高价对应的日期
dateOfHigher = "null"
# 最高成交量之后的更高价
year = [2013, 2014, 2015, 2016]
higher = 0
intervals = [1, 2, 3]
# accuracy = [];


def getmaxVolume(cursor, start, end):
    for row in cursor:
        if str(row['date']) < start:
            continue
        elif str(row['date']) > end:
            break
        else:
            if row['volume'] > maxVolume:
                global maxVolume
                global volumeOfDate
                global volumeOfHigh
                maxVolume = row['volume']
                volumeOfDate = row['date']
                volumeOfHigh = row['high']
    print("volumeOfDate:", volumeOfDate)
    print("volumeOfHigh:", volumeOfHigh)
    print("maxVolume:", maxVolume)


def getHigher(cursor):
    for row in cursor:
        if str(row['date']) >= str(volumeOfDate):
            if row['high'] > volumeOfHigh:
                global dateOfHigher
                global higher
                dateOfHigher = row['date']
                higher = row['high']
                break
    print("dateOfHigher:", dateOfHigher)
    print("higher:", higher)


def datetime_offset_by_month(datetime1, n=1):
    # create a shortcut object for one day
    one_day = datetime.timedelta(days=1)

    # first use div and mod to determine year cycle
    q, r = divmod(datetime1.month + n, 12)

    # create a datetime2
    # to be the last day of the target month
    datetime2 = datetime.datetime(
        datetime1.year + q, r + 1, 1) - one_day

    if datetime1.month != (datetime1 + one_day).month:
        return datetime2

    if datetime1.day >= datetime2.day:
        return datetime2

    return datetime2.replace(day=datetime1.day)


def getAccuracy(cursor):
    # accuracy = []
    total = 0
    num = [0, 0, 0]

    for t in year:
        startdate = datetime.datetime(t, 1, 1)
        enddate = datetime.datetime(t, 6, 30)

        startdate = startdate.strftime("%Y-%m-%d")
        enddate = enddate.strftime("%Y-%m-%d")
        print("start:", startdate, "enddate:", enddate)

        getmaxVolume(cursor, startdate, enddate)
        getHigher(cursor)

        if volumeOfDate != "null":
            total += 1
            mvdt = datetime.datetime.strptime(str(volumeOfDate), "%Y-%m-%d %H:%M:%S")
            hdt = datetime.datetime.strptime(str(dateOfHigher), "%Y-%m-%d %H:%M:%S")

            for i in range(0, 3):
                tt = datetime_offset_by_month(mvdt, intervals[i])
                if hdt < tt:
                    num[i] += 1
            print('interval days:', (hdt - mvdt).days)

            global maxVolume
            maxVolume = 0

        startdate = datetime.datetime(t, 7, 1)
        enddate = datetime.datetime(t, 12, 31)

        startdate = startdate.strftime("%Y-%m-%d")
        enddate = enddate.strftime("%Y-%m-%d")
        print("start:", startdate, "enddate:", enddate)

        getmaxVolume(cursor, startdate, enddate)
        getHigher(cursor)

        if volumeOfDate != "null":
            total += 1
            mvdt = datetime.datetime.strptime(str(volumeOfDate), "%Y-%m-%d %H:%M:%S")
            hdt = datetime.datetime.strptime(str(dateOfHigher), "%Y-%m-%d %H:%M:%S")

            for i in range(0, 3):
                tt = datetime_offset_by_month(mvdt, intervals[i])
                if hdt < tt:
                    num[i] += 1
            print('interval days:', (hdt - mvdt).days)

            global maxVolume
            maxVolume = 0

    accuracy = [num[0] / total, num[1] / total, num[2] / total]
    # accuracy.append(temp)

    return accuracy

if __name__ == "__main__":
    try:
        coon = pymysql.connect(host="121.42.143.164", port=3306, user="admin", passwd="NJU2016", db="stock")
        cursor = coon.cursor(pymysql.cursors.DictCursor)
    except:
        print("connect mysql error")

    stockcodes = []
    cursor.execute("select distinct code from StocksBasicInfo")
    file_object = open('result2.txt', 'w')
    rlist = []
    stockcodes = list(cursor.fetchall())

    # for row in cursor.fetchall():
    #     if row['code'] not in stockcodes:
    #         stockcodes.append(row['code'])

    for s in stockcodes:
        code = s['code']
        endstr = code[-1]
        # print(endstr)
        cursor.execute("select date,high,volume from StocksKInfo"+endstr+" WHERE code = '" + code + "' ")
        accuracy = getAccuracy(cursor.fetchall())

        for i in range(0, 3):
            rlist.append(code+" "+str(i+1)+" : "+str(accuracy[i])+"\n")

    file_object.writelines(rlist)
    file_object.close()