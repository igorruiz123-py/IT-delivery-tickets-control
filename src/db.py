import sqlite3 as sql
from pathlib import Path


class dbIncidents:
    def __init__(self) -> None:
        self.TABLE_PATH = Path(__file__).parent / "db_IT.db"
        self.TABLE_NAME = "incidents"

    def openConnection(self):
        self.connection = sql.connect(self.TABLE_PATH)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.cursor.close()
        self.connection.close()


class dbTasks:
    def __init__(self) -> None:
        self.TABLE_PATH = Path(__file__).parent / "db_IT.db"
        self.TABLE_NAME = "tasks"

    def openConnection(self):
        self.connection = sql.connect(self.TABLE_PATH)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.cursor.close()
        self.connection.close()

        

