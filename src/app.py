import re
import requests
import sys
from lxml import html

page = requests.get(sys.argv[1])
tree = html.fromstring(page.content)

link = tree.xpath('//meta[@property="og:image"]/@content')

print(link[0])

r = requests.get(link[0], stream=True)
if r.status_code == 200:
    with open(str(re.sub(r'^(\w|\W)*/', '', link[0])), 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
