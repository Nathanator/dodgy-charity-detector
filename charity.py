import urllib.request
import csv

def get_charity(charity_no):

    url = "https://beta.charitycommission.gov.uk/umbraco/api/CharityApi/ExportDetailsToCsv?regid=" + str(charity_no) + "&subid=0"

    req = urllib.request.urlopen(url)

    csvtext = req.read().decode()

    reader = csv.DictReader(csvtext.split("\n"))

    def tocharity(charity):
        for key, value in charity.items():
            newvalue = None
            
            if value and value[-1] == '%':
                newvalue = float(value[0:-1]) / 100
            
            if value and value[0]:
                if ord(value[0]) == 163:
                    newvalue = value[1:]

                    if newvalue[-1] == 'M':
                        newvalue = float(newvalue[:-1]) * 1000000
                    elif newvalue[-1] == 'K':
                        newvalue = float(newvalue[:-1]) * 1000
                    elif newvalue[-1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                        newvalue = float(newvalue[:-1]) * 1

            if newvalue is not None:
                charity[key] = newvalue

        return charity

    for row in reader:
        return tocharity(row)

CHARITY_NAME = "Charity name"
INCOME = "Total income"
SPENDING = "Total spending"
INCOME_GENERATION = "Income generation and governance"



