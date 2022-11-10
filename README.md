# Analysis of apex legends player statistic database constructed using Selenium, SQLite3, and the apexlegendsapi.com API.

The webscraping portion of this project is for demonstration purposes only. Please open an issue if you would like to request data
for your own analysis.

# Project Description
web_scrape.py: The webscraper grabs player platform and UID from apexlegendsstatus.com website. The website has a page that upon refresh will produce a random players in-game profile name and UID. These platform and UID are used to create a dictionary which key value pairs are used to query player statistics from the API. A pandas dataframe is then constructed to store the player statistic data and this dataframe is sent to a local SQLite database. 

eda.ipynb: Queries local SQL database, cleans dataframe, and runs basic univariate/bivariate analysis on relevant player statistics. 

cluster_ml.ipynb: Utlizes several clustering methods to attempt to identify 'true' ranks between players based off player eliminations and player level. Then employs various classification methods for the prediction of player rank and cluster based off player statistics. 




