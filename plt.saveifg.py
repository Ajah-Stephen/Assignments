# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:42:29 2023

@author: Ajah Stephen Chidi
"""

"""
DATASET SUMMARY
The dataset demostrate crime statistics of numerous crime and their illegal act in Bangladesh,
a populated country densely in Asia acros period of years, from the 2010-2019.

To understand the visualization and make insights, 3 types of visualization will be introduced.

Line plot: The characteristics of line plot is to display data points over a priod of time, for
this reason a crime case will be displayed for each crime case over the years.

Pie chart: pie chart shows and displays group of element in relative proportion to one another,
this will help show propotion of crime in relation to each other.

Bar chart: bar chart help us to check and compare the different data point. it employed and
show the total crime case across the years.



# Link to Dataset: https://www.kaggle.com/datasets/firozkabir1/crime-statistics-of-bangladesh-2010-2019/   
  

# Importing Python libraries for exploration and visualization

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Reading data file
illegal_act = pd.read_csv("Crime Statistics Of Bangladesh 2010-2019.csv")
print(illegal_act)

# Showing total dimention of the dataset
print(illegal_act.shape)

# Showing the general information of the dataset
print(illegal_act.info())

# Checking for missing values in the dataset
print(illegal_act.isna().sum())

# Showing the columns needed our visualization 
illegal_act = illegal_act[['Year', 'Woman & Child Repression', 'Theft', 'Explosive', 'Smuggling']]
print(illegal_act)

# Agregating the columns to get the Illegal Act cases in a year
illegal_act = illegal_act.groupby("Year").sum()
print(illegal_act)

# Declare function to plot Illegal Act cases 
def plot_line(variable_x, variable_y, xlabel, ylabel, xlim, title, color='', label=''):
    """
    Create a function that plots a line graph for the illegal cases

    Args:
        variable_x : List of values for the x-axis.
        variable_y : List of values for the y-axis.
        color : The color of the line plotted.
        label : Label for the plotted line.
        xlabel: Label for the x-axis.
        ylabel: Label for the y-axis.
        xlim : Set to True to set the x-axis limits.
        title : Title of the graph plotted.
        
        return
    """
    
    # plot graph and asign color and legend

    plt.plot(variable_x, variable_y, color=color, label=label)

    # Setting labels, limits and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xlim:
        plt.xlim(min(variable_x), max(variable_x))
    plt.title(title)
        
    # Showing the legend
    plt.legend()
        
    # Saving the plotted line plot
    plt.savefig('plot_line.png')
    
# Plotting lineplot for Theft vs Year
plot_line(illegal_act.index, illegal_act['Theft'], 'Year', 'No of Theft Cases',
          True, 'Crime Statistics Of Bangladesh 2010-2019', 'blue',
          'Theft')

# Plotting lineplot for Smuggling Vs Year
plot_line(illegal_act.index, illegal_act['Smuggling'], 'Year', 'No of Smuggling Cases',
          True, 'Crime Statistics Of Bangladesh 2010-2019', 'r',
          'Smuggling')

# Plotting lineplot for Explosive Vs Year
plot_line(illegal_act.index, illegal_act['Explosive'], 'Year', 'No of Explosive Cases',
          True, 'Crime Statistics Of Bangladesh 2010-2019', 'g',
          'Explosive')

# Plotting lineplot for Woman & Child Repression
plot_line(illegal_act.index, illegal_act['Woman & Child Repression'], 'Year', 'No of Woman & Child Repression Cases',
          True, 'Crime Statistics Of Bangladesh 2010-2019', 'y',
          ' Woman & Child Repression')


# Showing the Plot
plt.show()
"""
LINE PLOT INTERPRETATION
The provision of this graph gives more understanding for 4 illegail act: Theft, Smuggling, Explosive,
Woman & Child Repression and their total reported cases in Bangladesh for 2010 to 2019.
It observeed from the graph that theft occurances relatively start from 2010 and following degreasing. 
Smuggling degrease form 2010 to 2011 and slighly increase in 2012 and drop again in 2016 and the following years.
Explosive appeared to be steady but slightly increase in 2013 and 2018.
The Woman & Child Repression appeared to be fluctuating yearly, Hence there is increase in the year 2011 and 
followed by degrease in 2013 and increase again in 2014 to 15 before declining.   

All the 4 Illegal Act reduced in the year 2019
"""



# Calculate the Illegal_Act cases
illegal_act_total = np.sum(illegal_act, axis = 0)
print(illegal_act_total)

# Create data for Illegal Act for each cases
illegal_act_cases = ["Theft", "Eplosive", "Smoggling", "Woman & Child Repression"]
total_occurances = [66361, 5190, 53200, 175101]



# Declare function to plot Illegal Act cases 
def pie_chat(variable, variable_label, lable = '', title = '', **others):
    """
    Create function to plot a pie chart
    
    Args:
    variable: the values to be plotted on the pie chart.
    variable_label: the names corresponding to the values plotted
    title: the title of the pie chart.
    **others: other arguments to pass into the pie plot function as need be 
    
    return
    """
    # Create a graph figure size
    plt.figure(figsize =(10, 6))
    
    # plot pie chat
    plt.pie(variable, labels = variable_label, **others)
    
    
    # Set legend and tittle plot
    plt.legend(variable_label)
    plt.title(title)
    
    # Save the plotteded bar chart
    plt.savefig("plot_pie.png")
    plt.show()
    
# plot the pie chat
pie_chat(total_occurances, illegal_act_cases, title = 'Crime Statistics Of Bangladesh 2010-2019',
             autopct= '%2.1f%%', explode = [0,0.1,0,0.], shadow=True)

# Calculate the total occurances in a year
yearly_occurances = np.sum(illegal_act, axis = 1)
print(yearly_occurances)

# Total data for yearly occurances
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019] 
illegal_act_year = [32897, 36183, 36412, 34927, 36259, 34935, 29723, 28867, 27625, 2024]

"""
THE PIE CHART INTERPRETATION 
It is concluded that all the 4 illegal acts were recorded and show Woman & Child Repression
as the with 58.4%, followed by Theft with 22.1%, followed by Smuggling 17.1% and next is 
Explosive with 1.7% of illegal act.
"""


# Defined function for a plot of graph selected as Illegal Act cases yearly
def bar_chart(x_variable, y_variable, xlabel, ylabel, title, xticks = None, **others):
    """
    Create function to plot a bar chart
    
    Args:
    x_variable: the label to be plotted on x-axis.
    y_variable: the values of the data to be plotted
    xlabel: the name of the the x-axis
    ylabel: the name of the the y-axis
    title: title for the bar chart.
    **others: other arguments to pass into the pie plot function as need be
    return: None
    """
    # Declare bar chart figure size
    plt.figure(figsize = (10,6))
    
    # Plote bar chart
    plt.bar(x_variable, y_variable, **others)
    
    # Set xlabel, ylabel and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    # Set the xtick label
    if xticks:
        plt.xticks(x_variable)
        
    # Save graph plot as a png file   
    plt.savefig('plot_bar.png')
    
    # Display the bar chart
    plt.show()
    
# Bar char plotting 
bar_chart(year, yearly_occurances, 'Year', 'No of occurances',
          'Crime Satistics Of Bangladesh 2010-2019', True, color = 'red')

"""

THE BAR CHART INTERPRETATION
It is observed that bar chart started increasing from the first year 2010 to 2012 and 
reduced 2013 and pick up again to 2014 before declining to 2019 as the lowest.

# Plot style selection 
plt.style.use("ggplot")


    
    
    
    



    