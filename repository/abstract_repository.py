from abc import ABC, abstractmethod

class AbstractRepository(ABC):

    @abstractmethod
    def create_table_on_db(self):
        pass

    @abstractmethod
    def insert_record_on_db(self, obj):
        pass


    def execute_cursor(self, sql_query):
        cursor = self.db_conn.cursor()
        cursor.execute(sql_query)

        cursor.close()