import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

pd.set_option('display.max_columns', False)
pd.set_option('display.max_rows', False)
pd.set_option('expand_frame_repr', False)

def get_movie_tv(phrase, decade = 0, type = 0):
    searchTerm = phrase
    searchTerm.replace(" ", "%20")
    url = 'https://www.imdb.com/search/title-text/?quotes=' + searchTerm + '&ref_=fn_qu'
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    title = []
    episode = []
    year = []
    quotes = []
    links = []
    results = soup.findAll('div', attrs = {'class':'lister-item-content'})
    for item in results:
        title.append(item.find('h3', attrs = {'class':'lister-item-header'}).find('a').getText().strip())
        placeholder = item.find('h3', attrs = {'class':'lister-item-header'}).find('span', attrs={'class':'lister-item-year text-muted unbold'}).getText()
        placeholder = re.match(r"^[^\d]*(\d+)", placeholder)
        item.find('h3', attrs={'class': 'lister-item-header'}).find('a').extract()
        try:
            episode.append(item.find('h3', attrs={'class': 'lister-item-header'}).find('a').getText().strip())
            item.find('h3', attrs={'class':'lister-item-header'}).find('span', attrs = {'lister-item-year text-muted unbold'}).extract()
        except:
            episode.append("N/A")
        try:
            tempyear = re.match(r"^[^\d]*(\d+)", item.find('h3', attrs = {'class':'lister-item-header'}).find('span', attrs={'lister-item-year text-muted unbold'}).getText())
            year.append(int(tempyear.group(1)))
        except:
            year.append(int(placeholder.group(1)))
        item.find('h3').extract()
        item.find('p').extract()
        try:
            item.find('div').extract()
        except:
            pass
        item.find('h4').extract()
        links.append("https://imdb.com" + item.find('a').get('href'))
        item.find('a').extract()
        quotes.append(item.getText().strip().replace("  ", "").replace('\n\n', "\n"))
    d = {'Title': title, 'Episode': episode, 'Year': year, 'Quotes': quotes, 'Links': links}
    movieQuotes = pd.DataFrame(d, columns=['Title', 'Episode', 'Year', 'Quotes', 'Links'])
    if decade != 0:
        movieQuotes = movieQuotes.loc[(movieQuotes.Year >= decade) & (movieQuotes.Year < decade + 10)]
    if type != 0:
        if type == 1:
            movieQuotes = movieQuotes.loc[movieQuotes.Episode == "N/A"]
        if type == 2:
            movieQuotes = movieQuotes.loc[movieQuotes.Episode != "N/A"]
    return movieQuotes


