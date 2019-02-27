import requests
import html


class Videos:
    def __init__(self, search):
        self.search = search
        self.key = self.__api_key()
        self.search_url = 'https://www.googleapis.com/youtube/v3/search?key={}&part=snippet&maxResults=25&q={}&type=video'.format(self.key, self.search)
        self.videos = self.__search_results()

    def list_videos(self):
        for i, video in self.videos.items():
            print("{}. {}".format(i, video[0]))

    def __search_results(self):
        r = requests.get(self.search_url)
        full_results = r.json()["items"]
        results = {}

        count = 1
        for i in full_results:
            title = html.unescape(i["snippet"]["title"])
            url = 'https://www.youtube.com/watch?v='\
                + i["id"]["videoId"]

            results[count] = [title, url]
            count += 1

        return results

    def __api_key(self):
        f = open('env.key')
        key = f.readline()
        f.close()

        return key.strip()
