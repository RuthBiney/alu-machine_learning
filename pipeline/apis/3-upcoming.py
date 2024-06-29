#!/usr/bin/env python3
'''
Script that displays the upcoming launch
'''

import requests
import datetime

def get_upcoming_launch():
    '''
    Prints upcoming SpaceX launch

    Output info:
    - Name of the launch
    - The date (in local time)
    - The rocket name
    - The name (with the locality) of the launchpad
    '''

    url = 'https://api.spacexdata.com/v4/launches/upcoming'
    try:
        response = requests.get(url)
        response.raise_for_status()
        launches = response.json()

        # Sort launches by date_unix and get the upcoming launch
        upcoming_launch = sorted(launches, key=lambda x: x['date_unix'])[0]

        # Fetch rocket details
        rocket_id = upcoming_launch['rocket']
        rocket_url = f'https://api.spacexdata.com/v4/rockets/{rocket_id}'
        rocket_response = requests.get(rocket_url)
        rocket_response.raise_for_status()
        rocket = rocket_response.json()
        rocket_name = rocket['name']

        # Fetch launchpad details
        launchpad_id = upcoming_launch['launchpad']
        launchpad_url = f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}'
        launchpad_response = requests.get(launchpad_url)
        launchpad_response.raise_for_status()
        launchpad = launchpad_response.json()
        launchpad_name = launchpad['name']
        launchpad_locality = launchpad['locality']

        # Format the date in local time
        date_local = upcoming_launch['date_local']
        formatted_date_local = datetime.datetime.fromisoformat(date_local).strftime('%Y-%m-%d %H:%M:%S')

        # Print the details
        print(f"{upcoming_launch['name']} ({formatted_date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})")

    except requests.RequestException as e:
        print(f'An error occurred while making an API request: {e}')
    except Exception as err:
        print(f'A general error occurred: {err}')

if __name__ == '__main__':
    get_upcoming_launch()
