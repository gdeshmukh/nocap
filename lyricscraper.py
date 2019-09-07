import requests
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_columns', False)
pd.set_option('display.max_rows', False)
pd.set_option('expand_frame_repr', False)

def get_lyrics(phrase, exactPhrase, decade=2010, genre=None):

    phrase.strip()
    if exactPhrase:
        phrase = '%27' + phrase + '%27'

    phrase = phrase.replace(' ', '%20')

    url = 'https://www.lyrics.com/serp.php?st=' + phrase

    if genre:
        genre = genre.replace(' ', '+')
        url = url + '&genre=' + genre
    if decade:
        decade = str(decade)
        url = url + '&dec=' + decade


    if exactPhrase:
        url = 'https://www.lyrics.com/lyrics/' + phrase



    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    songs = soup.findAll('div', attrs = {'class':'sec-lyric clearfix'})

    all = [[]]

    for item in songs:
        row = []
        song_name = item.find('p', attrs = {'class':'lyric-meta-title'}).getText()
        artist = item.find('p', attrs = {'class':'lyric-meta-artists'}).getText()
        album = item.find('p', attrs = {'class':'lyric-meta-album'}).getText()
        year = item.find('p', attrs = {'class':'lyric-meta-album-year'}).getText()
        lyrics = item.find('pre', attrs = {'class':'lyric-body'}).getText()
        #lyrics = lyrics.replace('\n',' ')
        lyrics = lyrics.replace('\r', ' ')
        lyrics = lyrics.replace('  ', ' ')
        lyrics = lyrics.replace('   ', ' ')
        lyrics = lyrics.replace('    ', ' ')
        headers = [song_name, artist, album, year, lyrics]
        for header in headers:
            row.append(header)

        all.append(row)

    df = pd.DataFrame.from_records(all, columns= ['Song Name','Artists', 'Album', 'Year', 'Lyrics']).drop(index=0).reset_index(drop=True)
    df = df.drop_duplicates(subset= 'Lyrics')
    df = df.drop_duplicates(subset= ['Song Name', 'Artists']).reset_index(drop='True')
    df = df[df['Artists'] != 'Kidz Bop Kids']

    if exactPhrase and decade:
        df = df[df['Year'] >= str(decade)]
    return(df)
