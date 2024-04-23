import pytest
from lib.manage_time import *

def test_time():
    
    answer = time(60, 50000)
    
    assert answer == f"You cannot complete this reading"