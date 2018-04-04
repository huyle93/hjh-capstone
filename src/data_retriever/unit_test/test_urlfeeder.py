import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
ssl._create_default_https_context = ssl._create_unverified_context

i = 1
while True:
    try:
        if i == 0:
            url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01%2F01%2F2014&facet_to_date=01%2F01%2F2016"
        else:
            url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01/01/2014&facet_to_date=01/01/2016&search_api_fulltext=&page={}".format(i)
        
        i += 1
        html = urlopen(url)
        bsObj = BeautifulSoup(html, "html.parser")
        pdf_url = bsObj.findAll("div", {"class": "views-field views-field-field-document"})
        if len(pdf_url) == 0:
            print('nah')
            break
        print(url)
    except:
      break