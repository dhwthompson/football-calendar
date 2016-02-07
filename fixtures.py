from sys import stdin

from icalendar import Calendar
import requests


FIXTURES_URL = 'http://www.cambridge-united.co.uk/generic/download-fixtures-calendar.aspx?teamID=71'


def is_home_game(fixture):
    return fixture['location'] == 'Abbey Stadium'

response = requests.get(FIXTURES_URL)

fixtures = Calendar.from_ical(response.text)
fixtures.subcomponents = filter(is_home_game, fixtures.subcomponents)

print fixtures.to_ical()
