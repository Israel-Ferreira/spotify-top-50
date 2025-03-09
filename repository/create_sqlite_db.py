import sqlite3

from repository.abstract_repository import AbstractRepository


def create_sqlite_database(name: str):
    return sqlite3.connect(name)


def create_tables(repositories: list[AbstractRepository]):
    for repo in repositories:
        repo.create_table_on_db()
