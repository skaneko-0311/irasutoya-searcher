import requests
class MyCrawler:
    def __init__(self):
        pass
    @classmethod
    def fetchHtml(cls, url):
        return requests.get(url).text