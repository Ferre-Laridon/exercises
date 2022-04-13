from PIL import Image
import urllib.request
import json
import sys

def get_data(n):
    if n:
        url = f'https://xkcd.com/{n}/info.0.json'
    else:
        url = f'https://xkcd.com/info.0.json'

    with urllib.request.urlopen(url) as pagina:
        data = pagina.read().decode('utf-8')
    
    return json.loads(data)

def get_image(url):
    with urllib.request.urlopen(url) as pagina:
        return Image.open(pagina)

data = get_data(None if len(sys.argv) == 1 else int(sys.argv[1]))

for key, value in data.items():
    print(f'{key}: {value}')

get_image(data['img']).show()