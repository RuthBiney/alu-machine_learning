#!/usr/bin/env python3
import requests
import datetime

def get_upcoming_launch():
    url = 'https://api.spacexdata.com/v4/launches/upcoming'
    try:
        response = requests.get(url)
        response.raise_for_status()
        launches = response.json()
        
        # Sort launches by date_unix to get the soonest one
        upcoming_launch = sorted(launches, key=lambda x: x['date_unix'])[0]
        
        # Get rocket details
        rocket_id = upcoming_launch['rocket']
        rocket_response = requests.get(f'https://api.spacexdata.com/v4/rockets/{rocket_id}')
        rocket_response.raise_for_status()
        rocket = rocket_response.json()
        rocket_name = rocket['name']
        
        # Get launchpad details
        launchpad_id = upcoming_launch['launchpad']
        launchpad_response = requests.get(f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}')
        launchpad_response.raise_for_status()
        launchpad = launchpad_response.json()
        launchpad_name = launchpad['name']
        launchpad_locality = launchpad['locality']
        
        # Format date to local time
        date_local = datetime.datetime.strptime(upcoming_launch['date_local'], '%Y-%m-%dT%H:%M:%S%z')
        formatted_date = date_local.strftime('%Y-%m-%d %H:%M:%S %Z')

        # Print launch details in the required format
        print(f"{upcoming_launch['name']} ({formatted_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")
    
    except requests.RequestException as e:
        print(f'An error occurred while making an API request: {e}')
    except Exception as err:
        print(f'A general error occurred: {err}')

if __name__ == '__main__':
    get_upcoming_launch()
