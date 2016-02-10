from sys import stdin

from flask import Flask
from icalendar import Calendar
import requests


FIXTURES_URL = 'http://www.cambridge-united.co.uk/generic/download-fixtures-calendar.aspx?teamID=71'


def is_home_game(fixture):
    return fixture['location'] == 'Abbey Stadium'


app = Flask(__name__)


@app.route('/')
def get_fixtures():
    response = requests.get(FIXTURES_URL)

    fixtures = Calendar.from_ical(response.text)
    fixtures.subcomponents = filter(is_home_game, fixtures.subcomponents)
    response = fixtures.to_ical()
    status = 200
    headers = {'Content-Type': 'text/calendar'}
    return (response, status, headers)
