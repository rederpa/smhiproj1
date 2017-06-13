import requests
import datetime

#get weather
#print weather
#...
#profit

# coord for HOME
CATEGORY = 'pmp2g'
VERSION = '2'
GEOTYPE = 'point'
LON = '18.093713'
LAT = '59.304687'

API_URL = 'https://opendata-download-metfcst.smhi.se/api'


def collect_weather(url):
    # DATAINFORMATION:
    #
    # approvedTime
    # referenceTime
    # geometry -    type,
    #               coordinates
    # timeSeries -  validTime,
    #               parameters - name,
    #                           leveltype,
    #                           level,
    #                           values

    resp = requests.get(url)

    if resp.status_code != 200: #!=200 means status not ok
        raise ApiError('felblabbla') # hur funkar?
    else:
        #print(resp.status_code)
#vill inte visa passerad tid
        currentdate = datetime.datetime.today().strftime("%Y%m%d") #().strftime("%Y-%m-%d %H:%M:%S")
        currenttime = datetime.datetime.time().strftime("%H%M%S")
        print currentdate
        print currenttime
        
        for timepoint in resp.json()['timeSeries']:
            forecasttimepoint = timepoint['validTime'].split('t')
            print forecasttimepoint
            forecastdate = int(forecasttimepoint[0].strip('t'))
            forecasttime = int(forecasttimepoint[1].strip('z'))
            print forecastdate
            print forecastdate > currentdate

            #print time['parameters']
        #allParam = resp.json()['timeSeries'][0]['validTime']
        #allParam = 1



def main():
    url = API_URL+'/category/'+CATEGORY+'/version/'+VERSION+'/geotype/'+GEOTYPE+'/lon/'+LON+'/lat/'+LAT+'/data.json'

    collect_weather(url)

main()
