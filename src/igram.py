from lxml import html
import json
import re
import requests
import sys
import threading


class Download(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        page = requests.get(url)
        self.tree = html.fromstring(page.content)
        self.shared_data = json.loads(self.tree.xpath('//script/text()')[1][21:-1])

    def run(self):
        try:
            media_array = \
                self.shared_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children'][
                    'edges']

            for resource_link in media_array:
                try:
                    link = resource_link['node']['video_url']
                except KeyError:
                    link = resource_link['node']['display_url']
                finally:
                    print(link)
                    self.fetch(link)

        except KeyError:
            try:
                link = self.tree.xpath('//meta[@property="og:video"]/@content')[0]
            except IndexError:
                link = self.tree.xpath('//meta[@property="og:image"]/@content')[0]
            finally:
                # noinspection PyUnboundLocalVariable
                print(link)
                self.fetch(link)

    @staticmethod
    def fetch(link):
        r = requests.get(link, stream=True)
        if r.status_code == 200:
            with open(str(re.sub(r'^(\w|\W)*/', '', link)), 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)


# Iterate over input arguments
for index in range(len(sys.argv) - 1):
    Download(sys.argv[index + 1]).start()
