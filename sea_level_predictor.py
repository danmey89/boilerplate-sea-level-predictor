import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', label='original data')

    # Create first line of best fit
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    year1 = np.arange(1880, 2051)
    plt.plot(year1, res1.intercept + res1.slope * year1, 'r', label='first line of best fit')
    # Create second line of best fit
    res2 = linregress(df[df['Year']>=2000]['Year'], df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    year2 = np.arange(2000, 2051)
    plt.plot(year2, res2.intercept + res2.slope * year2, 'r', label='first line of best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()