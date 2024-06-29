#!/usr/bin/env python3
'''
Launch frequency
'''


import requests
from collections import defaultdict


def get_launches_per_rocket():
    '''
    Displays the number of launches per rocket
    '''
    launches_url = 'https://api.spacexdata.com/v4/launches'
    rockets_url = 'https://api.spacexdata.com/v4/rockets'

    try:
        # Fetch all launches
        launches_response = requests.get(launches_url)
        launches_response.raise_for_status()
        launches = launches_response.json()

        # Count launches per rocket
        launch_count = defaultdict(int)
        for launch in launches:
            rocket_id = launch['rocket']
            launch_count[rocket_id] += 1

        # Fetch rocket details
        rockets_response = requests.get(rockets_url)
        rockets_response.raise_for_status()
        rockets = rockets_response.json()

        rocket_names = {rocket['id']: rocket['name'] for rocket in rockets}

        # Prepare a list of tuples (rocket_name, count)
        rocket_launches = [
            (rocket_names[rocket_id], count)
            for rocket_id, count in launch_count.items()
            ]

        # Sort by number of launches (descending),
        # then by rocket name (ascending)
        rocket_launches.sort(key=lambda x: (-x[1], x[0]))

        # Print results
        for rocket, count in rocket_launches:
            print("{}: {}".format(rocket, count))

    except requests.RequestException as e:
        print(
            'An error occurred while making an API request: {}'.format(e))
    except Exception as err:
        print('A general error occurred: {}'.format(err))


if __name__ == '__main__':
    get_launches_per_rocket()
