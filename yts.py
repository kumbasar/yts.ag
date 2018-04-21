from urllib.request import Request, urlopen
import json 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

YTS_AG = "https://yts.am/api/v2/list_movies.json?minimum_rating=7&sort_by=date_added&genre=Documentary"

req = Request(YTS_AG, headers={'User-Agent': 'Mozilla/5.0'})

with urlopen(req) as url:
    data = json.loads(url.read().decode())

print(data)
    