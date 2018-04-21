from urllib.request import Request, urlopen
import json 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

YTS_AG_API = "https://yts.am/api/v2/list_movies.json"

#Get newest Documentaries with imdb rating >= 7
#Full list of parms: https://yts.am/api
YTS_AG_PARMS = "?minimum_rating=7&sort_by=date_added&genre=Documentary"


req = Request(YTS_AG_API+YTS_AG_PARMS, headers={'User-Agent': 'Mozilla/5.0'})

with urlopen(req) as url:
    data = json.loads(url.read().decode())

print('Title'.ljust(60) + 'Year'.ljust(6) + 'Rating'.ljust(10) + 'URL')
for i in data['data']['movies']:
    print(str(i['title']).ljust(60) + str(i['year']).ljust(6) + str(i['rating']).ljust(10) + str(i['url']).ljust(4))

    