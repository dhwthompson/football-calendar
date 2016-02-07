from sys import stdin
from icalendar import Calendar


def is_home_game(fixture):
    return fixture['location'] == 'Abbey Stadium'


fixtures = Calendar.from_ical(stdin.read())
fixtures.subcomponents = filter(is_home_game, fixtures.subcomponents)

print fixtures.to_ical()
