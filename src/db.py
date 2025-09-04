import sqlite3 as sql
from pathlib import Path


class DbIncidents:
    def __init__(self) -> None:
        self.TABLE_PATH = Path(__file__).parent / "db_IT.db"
        self.TABLE_NAME = "incidents"

    def OpenConnection(self):
        self.connection = sql.connect(self.TABLE_PATH)
        self.cursor = self.connection.cursor()

    def CloseConnection(self):
        self.cursor.close()
        self.connection.close()


    def InsertName(self, name: str):
        self.OpenConnection()

        name = f" INSERT INTO {self.TABLE_NAME} (name) VALUES (?)"

        self.cursor.execute(name)
        self.connection.commit()

        self.CloseConnection()

    def InsertTicketNumber(self, ticket: str):
        self.OpenConnection()

        ticket = f"INSERT INTO {self.TABLE_NAME} (ticket_number) VALUES (?)"

        self.cursor.execute(ticket)
        self.connection.commit()

        self.CloseConnection()

    def ReadFile(self, path):
        with open(path, "rb") as file:
            return file.read()

    def InsertCheckList(self, CheckList):
        self.OpenConnection()

        CheckList = self.ReadFile(CheckList)

        self.cursor.execute(f"INSERT INTO {self.TABLE_NAME} (check_list) VALUES (?)", (CheckList))
        self.connection.commit()

        self.CloseConnection()
            
        


class DbTasks:
    def __init__(self) -> None:
        self.TABLE_PATH = Path(__file__).parent / "db_IT.db"
        self.TABLE_NAME = "tasks"

    def OpenConnection(self):
        self.connection = sql.connect(self.TABLE_PATH)
        self.cursor = self.connection.cursor()

    def CloseConnection(self):
        self.cursor.close()
        self.connection.close()

    def InsertName(self, name: str):
        self.OpenConnection()

        name = f" INSERT INTO {self.TABLE_NAME} (name) VALUES (?)"

        self.cursor.execute(name)
        self.connection.commit()

        self.CloseConnection()

    def InsertTicketNumber(self, ticket: str):
        self.OpenConnection()

        ticket = f"INSERT INTO {self.TABLE_NAME} (ticket_number) VALUES (?)"

        self.cursor.execute(ticket)
        self.connection.commit()

        self.CloseConnection()

    def ReadFile(self, path):
        with open(path, "rb") as file:
            return file.read()

    def InsertCheckList(self, CheckList):
        self.OpenConnection()

        CheckList = self.ReadFile(CheckList)

        self.cursor.execute(f"INSERT INTO {self.TABLE_NAME} (check_list) VALUES (?)", (CheckList))
        self.connection.commit()

        self.CloseConnection()

    

        

