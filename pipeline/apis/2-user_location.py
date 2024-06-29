#!/usr/bin/env python3
'''
    This module returns the location of a user
    with a github api url.
'''
import requests
import sys
import time


def get_user_location(api_url):
    '''Returns the user's location'''
    response = requests.get(api_url)
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('location', 'Location not specified'))
    elif response.status_code == 403:
        reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
        reset= (reset_time - time.time()) / 60
        print('Reset in {} min'.format(reset))
    elif response.status_code == 404:
        print('Not found')
    else:
        print('Error: {}'.format(response.status_code))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./2-user_location.py <API_URL>')
    else: 
        get_user_location(sys.argv[1])
