# import requests
# import requests_html
# from bs4 import BeautifulSoup

# page = requests.get('https://bscscan.com/token/0x20512ee0052236b009772af0ed22bc58b40c27b9')

# soup = BeautifulSoup(page.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())
# table = soup.find('div', attrs = {'id':'ContentPlaceHolder1_tr_tokenHolders'})
# print(table)



from inf import env
import cfscrape
from bs4 import BeautifulSoup 
def data():
    scraper = cfscrape.CloudflareScraper() 
    r = scraper.get(f"https://bscscan.com/token/{env.token_number}").content 
    soup = BeautifulSoup(r, 'html5lib')
    table = soup.find('div', attrs = {'id':'ContentPlaceHolder1_tr_tokenHolders'}).find('div',attrs={'class':'d-flex align-items-center'}).find('div',attrs={'class':{'mr-3'}}).contents
    response = {
        'success':True,
        'data':{
            'holder_count':int(str(table[0]).lstrip('\n')[:(len(str(table[0]).lstrip('\n'))-1)].split()[0].replace(',', '')),

        }
    }#str(table[0]).lstrip('\n')
    print(response)
    return response
