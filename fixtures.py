from os import environ
from sys import stdin

from flask import Flask
from icalendar import Calendar
import requests

FIXTURES_URL = environ['FIXTURES_URL']
HOME_LOCATION = environ['HOME_LOCATION']


def is_home_game(fixture):
    return fixture.get('location') == HOME_LOCATION


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
