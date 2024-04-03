import requests
from bs4 import BeautifulSoup
import signal
import threading
import argparse


pages = []
try:
    request = build_request("http://kb.dynamsoft.com/sitemap.xml")
    f = urlopen(request, timeout=3)
    xml = f.read()
    soup = BeautifulSoup(xml)
    urlTags = soup.find_all("url")

    print("The number of url tags in sitemap: ", str(len(urlTags)))

    for sitemap in urlTags:
        link = sitemap.findNext("loc").text
        pages.append(link)
    f.close()
    
except HTTPError, URLError:
    print URLError.code

return pages