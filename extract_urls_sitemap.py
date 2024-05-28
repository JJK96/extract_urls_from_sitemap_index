import requests
from bs4 import BeautifulSoup

def extract_urls_from_sitemap(url_sitemap):
    sitemap = []
    urls = []
    sitemap_crawled = []
    xml = requests.get(url_sitemap, verify=False, headers={"Accept-Language": "en-US,en;q=0.5"})
    xml_parsed = BeautifulSoup(xml.content, "xml")
    if xml_parsed.find_all("sitemap"):
        sitemaps = xml_parsed.find_all("loc")
        for s in sitemaps:
            sitemap.append(s.text)
        for s in sitemap:
            urls1, sitemap_crawled1 = extract_urls_from_sitemap(s)
            urls += urls1
            sitemap_crawled += sitemap_crawled1
    else:
        url = xml_parsed.find_all("loc")
        for u in url:
            urls.append(u.text)
            sitemap_crawled.append(url_sitemap)
    return urls, sitemap_crawled


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()

urls,sitemap_crawled = extract_urls_from_sitemap(args.url)

for url in urls:
    print(url)
