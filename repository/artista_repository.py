import sqlite3

from repository.abstract_repository import AbstractRepository


class ArtistaRepository(AbstractRepository):

    def __init__(self, db_conn: sqlite3.Connection):
        self.db_conn = db_conn


    def insert_record_on_db(self, obj):
        cursor =  self.db_conn.cursor()

        sql_query = '''
        INSERT OR REPLACE INTO ARTISTA (Id, Nome) VALUES (?,?)
        '''

        cursor.execute(sql_query, (obj['id'], obj['name']))
        self.db_conn.commit()


    def create_table_on_db(self):
        sql_query =  """
        CREATE TABLE IF NOT EXISTS Artista (
            Id TEXT NOT NULL UNIQUE PRIMARY KEY,
            Nome VARCHAR(256) NOT NULL
        )
        """


        self.execute_cursor(sql_query)

        # cursor =  self.db_conn.cursor()
        # cursor.execute(sql_query)

        # cursor.close()

        
