#!/usr/bin/env python3
"""
This module retrieves information about the upcoming SpaceX launch.
"""
import requests
from datetime import datetime, timezone


def sentientPlanets():
    """
    Retrieves information about the upcoming SpaceX launch.
    """
    try:
        species_response = requests.get('https://api.spacexdata.com/v4/launches/upcoming')
        if species_response.status_code == 200:
            upcoming_launches = species_response.json()
            next_launch = sorted(upcoming_launches, key=lambda x: x['date_unix'])[0]

            launch_name = next_launch['name']
            launch_date_utc = datetime.fromtimestamp(next_launch['date_unix'], timezone.utc)
            launch_date_local = launch_date_utc.astimezone().strftime('%Y-%m-%d %H:%M:%S')
            
            launchpad_id = next_launch['launchpad']
            launchpad_details = requests.get(f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}')
            launchpad_data = launchpad_details.json()
            launchpad_name = launchpad_data.get('name', 'Unknown launchpad')
            launchpad_location = launchpad_data.get('locality', 'Unknown locality')

            rocket_details = requests.get(f'https://api.spacexdata.com/v4/rockets/{rocket_id}')
            rocket_name = rocket_details.json().get('name', 'Unknown rocket')
            rocket_id = next_launch['rocket']



            print(f'{launch_name} ({launch_date_local}) {rocket_name} - {launchpad_name} ({launchpad_location})')
        else:
            print(f'Error: {species_response.status_code}')
    except requests.exceptions.RequestException as error:
        print(f'Request failed: {error}')

if __name__ == '__main__':
    sentientPlanets()
