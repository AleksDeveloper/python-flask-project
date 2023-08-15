import pytest
import sqlite3
from unittest.mock import patch
from dbutils.dbUtils import delete_registry
from model import User


@pytest.fixture
def mock_sqlite3_connect():
    with patch('sqlite3.connect') as mock_connect:
        connection_instance = mock_connect.return_value
        yield connection_instance


def test_delete_existing_registry(mock_sqlite3_connect):
    mock_cursor = mock_sqlite3_connect.cursor.return_value
    db = 'dbutils/test_db.db'
    #These must be existing values
    table = "existing_table"
    field = "valid_field"
    value = "existing_value"

    delete_registry(db, table, field, value)

    mock_sqlite3_connect.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once()
    mock_sqlite3_connect.commit.assert_called_once()
    mock_sqlite3_connect.close.assert_called_once()

def test_delete_nonexisting_registry(mock_sqlite3_connect, capsys):
    db = "nonexistingpath/nonexistingdb.db"
    table = "nonexistingtable"
    field = "nonexistingfield"
    value = "nonexistingvalue"

    delete_registry(db, table, field, value)
    assert "ERROR: " + str(sqlite3.Error)

if __name__ == '__main__':
    pytest.main()

