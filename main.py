import logging
import os

from repository.create_sqlite_db import create_sqlite_database, create_tables
from repository.artista_repository import ArtistaRepository
from repository.playlist_repository import PlaylistRepository
from repository.musica_repository import MusicaRepository

from services.spotify_service import SpotifyService
from dotenv import load_dotenv


load_dotenv()


def create_playlist_on_db(api_response, playlist_repo):
    playlist_obj = {
        "playlist_id": api_response["id"],
        "title": api_response["name"]
    }

    playlist_repo.insert_record_on_db(playlist_obj)



def insert_artists_on_db(track_info, artist_repo):
    artists =  track_info['artists']

    for artist in artists:
        artist_repo.insert_record_on_db(artist)





if __name__ == "__main__":
    logging.info("Iniciando o processo de extração das TOP 100 Músicas do Spotify")

    conn = create_sqlite_database("spotify-top-50.db")


    artista_repo =  ArtistaRepository(conn)
    playlist_repo =  PlaylistRepository(conn)
    musica_repo =  MusicaRepository(conn)

    create_tables([artista_repo, playlist_repo, musica_repo])


    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    
    spotify_service = SpotifyService(client_id, client_secret)

    playlist_response = spotify_service.get_playlist_info("6UeSakyzhiEt4NB3UAd6NQ")


    if playlist_response is not None:
        api_response = playlist_response.json()


        items = api_response["tracks"]["items"]

        create_playlist_on_db(api_response, playlist_repo)

        for item in items:
            track =  item['track']
            artists =  track['artists']

            insert_artists_on_db(track, artista_repo)

            musica_repo.insert_record_on_db(track)





    






        
        



