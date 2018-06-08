#Also, can get names of all results using temp[i] in query2 funtion.

from bs4 import BeautifulSoup
from requests import get

def crawl(url,clas,span):
    htmlString = get(url).text
    html = BeautifulSoup(htmlString, 'lxml')
    entries = html.find_all('div', {'class': clas}, span)
    text = [e.get_text() for e in entries]
    return text


def query2(pg,kw):
    url= 'http://www.shopping.com/products~PG-'+str(pg)+'?KW='+str(kw)
    temp=crawl(url,"gridItemBtm","span")
    return"Total no of results for Keyword: "+str(kw)+" on page: "+ str(pg)+" are: "+str(len(temp)) 
