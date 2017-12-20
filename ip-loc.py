#Get current Public IP address and location

import requests

ip = requests.get('https://api.ipify.org?format=json')
ip_add = ip.json()
geoloc = requests.get('http://ip-api.com/json/'+ip_add['ip'])
loc_details = geoloc.json()
print 'Your public IP address is: '+ip_add['ip']
print 'Location: '+ loc_details['city'] + ', ' + loc_details['regionName'] + ', ' + loc_details['country']
print 'Coordinates: ' + str(loc_details['lat']) + ',' + str(loc_details['lon']) 
print 'Timezone: ' + loc_details['timezone']
print 'ISP: ' + loc_details['isp']
#My public IP address is: 122.177.96.251