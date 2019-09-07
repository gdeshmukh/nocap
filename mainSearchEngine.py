import pandas as pd
from lyricscraper import get_lyrics
from movietvshowscrapper import get_movie_tv
from imageTagger import get_image_tags

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

def search_by_phrase(phrase, number_of_each, decade=2010):

    jokes = pd.read_csv('databases/allCleanedJokes.csv')
    jokes = jokes[jokes['Joke'].str.contains(phrase)]
    jokes = jokes.drop_duplicates(subset= 'Joke')

    jokes = jokes.head(number_of_each)
    quotes = pd.read_csv('databases/allQuotes.csv')
    quotes = quotes[quotes['Quote'].str.contains(phrase)]
    quotes = quotes.drop_duplicates(subset= 'Quote')
    quotes = quotes.head(number_of_each)

    lyrics = get_lyrics(phrase, True, decade)
    lyrics = lyrics.head(number_of_each)

    moviesTV = get_movie_tv(phrase, decade)
    moviesTV = moviesTV.head(number_of_each)

    results = [lyrics, jokes, quotes, moviesTV]

    captions = []

    lyrics['final'] = lyrics['Lyrics'] + ' --- ' + (lyrics['Artists'])
    quotes['final'] = quotes['Quote'] + ' --- ' + quotes['Author']
    moviesTV['final'] = moviesTV['Quotes'] + ' --- ' + moviesTV['Title']

    for item in lyrics['final']:
        captions.append(item)
    for item in quotes['final']:
        captions.append(item)
    for item in moviesTV['final']:
        captions.append(item)
    for item in jokes['Joke']:
        captions.append(item)

    for caption in captions:
        print(caption)
        print('--------------------------------------')


def search_by_image(image_path, number_of_each, decade=2010):

    phrase = get_image_tags(image_path)[0]
    search_by_phrase(phrase, number_of_each, decade)


if __name__ == '__main__':
    image_path = 'taggingImages/beach.png'
    search_by_image(image_path, 3)




