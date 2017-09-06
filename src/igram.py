from lxml import html
import json
import re
import requests
import sys


# todo: Try threading for downloads


class Download:
    def __init__(self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        shared_data = json.loads(tree.xpath('//script/text()')[1][21:-1])
        try:
            media_array = \
                shared_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children'][
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
                link = tree.xpath('//meta[@property="og:video"]/@content')[0]
            except IndexError:
                link = tree.xpath('//meta[@property="og:image"]/@content')[0]
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
    Download(sys.argv[index + 1])
