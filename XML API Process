LastFM API 
https://www.last.fm/api/show/artist.getInfo

import requests
import os

def get_artist_info(artist_name, api_key):
    """
    Fetches artist metadata from the Last.fm API.
    """
    url = "http://ws.audioscrobbler.com/2.0/"
    
    # Define the parameters for the API call
    params = {
        'method': 'artist.getinfo',
        'artist': artist_name,
        'api_key': api_key,
        'format': 'json'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Checks for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Usage
if __name__ == "__main__":
    # Best practice: Retrieve your key from an environment variable
    # Set this in your terminal with: export LASTFM_API_KEY='your_key_here'
    MY_API_KEY = os.getenv('LASTFM_API_KEY')
    
    if not MY_API_KEY:
        print("Error: Please set the LASTFM_API_KEY environment variable.")
    else:
        data = get_artist_info("Radiohead", MY_API_KEY)
        
        if "artist" in data:
            artist = data['artist']
            print(f"Artist: {artist['name']}")
            print(f"Listeners: {artist['stats']['listeners']}")
            print(f"Summary: {artist['bio']['summary']}")
        else:
            print("Could not find artist info.")
