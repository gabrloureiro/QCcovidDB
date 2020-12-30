import urlConnector
import calendar
from covidDBUpdate import covidDBUpdate
from datetime import datetime

def formatDate(date):
    dateFormat = date.split(' ')
    year = datetime.now().year
    month = list(calendar.month_name).index(str(dateFormat[0]))
    day = dateFormat[1]
    return('{}-{}-{}'.format(year, month, day))
    
def splitData(data):
    rows = data.splitlines()
    dates = rows[0].split(';')
    for i in range(1, (len(rows) - 3)):
        cells = rows[i].split(';')
        for n in range(1, (len(cells) - 1)):
            regionId = cells[0].split(' - ')[0]
            cases = cells[n]
            if covidDBUpdate.dataExists(formatDate(dates[n]), regionId) == False:
                covidDBUpdate.dbRowInsert(regionId, formatDate(dates[n]), cases)
            else:
                print(('Region #{}: Data already exists for this date ({})').format(regionId, dates[n]))

def formatUrlTime(address):
    address.format(datetime.now())
    return(address)

def run(link):
    formatUrlTime(link)
    csv = urlConnector.getData(link, 'utf-8')
    splitData(csv)
    return()

#run('https://cdn-contenu.quebec.ca/cdn-contenu/sante/documents/Problemes_de_sante/covid-19/csv/cas-region-7jours-en.csv?t={}')
