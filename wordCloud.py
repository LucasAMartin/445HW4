# Anthony Briones
# Homework 4
# Python File to display word clouds of Top 100, 150, 200, and 250

import pandas as pd
import plotly.graph_objects as go
from wordcloud import WordCloud

# Function to take csv file name and number of items to display in a word cloud.
def generate_word_cloud(csv_file, top_n):
    # Read data from CSV file
    data = pd.read_csv(csv_file)

    # Sort data by frequency and get top N words
    top_n_words = data.nlargest(top_n, 'frequency')

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(zip(top_n_words['word'], top_n_words['frequency'])))

    # Plot the word cloud using Plotly
    fig = go.Figure(go.Image(z=wordcloud.to_array()))
    fig.update_layout(title_text=f'Top {top_n} Words')
    fig.show(renderer="browser")

# Call generate_word_cloud to display graphs
generate_word_cloud('elonDictSorted.csv', 100)
generate_word_cloud('elonDictSorted.csv', 150)
generate_word_cloud('elonDictSorted.csv', 200)
generate_word_cloud('elonDictSorted.csv', 250)