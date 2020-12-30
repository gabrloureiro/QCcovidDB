import urlConnector
from datetime import datetime
from dbConnector import dataBase
import covidDBUpdate

def dateFormat(date):
    dateArray = date.split('-')
    correctedDate = '{}-{}-{}'.format(dateArray[2],dateArray[1],dateArray[0])
    return(correctedDate)

def dbFetch(infoToGet, initialDate, finalDate):
    db = dataBase('CovidData')
    regions = db.execute('SELECT * FROM dbo.Region')
    for region in regions:
        regionCode = region.Code
        regionId = region.Id
        jsonSave(infoToGet, regionId, regionCode, initialDate, finalDate)
    return()

def jsonSave(infoToGet, regionId, regionCode, initialDate, finalDate):
    covidDB = covidDBUpdate.covidDBUpdate()
    covidDeathsDB = covidDBUpdate.covidDeathsUpdate()
    regionData = urlConnector.getJson('https://api.opencovid.ca/timeseries?stat={}&loc={}&after={}&before={}'.format(infoToGet, regionCode,initialDate, finalDate), 'utf-8')
    regionInfo = regionData[infoToGet]
    if len(regionInfo) == 0:
        print("This data isn't available yet (region #{}, {}), please check back later!".format(regionId, finalDate))
        return()
    else:
        if infoToGet == 'mortality':
            for deaths in regionInfo:
                totalDeaths = deaths['deaths']
                date = deaths['date_death_report']
                #print(regionId, dateFormat(date), totalDeaths)
                if covidDeathsDB.dataExists(dateFormat(date), regionId) == False:
                    #print(regionId, dateFormat(date), totalDeaths)
                    covidDeathsDB.dbRowInsert(regionId, dateFormat(date), str(totalDeaths))
                    print('Region #{}: Data successfully updated for the date: {}'.format(regionId, date))
                else:
                    print('Region #{}: Data already exists for the date: {}'.format(regionId, date))
        elif infoToGet == 'cases':
            for cases in regionInfo:
                totalCases = cases['cases']
                date = cases['date_report']
                #print(regionId, dateFormat(date), totalCases)
                if covidDB.dataExists(dateFormat(date), regionId) == False:
                    #print(regionId, dateFormat(date), totalCases)
                    covidDB.dbRowInsert(regionId, dateFormat(date), str(totalCases))
                    print('Region #{}: Data successfully updated for the date: {}'.format(regionId, date))
                else:
                    print('Region #{}: Data already exists for the date: {}'.format(regionId, date))
        return()




    


        
