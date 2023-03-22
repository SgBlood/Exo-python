import requests
import math
# EXO 2
# reponse = requests.get("https://gbfs.citibikenyc.com/gbfs/fr/station_information.json")
# page = reponse.json()
# stations = page['data']['stations']

# for station in stations:
# print(station['name'] + " : " + str(int(station['capacity'])))

# EXO 3
# reponse = requests.get("https://gbfs.citibikenyc.com/gbfs/fr/station_status.json")
# page = reponse.json()
# status = page['data']['stations']
# ratio = 0
# active = 0
# Nactive =0
# for station in status:
#     if station['station_status'] == 'active':
#         ratio = ratio + 1
#         active = active + 1
#     else:
#         ratio = ratio
#         Nactive = Nactive + 1
# x =  ratio/len(status)
# print("Le ratio de station active est " + str(x))
# print("Il y a " + str(active) + " station actif")
# print("Il y a " + str(Nactive) + " station non active")

# EXO 4

# reponse = requests.get("https://gbfs.citibikenyc.com/gbfs/fr/station_status.json")
# page = reponse.json()
# status = page['data']['stations']
# bikes = 0
# Ebikes =0
# for station in status:
#     bikes = bikes + station['num_bikes_available']
#     Ebikes = Ebikes + station['num_ebikes_available']
# print(bikes)
# print(Ebikes)
# ratio = bikes + Ebikes
# rat = Ebikes/ratio
# print(rat)

# EXO 5
reponse = requests.get(
    "https://gbfs.citibikenyc.com/gbfs/fr/station_information.json")
page = reponse.json()
stations = page['data']['stations']
cords = [{'name': page['data']['stations'][0]['name'],
        'distance':math.sqrt(page['data']['stations'][0]['lon']**2 + page['data']['stations'][0]['lat']**2),
        }, 
        {'name': page['data']['stations'][1]['name'],
        'distance':math.sqrt(page['data']['stations'][1]['lon']**2 + page['data']['stations'][1]['lat']**2)}
        ]
for station in stations:
    string = str(station['name']) + " | " + "+" + \
        str(station['lat']) + " | " + str(station['lon']) + " | "
    sqr = math.sqrt(station['lat']**2 + station['lon']**2)
    if cords[0]['distance'] < sqr:
        cords[0]['name'] = station['name']
        cords[0]['distance'] = sqr
    elif cords[1]['distance'] > sqr:
        cords[1]['name'] = station['name']
        cords[1]['distance'] = sqr
        
print(cords[0])
print(cords[1])
