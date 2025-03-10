from repository.abstract_repository import AbstractRepository

import sqlite3

class MusicaRepository(AbstractRepository):

    def __init__(self, db_conn: sqlite3.Connection):
        self.db_conn = db_conn

    def insert_record_on_db(self, obj):
        cursor = self.db_conn.cursor()


        song_id = obj['id']
        isrc =  obj['external_ids']['isrc']

        song_name =  obj['name']

        duration =  int(obj['duration_ms']) / 1000


        artist_ids =  [artist["id"] for artist in obj['artists']]

        insert_music_sql =  '''
        INSERT OR REPLACE INTO Musica (Id, Isrc, Nome, Duracao_Em_Segundos, Is_Explicita)
        VALUES (?, ?, ?, ?, ?)
        '''


        cursor.execute(insert_music_sql, (song_id, isrc, song_name, duration, False))

        self.db_conn.commit()


        insert_song_to_artist_sql =  '''
        INSERT OR REPLACE INTO ArtistaMusica (MusicaId, ArtistaId) VALUES (?, ?)
        '''

        for artist_id in artist_ids:
            cursor.execute(insert_song_to_artist_sql, (song_id, artist_id))
            self.db_conn.commit()


        






    

    def create_table_on_db(self):
        music_table_sql =  """
        CREATE TABLE IF NOT EXISTS  Musica (
            Id TEXT NOT NULL UNIQUE PRIMARY KEY,
            Isrc TEXT NOT NULL UNIQUE,
            Nome TEXT NOT NULL,
            Duracao_Em_Segundos INTEGER NOT NULL,
            Is_Explicita BOOLEAN
        )
        """


        self.execute_cursor(music_table_sql)



        music_artist_assoc_table = """
        CREATE TABLE IF NOT EXISTS  ArtistaMusica (
            Id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
            MusicaId TEXT NOT NULL,
            ArtistaId TEXT NOT NULL,

            FOREIGN KEY (MusicaId) REFERENCES Musica(Id),
            FOREIGN KEY (ArtistaId) REFERENCES Playlist(Id)
        )
        """

        self.execute_cursor(music_artist_assoc_table)

        # cursor =  self.db_conn.cursor()
        # cursor.execute(sql_query)

        # cursor.close()

        