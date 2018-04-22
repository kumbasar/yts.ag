from urllib.request import Request, urlopen
import json
import ssl
import textwrap
import argparse

# 11 is the width of the first expression of print eg: 'Title    : '
WIDTH_LENGTH = 11
# Desired quality. If not found, the first torrent will be displayed.
QUALITY = '1080p'


genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
          'Documentary', 'Drama', 'Family', 'Fantasy', 'Film Noir', 'History',
          'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
          'Short', 'Sport', 'Superhero', 'Thriller', 'War', 'Western']
sort_by = ['title', 'year', 'rating', 'peers', 'seeds', 'download_count',
           'like_count', 'date_added']

parser = argparse.ArgumentParser(
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-r", "--rating", help="Minumun IMDB rating", type=float,
                    default=7)
parser.add_argument("-g", "--genre", help="Genres", type=str, choices=genres,
                    default=genres[6])
parser.add_argument("-s", "--sort", help="Sort results by", type=str,
                    choices=sort_by, default=sort_by[-1])
parser.add_argument("-l", "--limit", help="Result limit [1-50]", type=int,
                    default=10)

args = parser.parse_args()

if args.limit > 50 or args.limit < 1:
    args.limit = 1
    print("Given value is not within the boundaries. \
It is set to default value")

ssl._create_default_https_context = ssl._create_unverified_context

YTS_AG_API = "https://yts.am/api/v2/list_movies.json"

# Full list of parms: https://yts.am/api
YTS_AG_PARMS = ("?minimum_rating=" + str(args.rating) +
                "&sort_by=" + str(args.sort) + "&genre=" + str(args.genre) +
                "&limit=" + str(args.limit))

req = Request(YTS_AG_API+YTS_AG_PARMS, headers={'User-Agent': 'Mozilla/5.0'})

with urlopen(req) as url:
    data = json.loads(url.read().decode())

lineWidth = len(str(data['data']['movies'][0]['torrents'][0]['url'])) + WIDTH_LENGTH

for i in data['data']['movies']:
    print('Title    : ' + str(i['title']))
    print('Year     : ' + str(i['year']))
    print('Rating   : ' + str(i['rating']))
    print(textwrap.fill(('Summary  : ' + str(i['summary'])), width = lineWidth,
          subsequent_indent = ' ' * WIDTH_LENGTH))
    print('URL      : ' + str(i['url']))
    #Set the first as default torrent URL
    torrent_url = str(i['torrents'][0]['url'])
    torrent_quality = str(i['torrents'][0]['quality'])
    #Search for desired quality
    for torrent in i['torrents']:
        if torrent['quality'] == QUALITY:
            torrent_url = str(torrent['url'])
            torrent_quality = QUALITY
            break
    print('Torrent  : ' + torrent_url)
    print('Quality  : ' + torrent_quality)
    print('#' * lineWidth)
