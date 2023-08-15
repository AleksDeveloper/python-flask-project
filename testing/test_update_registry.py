from dataclasses import dataclass
import pytest
import sqlite3
from unittest.mock import patch
from dbutils.dbUtils import update_registry
from model import User


@pytest.fixture
def mock_sqlite3_connect():
    with patch('sqlite3.connect') as mock_connect:
        connection_instance = mock_connect.return_value
        yield connection_instance

@dataclass
class Registry:
    id: str
    user: str
    password: str
    worker: int
    student: int
    incomes: float


def test_update_existing_registry(mock_sqlite3_connect):
    mock_cursor = mock_sqlite3_connect.cursor.return_value
    db = 'dbutils/test_db.db'
    #These must be existing values
    table = "existing_table"
    where = "valid_existing_field"
    #Create obj from dataclass
    updated = Registry("1", "alex", "passwordalex", 0, 1, 2000322.12)

    update_registry(db, table, where, updated.id, updated)

    mock_sqlite3_connect.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once()
    mock_sqlite3_connect.commit.assert_called_once()
    mock_sqlite3_connect.close.assert_called_once()

def test_update_nonexisting_registry(mock_sqlite3_connect):
    db = "nonexistingpath/nonexistingdb.db"
    table = "nonexistingtable"
    where = "nonvalid_nonexisting_field"
    #Create obj from dataclass
    updated = Registry("1", "alex", "passwordalex", 0, 1, 2000322.12)

    update_registry(db, table, where, updated.id, updated)
    assert "ERROR: " + str(sqlite3.Error)

if __name__ == '__main__':
    pytest.main()

