import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)


one = pd.read_json('quoteFiles/quotes.json')

print(one)

one = one.drop(columns='Popularity')

two  = pd.read_csv('quoteFiles/Quotes.csv', sep= ';')
two['Tags'] = None


two = two.rename(columns = {'QUOTE' : 'Quote', 'AUTHOR' : 'Author', 'GENRE': 'Category'})


three  = pd.read_csv('quoteFiles/quotesone.csv', sep=',')



three['Tags'] = None
three['Category'] = None



print('one')
print(one.columns.values)

print('two')
print(two.columns.values)

print('three')
print(three.columns.values)

frames = [one, two, three]
final = pd.concat(frames)
print(final)

final = final.sort_values(by = ['Author'])
final = final.reset_index(drop=True)

print(final)
final.to_csv('allQuotes.csv')