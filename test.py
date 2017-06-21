import requests
import datetime

# get weather
# print weather
# ...
# profit

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

    if resp.status_code != 200:  # !=200 means status not ok
        raise ApiError('felblabbla')  # hur funkar?
    else:
        # print(resp.status_code)
        # vill inte visa passerad tid
        currentdate = int(datetime.datetime.today().strftime("%Y%m%d"))  # ().strftime("%Y-%m-%d %H:%M:%S")
        currenttime = int(datetime.datetime.now().time().strftime("%H%M%S"))
        timeSeries = resp.json()['timeSeries']

        print 'current date and time:'
        print currentdate
        print currenttime
        print '--x--'
        forecastdate = []
        forecasttime = []
        indRespStart = []

        #print resp.json()['timeSeries']

        for idx,timepoint in enumerate(timeSeries): #finds interval for which forecasts to look at
            forecasttimepoint = timepoint['validTime'].split('T')
            forecastdate = int(forecasttimepoint[0].strip('').replace("-",""))
            forecasttime = int(forecasttimepoint[1].strip('Z').replace(":",""))

            if forecastdate == currentdate:
                if forecasttime > currenttime:
                    #print 'hello'
                    indRespStart = idx-1
                    indRespEnd = idx+12 #indRespStart+10
                    break

        #print timeSeries[0]['parameters'][5]
        list1 = []
        dict1 = {"Date and Time":[], "Temperature":[],"Cloud coverage":[],"Precipitation":[]}


        for indResp in range(indRespStart,indRespEnd):
            for idx,param in enumerate(timeSeries[indResp]['parameters']):
                #print timepoint
                #param = timepoint['parameters']
                if param['name'] == 't':
                    dict1["Temperature"] = param['values']
                    #indParam.append(idx)
                if param['name'] == 'tcc_mean':
                    dict1["Cloud coverage"] = param['values']
                    #indParam.append(idx)
                if param['name'] == 'pmean':
                    dict1["Precipitation"] = param['values']
                    #precipitation.append(param)
                    #indParam.append(idx)
            list1.append(dict1)
            print dict1
        print list1
        # print '--x--'
        # print indRespStart
        # print forecastdate
        # print forecasttime
            #print forecastdate > currentdate
            # print time['parameters']
            # allParam = resp.json()['timeSeries'][0]['validTime']
            # allParam = 1

def main():
    url = API_URL + '/category/' + CATEGORY + '/version/' + VERSION + '/geotype/' + GEOTYPE + '/lon/' + LON + '/lat/' + LAT + '/data.json'

    collect_weather(url)


main()
