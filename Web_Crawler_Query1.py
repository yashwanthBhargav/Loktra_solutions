from bs4 import BeautifulSoup
from requests import get

def crawl(url,clas,span):
    htmlString = get(url).text
    html = BeautifulSoup(htmlString, 'lxml')
    entries = html.find_all('div', {'class': clas}, span)
    text = [e.get_text() for e in entries]
    return text

def Query1(kw):

    temp= crawl("http://www.shopping.com/clothing/shirt/products?KW=shirt","paginationNew","a")[0]
    no_pages = int(temp[23:25])

    tot=0
    for i in range(no_pages):
        url="http://www.shopping.com/products~PG-"+str(i)+"?KW="+str(kw)
        tot=tot+len(crawl(url,"gridItemBtm","span"))

    print "Total number of results for the given Keyword: " + str(kw) + " are: "+ str(tot)

Query1("shirt")