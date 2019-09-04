import lxml.html

class MyScraper:
    def __init__(self):
        pass
    @classmethod
    def scrapeHtml(cls, html):
        return lxml.html.fromstring(html)
    @classmethod
    def extractNode(cls, dom, xpath):
        return dom.xpath(xpath)