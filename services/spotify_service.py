import requests
from base64 import b64encode

import logging



class SpotifyService:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret


    def login_oauth2(self):
        auth_basic_token_content =  str.encode(f"{self.client_id}:{self.client_secret}")
        auth_basic_token = b64encode(auth_basic_token_content).decode()

        spotify_token_url = 'https://accounts.spotify.com/api/token'

        headers = {
            "Authorization": f"Basic {auth_basic_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }


        payload =  {
            "grant_type": "client_credentials"
        }


        return  requests.post(spotify_token_url, data=payload, headers=headers)



        

    
    def get_playlist_info(self, playlist_id):
        auth_response = self.login_oauth2()

        if auth_response.status_code != 200:
            logging.error("Erro ao realizar a autenticação na API do SPOTIFY")
            return 
        
        auth_token =  auth_response.json()['access_token']

        get_playlist_url =  f"https://api.spotify.com/v1/playlists/{playlist_id}"

        headers =  {
            "Authorization": f"Bearer {auth_token}"
        }


        return requests.get(get_playlist_url,headers=headers)

