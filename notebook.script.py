import pandas as pd

# Load the dataset
netflix_df = pd.read_csv("netflix_data.csv")

# Filter for movies released in the 1990s (1990–1999)
movies_1990s = netflix_df[
    (netflix_df["type"] == "Movie") & 
    (netflix_df["release_year"] >= 1990) & 
    (netflix_df["release_year"] <= 1999)
]

# Task 1: Find the most frequent movie duration in the 1990s
duration = int(movies_1990s["duration"].mode()[0])

# Task 2: Count short Action movies (< 90 minutes) released in the 1990s
short_action_movies = movies_1990s[
    (movies_1990s["genre"] == "Action") & 
    (movies_1990s["duration"] < 90)
]
short_movie_count = int(len(short_action_movies))

# Print results to verify
print("Most frequent duration:", duration)
print("Short action movie count:", short_movie_count)
