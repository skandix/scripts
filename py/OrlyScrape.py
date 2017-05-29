# quick and dirty script to scrape the books from http://www.oreilly.com/programming/free/
import requests
import wget
import re

root_site_links = []

def main(url):
    resp = requests.get(url).text

    root_regex = re.compile(ur'href=\"http:\/\/www.oreilly.com\/programming\/free\/\w{3,}.+.csp')
    loot = re.findall(root_regex, resp)
    for pathway in loot:
        clean_root = pathway.replace('href="','')
        root_site_links.append(clean_root)

    next_site = requests.get
    next_site_regex = re.compile(ur'<!-- path_info: csp//programming/free/\w{3,}.+.csp')
    for links in root_site_links:
        sauce = next_site(links).text
        nextLoot = re.findall(next_site_regex,sauce)
        for books in nextLoot:
            cleanBook = "files"+books.replace('<!-- path_info: csp/','').replace('.csp','.pdf')
            
            dlLinks = "http://www.oreilly.com/"+cleanBook
            download = wget.download(dlLinks)
            print "\t"+download

main("http://www.oreilly.com/programming/free/")
