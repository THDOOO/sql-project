import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('C:\\Users\\RickE\\Downloads\\movies.xls')
genres_list = df['Genres'].str.split('|').explode()

# Count the occurrences of each genre
genre_counts = genres_list.value_counts()

# Get the top 5 and bottom 5 genres
top_5_genres = genre_counts.head(5)
bottom_5_genres = genre_counts.tail(5)

print("Top 5 most common genres:")
print(top_5_genres)

print("\nFlop 5 least common genres:")
print(bottom_5_genres)