# Anthony Briones
# Homework 4
# Python File to display bar charts of Top 10, 30, and 50 words

import pandas as pd
import plotly.graph_objects as go


# Function to take csv file name and number of items to display in a barchart.
def plot_top_words(csv_file, top_n):
    # Read data from CSV file, assuming it's already sorted
    data = pd.read_csv(csv_file)

    # Extract data for the top N words
    top_n_words = data.head(top_n)
    x_data = top_n_words['frequency']
    y_data = top_n_words['word']

    # Define a color scale based on frequency
    color_scale = [
        [0, 'rgb(0, 0, 100)'],  # Blue
        [1, 'rgb(255, 0, 0)']  # Red
    ]

    # Create the bar chart with color scale
    fig = go.Figure(go.Bar(
        x=x_data,
        y=y_data,
        orientation='h',
        marker=dict(color=x_data, colorscale=color_scale)
    ))

    # Set the title for the graph
    fig.update_layout(title=f"Top {top_n} words")

    # Show the chart in the default web browser
    fig.show(renderer="browser")


# Call plot_top_words to display bar chart
plot_top_words('elonDictSorted.csv', 10)  # Top 10 words
plot_top_words('elonDictSorted.csv', 30)  # Top 30 words
plot_top_words('elonDictSorted.csv', 50)  # Top 50 words