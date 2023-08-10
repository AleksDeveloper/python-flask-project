import pytest
import sqlite3
from unittest.mock import patch
from dbutils.dbUtils import insert_full_table
from model import User

@pytest.fixture
def mock_sqlite3_connect():
    with patch('sqlite3.connect') as mock_connect:
        connection_instance = mock_connect.return_value
        yield connection_instance



def test_insert_full_table_valid_db_table(mock_sqlite3_connect):
    mock_cursor = mock_sqlite3_connect.cursor.return_value
    data = User('1', 'John Doe', 'johndoe', 'johndoe@gmail.com', 'johnpass', '1998-09-02', 'male')

    insert_full_table('dbutils/db1.db', 'users2', data)

    mock_sqlite3_connect.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once()
    mock_sqlite3_connect.commit.assert_called_once()
    mock_sqlite3_connect.close.assert_called_once()

def test_insert_full_table_invalid_db_table(mock_sqlite3_connect, capsys):
    data = User('1', 'John Doe', 'johndoe', 'johndoe@gmail.com', 'johnpass', '1998-09-02', 'male')

    insert_full_table('other.db', 'other_table', data)

    captured = capsys.readouterr()
    assert "THE DATABASE OR TABLE DOESN'T EXIST" in captured.out

if __name__ == '__main__':
    pytest.main()
