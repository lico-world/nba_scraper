# nba_scraper
A python base you can work on to scrap data from basketball-reference.

Things to change :

    - path          :   Were yo want to save the excel file
    - delay         :   The delay before any request (to avoid the "Too Many Requests" error)
    - wanted_stats  :   All the stats you want to scrap
    - years         :   What years you want to scrap
    - teams.txt     :   What teams you want to scrap

# Using Pipenv

## Install required packages

``pipenv install``

## Running the application

``pipenv run python main.py``

# Using the App

## Select data

    - In the teams.txt file, you can write all the teams you want to analyze, one team per line.
    
    - In the urls.txt file, you can enter the pattern for each url you want to request.
        > "TEAM_TO_CHANGE" is the location in the url where the team acronym will be written.
        > "YEAR_TO_CHANGE" is the location in the url where the year will be written.

    - In the stats.txt file, each line consists of all the statistics to be retrieved from the url of the corresponding line in urls.txt, each stat separated by ':'.
