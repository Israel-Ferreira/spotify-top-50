import sqlite3

from repository.abstract_repository import AbstractRepository


class PlaylistRepository(AbstractRepository):

    def __init__(self, db_conn: sqlite3.Connection):
        self.db_conn = db_conn


    def insert_record_on_db(self, obj):
        cursor = self.db_conn.cursor()

        playlist_id = obj["playlist_id"]
        title = obj["title"]

        sql_query = f'''
        INSERT INTO Playlist (Id, Titulo) VALUES (?,?)
        '''

        print(sql_query)

        cursor.execute(sql_query, (playlist_id,title))
        self.db_conn.commit()





    def create_table_on_db(self):
        sql_query =  """
        CREATE TABLE IF NOT EXISTS Playlist (
            Id TEXT NOT NULL UNIQUE  PRIMARY KEY,
            Titulo TEXT NOT NULL,
            Created_At TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            Updated_At TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """

        self.execute_cursor(sql_query)

        # cursor =  self.db_conn.cursor()
        # cursor.execute(sql_query)

        # cursor.close()

        
