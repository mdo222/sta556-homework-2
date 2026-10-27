# sta556-homework-2

Data Source: 

File: housing_market.csv

Source: https://stratumstats.com/datasets/housing-market/

Author: Stratum Stats

Description: This data is a public .csv file from Stratumstats.com. It is a housing market dataset with 1500 listings with 15 different columns related to price, size, amount of rooms, and dates. It is a free to download data set and can be downloaded through this link: https://stratumstats.com/datasets/housing-market/. 

For this analysis, download housing_market.csv and put it into your data/raw directory. 

Project Purpose:

The purpose of this project is to analyze the relationship between Listing Price and Square footage between houses (not including condos). I am also analyzing whether the home has an effect on the relationship between Listing Price and Square footage. 

How to Run the Analysis:

1. Download the housing_market.csv and the repository.
2. Use the requirements.txt file to install all necessary packages in your shell:
 python -m pip install -r requirements.txt
3. Open the notebook titled: homework_2.ipynb
4. Run all cells in order
5. If you would like to look at the datsets, those will be in the data directory.
    For figures, those will be in the figures directory.
    For information on the
    
Main Findings:

Based on the analysis, there are three main findings:

1. Listing Price from the proccesed data set is right-skewed with a mean of approximately $558,711.10 and a median of $498,690.
2. When comparing Listing Price for each condition, all conditions have outliers. These outliers are more expensive than the other listing prices for that condition. When it comes to variability, the listing prices for the homes in Good and Excellent conditions were the most variable. There is still variability in the Poor and Fair homes as well. It is important to note that the variability in listing prices could be from other factors like amount of rooms and location, though it is not for certain. When it comes to the 50th percentiles, there is an increase in listing price as the condition of them home is better (from Poor to Excellent) condition. 
3. When looking at the relationship between listing prices and square footage for homes, there is an associated strong postive linear correlation. As the amount of square footage in a home increases, there is an associated increase in listing price. This can be seen among homes with each of the different conditions. Thus, it is hard to say if condition is correlated to the relationship between listing price and square footage since the relationships in each of the scatterplots (for each condition) is very similar. 