import requests
from bs4 import BeautifulSoup

url_dataframe = {}

root_url = 'http://www.helloworldstudio.org'

def get_urls(url):
    if url not in url_dataframe:
        print("running")
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        
        urls = []
    
        for link in soup.find_all('a'):
            new_link = link.get('href')
            if new_link:
                if new_link[0] == '/':
                    new_link = root_url + link.get('href')
                    urls.append(new_link)
                elif new_link.startswith('http://www.helloworldstudio.org/'):
                    urls.append(new_link)
    
        url_dataframe[url] = urls
    
        for url in urls:
            get_urls(url)
    

get_urls('http://www.helloworldstudio.org/')