import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7)

    # Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Extend line to 2050
    years_extended = range(1880, 2051)
    line1 = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, line1, 'r', label='Linha de melhor ajuste (1880-2013)')

    # Create second line of best fit (data from 2000 onwards)
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    # Extend line to 2050
    years_2000_extended = range(2000, 2051)
    line2 = [slope2 * year + intercept2 for year in years_2000_extended]
    plt.plot(years_2000_extended, line2, 'g', label='Linha de melhor ajuste (2000-2013)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()