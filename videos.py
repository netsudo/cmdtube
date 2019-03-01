import requests
from lxml import html as lx


class Videos:
    def __init__(self, search):
        self.search = search
        self.search_url = 'https://www.youtube.com/results?search_query={}'.format(self.search)
        self.videos = self.__search_results()

    def list_videos(self):
        for i, video in self.videos.items():
            print("{}. {}".format(i, video[0]))

    def __search_results(self):
        r = requests.get(self.search_url)
        tree = lx.fromstring(r.text)
        elems = tree.xpath(".//a[contains\
                    (@class, 'yt-uix-tile-link')]")
        results = {}

        count = 1
        for i in elems:
            title = i.get('title')
            # Strip off /watch?v=
            url = i.get('href')[9:]

            results[count] = [title, url]
            count += 1

        return results
