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

for i in data['data']['movies']:
    print('Title:   ' + str(i['title']))
    print('Year:    ' + str(i['year']))
    print('Rating:  ' + str(i['rating']))
    print('Summary: ' + str(i['summary']))
    print('URL:     ' + str(i['url']))
    print('Torrent: ' + str(i['torrents'][0]['url']))
    print('###############################################')

    