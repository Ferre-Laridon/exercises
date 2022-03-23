import json
import sys
import urllib.request
import re

artist = sys.argv[1]
title = sys.argv[2]

def remove_space(string):
    return re.sub(" ", "%20", string)

artist = remove_space(artist)
title = remove_space(title)

url = f"https://api.lyrics.ovh/v1/{artist}/{title}"

with urllib.request.urlopen(url) as url:
    lyrics = json.loads(url.read())
    print(lyrics["lyrics"])