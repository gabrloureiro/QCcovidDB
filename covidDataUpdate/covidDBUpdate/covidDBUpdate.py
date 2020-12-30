import dbConnector
import pyodbc


class covidDBUpdate:

    def __init__(self):
        self.db = dbConnector.dataBase('CovidData')

    def dataExists(self, date, regionId):
        existingData = self.db.execute(("SELECT COUNT(*) FROM dbo.DailyCases WHERE Date = '{}' AND RegionId = {}").format(date, regionId)).fetchone()
        return(existingData[0] > 0)

    def dbRowInsert(self, regionId, date, totalCases):
        totalCases = totalCases.strip()
        if totalCases.isnumeric() == True:
            sqlString = ("INSERT INTO dbo.DailyCases (RegionId, Date, TotalCases) VALUES ({}, '{}', {})").format(regionId, date, totalCases)
            self.db.execute(sqlString)
            self.db.commit()
        else:
            print('Data not found for {}'.format(date))
        return()

    def showDataTable(self):
        table = self.db.execute('SELECT * FROM DailyCases D INNER JOIN Region R ON D.RegionId = R.Id ORDER BY D.RegionId, Date')
        for line in table:
            print(line)
        return()

class covidDeathsUpdate:

    def __init__(self):
        self.db = dbConnector.dataBase('CovidData')

    def dataExists(self, date, regionId):
        existingData = self.db.execute(("SELECT COUNT(*) FROM dbo.DailyDeaths WHERE Date = '{}' AND RegionId = {}").format(date, regionId)).fetchone()
        return(existingData[0] > 0)

    def dbRowInsert(self, regionId, date, totalDeaths):
        totalDeaths = totalDeaths.strip()
        if totalDeaths.isnumeric() == True:
            sqlString = ("INSERT INTO dbo.DailyDeaths (RegionId, Date, TotalDeaths) VALUES ({}, '{}', {})").format(regionId, date, totalDeaths)
            self.db.execute(sqlString)
            self.db.commit()
        else:
            print('Data not found for {}'.format(date))
        return()

    def showDataTable(self):
        table = self.db.execute('SELECT * FROM DailyDeaths D INNER JOIN Region R ON D.RegionId = R.Id ORDER BY D.RegionId, Date')
        for line in table:
            print(line)
        return()