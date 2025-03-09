import logging
import os

from repository.create_sqlite_db import create_sqlite_database, create_tables
from repository.artista_repository import ArtistaRepository
from repository.playlist_repository import PlaylistRepository

from services.spotify_service import SpotifyService
from dotenv import load_dotenv



load_dotenv()


def create_playlist_on_db(api_response, playlist_repo):
    playlist_obj = {
        "playlist_id": api_response["id"],
        "title": api_response["name"]
    }

    playlist_repo.insert_record_on_db(playlist_obj)


    



if __name__ == "__main__":
    logging.info("Iniciando o processo de extração das TOP 50 Músicas do Spotify")

    conn = create_sqlite_database("spotify-top-50.db")


    artista_repo =  ArtistaRepository(conn)
    playlist_repo =  PlaylistRepository(conn)

    create_tables([artista_repo, playlist_repo])


    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    
    spotify_service = SpotifyService(client_id, client_secret)

    playlist_response = spotify_service.get_playlist_info("4HsVwfQ61BawbPdot6oWPc")


    if playlist_response is not None:
        api_response = playlist_response.json()

        create_playlist_on_db(api_response, playlist_repo)



    






        
        



