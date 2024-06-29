#!/usr/bin/env python3
'''
Create a method that returns a list of
names of home planets of all sentient
species
'''


import requests


def sentientPlanets():
    '''
    Returns home planet list for
    sentient species
    '''

    planets = []

    try:
        url = "https://swapi-api.alx-tools.com/api/species/"

        while url:
            response = requests.get(url)

            data = response.json()
            species = data['results']

            for specie in species:
                if (
                    specie['designation'] == 'sentient'
                    or specie['classification'] == 'sentient'
                ):
                    homeworld_url = specie['homeworld']
                    if homeworld_url:
                        homeworld_response = requests.get(homeworld_url)
                        homeworld_response.raise_for_status()
                        homeworld_data = homeworld_response.json()
                        planets.append(homeworld_data['name'])

            url = data.get('next')

        return planets

    except requests.RequestException as e:
        print('An error occured: {}'.format(e))
    except Exception as err:
        print('A general error: {}'.format(err))
