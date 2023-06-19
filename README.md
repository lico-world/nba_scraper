# nba_scraper
A python base you can work on to scrap data from basketball-reference.

Things to change :
- path          :   Where you want to save the excel file

# Using Pipenv

## Install required packages

``pipenv install``

## Running the application

``pipenv run python main.py``

# Using the App

## Select data

Update the ``config.toml`` file to customize :

- ``years`` : the list of years to retrieve data for
- ``teams`` : the list of teams you want to analyze
- ``http_delay`` : the number of seconds to wait in between each request
- ``requests.SOME_NAME`` : the request you want to execute (the ``SOME_NAME`` does not matter, as long as it's unique and not a duplicate)
    - ``url`` : the pattern of the URL to request
        - ``TEAM_TO_CHANGE`` is the location in the url where the team acronym will be written.
        - ``YEAR_TO_CHANGE`` is the location in the url where the year will be written.
    - ``stats`` : the list of stats you are interested in for this request

## Example of a valid configuration file config.toml
```toml
years = [2023, 2022]
teams = ["MIA", "BOS"]
http_delay = 1.5

[requests.basic]
url = "https://www.basketball-reference.com/teams/TEAM_TO_CHANGE/YEAR_TO_CHANGE/gamelog/#tgl_basic"
stats = [ "FG%", "TOV" ]

[requests.advanced]
url = "https://www.basketball-reference.com/teams/TEAM_TO_CHANGE/YEAR_TO_CHANGE/gamelog-advanced/#tgl_advanced"
stats = [ "ORtg", "3PAr", "Pace" ]
```
