import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('C:\\Users\\RickE\\Downloads\\movies.xls')

high_rated_movies = df.loc[df['Year'] > 1000, ['Title', 'IMDB Score']]
print(df.columns)                 
print(high_rated_movies)