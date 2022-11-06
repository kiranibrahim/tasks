'''
LIVE AIR DATA TRAFFIC REQUEST
by ideagora geomatics | www.geodose.com | @ideageo
'''
#IMPORTING LIBRARIES
import requests
import json
import csv
import time

#AREA EXTENT COORDINATE GCS WGS84
#pakista = lamin=23.350&lomin=60.500&lamax=37.050&lomax=77.500
lon_min,lat_min=60.500,23.350
lon_max,lat_max=77.500,37.050

#CSV OUPUT PATH
csv_data='/home/kiran/Desktop/Q1/data.csv'

#REST API QUERY
user_name=''
password=''
url_data='https://'+user_name+':'+password+'@opensky-network.org/api/states/all?'+'lamin='+str(lat_min)+'&lomin='+str(lon_min)+'&lamax='+str(lat_max)+'&lomax='+str(lon_max)
col_name=['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground','velocity',       
'true_track','vertical_rate','sensors','geo_altitude','squawk','spi','position_source']

#REQUEST INTERVAL
if user_name !='' and password !='':
    sleep_time=5
else:
    sleep_time=10

#GET DATA AND STORE INTO CSV
while col_name !='':
    with open(csv_data,'w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL)
        csv_writer.writerow(col_name)
        response=requests.get(url_data).json()
        
        try:
            n_response=len(response['states'])
        except Exception:
            pass
        else:
            for i in range(n_response):
                info=response['states'][i]
                csv_writer.writerow(info)
    time.sleep(sleep_time)
    print('Get',len(response['states']),'data')
