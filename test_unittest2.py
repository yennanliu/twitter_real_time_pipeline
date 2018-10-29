# python3 

from test_config import *

def test_db_setting():
    assert database == "ur DATABASE"
    assert schema == "ur SCHEMA"
    assert table == "ur TABLE"
    assert col == '"ur COL"'