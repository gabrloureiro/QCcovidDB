import sched
import time
import qcCSVExtractor
import covidDBUpdate
from datetime import datetime

qcCSVExtractor.run('https://cdn-contenu.quebec.ca/cdn-contenu/sante/documents/Problemes_de_sante/covid-19/csv/cas-region-en.csv?t={}')
qcCSVExtractor.run('https://cdn-contenu.quebec.ca/cdn-contenu/sante/documents/Problemes_de_sante/covid-19/csv/cas-region-7jours-en.csv?t={}')
covidDBUpdate.showDataTable()


