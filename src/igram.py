import re
import requests
import sys
from lxml import html


# todo: Try threading for downloads


class Download:
    def __init__(self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        try:
            self.link = tree.xpath('//meta[@property="og:video"]/@content')[0]
        except IndexError:
            self.link = tree.xpath('//meta[@property="og:image"]/@content')[0]
        finally:
            print(self.link)
            self.fetch()

    def fetch(self):
        r = requests.get(self.link, stream=True)
        if r.status_code == 200:
            with open(str(re.sub(r'^(\w|\W)*/', '', self.link)), 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)


# Iterate over input arguments
for index in range(len(sys.argv) - 1):
    Download(sys.argv[index + 1])
