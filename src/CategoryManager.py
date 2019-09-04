import os
from crawler.MyCrawler import MyCrawler
from scraper.MyScraper import MyScraper
from storager.CategoryStorager import CategoryStorager


def main():
    html = MyCrawler.fetchHtml("https://www.irasutoya.com/")
    dom = MyScraper.scrapeHtml(html)
    nodes = MyScraper.extractNode(dom, "//*[@id='Label1']/div/ul/li/a")
    labels, links = createLists(nodes)
    store(labels, links)

def createLists(nodes):
    labels = []
    links = []
    for node in nodes:
        labels.append(node.text)
        links.append(node.attrib["href"])
    return labels, links

def store(labels, links):
    ctgstr = CategoryStorager()
    ctgstr.connect()
    ctgstr.insert(labels, links)
    ctgstr.disconnect()


if __name__ == "__main__":
    main()
