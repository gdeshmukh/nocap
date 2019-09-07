import pandas as pd

pd.set_option('display.max_columns', False)
pd.set_option('display.max_rows', False)
pd.set_option('expand_frame_repr', False)

def remove_phrase(phrase):
    jokes = pd.read_csv('databases/allCleanedJokes.csv')
    blacklist_rows = []
    for i, joke in enumerate(jokes['Joke']):
        if phrase.lower() in joke.lower() and 'marshawn' not in joke.lower():
            blacklist_rows.append(i)
            print(joke)

    for num in blacklist_rows:
        jokes = jokes.drop(index=num)
    jokes = jokes.drop([jokes.columns[0]], axis='columns')
    jokes.to_csv('databases/allCleanedJokes.csv')

remove_phrase('')