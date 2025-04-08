import pandas as pd
df = pd.read_excel('C:\\Users\\RickE\\Downloads\\movies.xls')
grouped_data =  df.groupby('Year')['IMDB Score'].agg(['mean', 'count'])
filtered_data =  grouped_data[grouped_data['count']>5]
ordered_data = filtered_data.sort_values('count', ascending=False)
print(ordered_data)