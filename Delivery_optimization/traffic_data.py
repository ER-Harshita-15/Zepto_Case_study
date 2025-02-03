import requests
import json
from datetime import datetime

# Function to get real-time traffic data from an API
def get_traffic_data(api_url, api_key, location):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(f'{api_url}?location={location}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching traffic data: {response.status_code}")
        return None

# Function to analyze traffic data and suggest optimal routes
def analyze_traffic_data(traffic_data):
    optimal_routes = []
    for route in traffic_data['routes']:
        if route['traffic_condition'] == 'light':
            optimal_routes.append(route)
    return optimal_routes

# Function to adapt delivery routes based on traffic data
def adapt_delivery_routes(api_url, api_key, location):
    traffic_data = get_traffic_data(api_url, api_key, location)
    if traffic_data:
        optimal_routes = analyze_traffic_data(traffic_data)
        print(f"Optimal routes based on current traffic data: {optimal_routes}")
    else:
        print("No traffic data available to adapt delivery routes.")

if __name__ == "__main__":
    API_URL = 'https://api.trafficdata.com/v1/traffic'
    API_KEY = 'your_api_key_here'
    LOCATION = 'your_location_here'
    
    adapt_delivery_routes(API_URL, API_KEY, LOCATION)