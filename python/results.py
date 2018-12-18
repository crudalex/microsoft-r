import re
import tempfile
import webbrowser

import pandas as pd
import requests
from bs4 import BeautifulSoup


def browser_render(html):

    if isinstance(html, str):
        html = html.encode()

    f = tempfile.NamedTemporaryFile(suffix=".html", delete=False)
    f.write(html)
    f.flush()

    webbrowser.open(f.name)


def parse_with_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.select('#results > div:nth-of-type(6) > table').pop()

    # for each table rows
    for r in table.select('tbody > tr'):

        # remove nested table at 10th column "Running Position"
        cell = r.select_one('td:nth-of-type(10)')
        for t in cell.find_all(['table', 'tr', 'tbody', 'td']):
            t.unwrap()

        # remove horse name from at 3rd column "Horse"
        cell = r.select_one('td:nth-of-type(3)')
        href = cell.a['href']
        horseno = re.search('horseno=(\w+)', href).group(1)
        cell.clear()
        cell.append(horseno)

        # remove horse name from at 4th column "Jockey"
        cell = r.select_one('td:nth-of-type(4)')
        href = cell.a['href']
        jockeycode = re.search('jockeycode=(\w+)', href).group(1)
        cell.clear()
        cell.append(jockeycode)

        # remove horse name from at 5th column "Trainer"
        cell = r.select_one('td:nth-of-type(5)')
        href = cell.a['href']
        trainercode = re.search('trainercode=(\w+)', href).group(1)
        cell.clear()
        cell.append(trainercode)

    # remove thead and tbody
    table.select_one('thead').unwrap()
    table.select_one('tbody').unwrap()

    return str(table.prettify())


if __name__ == '__main__':
    url = 'http://racing.hkjc.com/racing/Info/meeting/Results/English/Local/20180701/ST/1'
    r = requests.get(url)

    content = r.content
    table = parse_with_soup(content)

    result = pd.read_html(table, header=0).pop()
    result.dropna()
    result.columns = ['place', 'horse_no', 'horse_id', 'jockey_id', 'trainer_id', 'carried_wt', 'declared_wt',
                      'barrier',
                      'lbw', 'running_position', 'finish_time', 'win_odds']

    browser_render(result.to_html())
