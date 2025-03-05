import logging
import os

from services.spotify_service import SpotifyService
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    logging.info("Iniciando o processo de extração das TOP 50 Músicas do Spotify")

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    
    spotify_service = SpotifyService(client_id, client_secret)

    playlist_response = spotify_service.get_playlist_info("4HsVwfQ61BawbPdot6oWPc")

    if playlist_response is not None:
        print(playlist_response.json())

