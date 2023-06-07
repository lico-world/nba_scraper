from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

import private_constants

delay = 2  # Waiting delay to avoid "Too Many Requests" error with the website

# Path were you want to export data
PATH = private_constants.path


def get_team_acronym(team, year):
    critical_acronyms = ['NOP', 'NOH', 'NOK', 'NJN', 'BRK', 'CHO', 'CHA', 'CHH', 'SEA', 'OKC']
    if team not in critical_acronyms:
        return team
    else:
        if team == 'NOP' or team == 'NOH' or team == 'NOK':
            if year < 2006 or 2007 < year < 2014:
                return 'NOH'
            elif 2005 < year < 2008:
                return 'NOK'
            else:
                return 'NOP'

        elif team == 'NJN' or team == 'BRK':
            if year < 2013:
                return 'NJN'
            else:
                return 'BRK'
        elif team == 'CHO' or team == 'CHA' or team == 'CHH':
            if year < 2003:
                return 'CHH'
            elif year > 2014:
                return 'CHO'
            elif 2001 < year < 2005:
                return 'ERROR_CHA_DONT_PLAY_THIS_YEAR'
            else:
                return 'CHA'
        elif team == 'OKC' or team == 'SEA':
            if year < 2009:
                return 'SEA'
            else:
                return 'OKC'


def call_bbr(url, wanted_stats):
    sleep(delay)
    html = urlopen(url)
    soup = BeautifulSoup(html, features="lxml")

    print(url)

    titles = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]

    indexes = []
    for s in wanted_stats:
        indexes.append(titles.index(s))

    data = soup.findAll('tr')[1:]
    rows = [[td.getText() for td in data[i].findAll('td')] for i in range(len(data))]

    result = []
    for stat in wanted_stats:
        stat_list = []
        for row in rows[1:(len(rows))]:
            if len(row) > 0:
                stat_list.append(row[titles.index(stat) - 1])

        result.append(stat_list)

    return result


def main():
    years = [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2010, 2009, 2008, 2007, 2006, 2005]
    wanted_stats = ['ORtg', '3PAr']

    with open("teams.txt", "r") as t:
        teams = t.read().splitlines()

    # --------------------------------- URL CREATION ---------------------------------

    url_list = []

    for y in years:
        for t in range(len(teams)):
            url_list.append("https://www.basketball-reference.com/teams/" +
                            str(get_team_acronym(teams[t], y)) + "/" + str(y) + "/gamelog-advanced/#tgl_advanced")

    # --------------------------------------------------------------------------------

    data = []

    for url in url_list:
        data.append(call_bbr(url, wanted_stats))

    # --------------------------------- EXCEL EXPORT ---------------------------------

    excel_file = Workbook()

    for year in range(len(years)):
        excel_file.create_sheet(str(years[year]))
        year_sheet = excel_file[str(years[year])]

        for t in range(len(teams)):
            year_sheet.cell(1, len(wanted_stats) * t + 1, teams[t])

        for sample in range(int(len(data) / len(years))):
            sample += int(len(data) * (year / len(years)))
            for h in range(len(wanted_stats)):
                year_sheet.cell(2, (h + len(wanted_stats) * sample) % int(len(wanted_stats) * len(data) / len(years)) +
                                1, wanted_stats[h])

            for column in range(len(data[sample])):
                for line in range(len(data[sample][column])):
                    year_sheet.cell(line + 3, (column + len(wanted_stats) * sample) % int(len(wanted_stats) * len(data)
                                                                                          / len(years)) + 1,
                                    float(data[sample][column][line]))

    excel_file.remove(excel_file["Sheet"])
    excel_file.save(PATH + "DATA" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".xlsx")

    # --------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
