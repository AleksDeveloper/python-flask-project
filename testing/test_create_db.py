import pytest
import sqlite3
from unittest.mock import patch
from dbutils.dbUtils import create_db
from model import User

@pytest.fixture
def mock_sqlite3_connect():
    with patch('sqlite3.connect') as mock_connect:
        connection_instance = mock_connect.return_value
        yield connection_instance



def test_create_valid_db(mock_sqlite3_connect):
    db = 'dbutils/test_db.db'

    create_db(db)

def test_create_invalid_db(mock_sqlite3_connect):
    db = 'nonexistingpath/non.valid.name.db'

    create_db(db)
    assert "ERROR: " + str(sqlite3.Error)

if __name__ == '__main__':
    pytest.main()
