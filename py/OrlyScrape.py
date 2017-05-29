# quick and dirty script to scrape the books from http://www.oreilly.com/programming/free/
# pip install requests
import requests
import shutil
import re

root_site_links = []

def main(url, inputUrl=""):
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
            name = cleanBook[23:]
            dlLinks = "http://www.oreilly.com/"+cleanBook
            stream = requests.get(dlLinks, stream=True)

            with open(name, 'wb') as file:
                shutil.copyfileobj(stream.raw, file)
            print "Downloaded: {0}".format(name)

main("http://www.oreilly.com/programming/free/")
