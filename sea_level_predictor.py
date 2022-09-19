import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # draw the scatter plot with the Year as x, and the sea level as y
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit extended to 2050
    lr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    future_years = pd.Series(np.arange(df['Year'].max()+1, 2051))
    x = pd.concat([df['Year'], future_years], ignore_index=True)
    ax.plot(x, lr.slope * x + lr.intercept)

    # create a copy of the datframe with just the data from 2000 on
    df2 = df[df['Year'] >= 2000]

    # Create second line of best fit from 2000 to 2050
    lr2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x2 = pd.concat([df2['Year'], future_years], ignore_index=True)
    ax.plot(x2, lr2.slope * x2 + lr2.intercept)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
