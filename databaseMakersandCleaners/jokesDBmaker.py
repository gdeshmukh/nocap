import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)


one = pd.read_csv('jokesFiles/jokes.csv')
two = pd.read_csv('jokesFiles/shortjokes.csv')

print(one.columns.values)
print(two.columns.values)

one['Joke'] = one['Question'] + ' ' + one['Answer']
print(one)
one = one.drop(columns='Question')
one = one.drop(columns='Answer')
print(one)

final = pd.concat([one, two])
final = final.reset_index(drop=True)
final = final.drop(columns='ID')
print(final)

final.to_csv('allJokes.csv')