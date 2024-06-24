#!/usr/bin/env python3
import requests
"""Fetches and returns a list of starships from the SWAPI"""

def availableShips(passengerCount):
    """
    Fetches and returns a list of starships from the SWAPI that can hold at least the given number of passengers.

    Args:
        passengerCount (int): The minimum number of passengers the ship must be able to hold.

    Returns:
        list: A list of starship names that can hold at least the given number of passengers. If no ship is available, returns an empty list.
    """
    ships = []
    url = 'https://swapi.dev/api/starships/'
    
    while url:
        response = requests.get(url)
        data = response.json()
        
        for ship in data['results']:
            # Clean the passengers field to handle large numbers with commas
            passengers = ship['passengers'].replace(',', '')
            
            # Check if the passengers field is a digit and if it meets the passenger count requirement
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship['name'])
        
        # Move to the next page, if available
        url = data['next']
    
    return ships

# Example usage:
if __name__ == "__main__":
    print(availableShips(100))
