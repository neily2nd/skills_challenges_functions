import pytest
from lib.make_snippet import *


def test_make_snippet():
    snippet = make_snippet("testing")
    assert snippet == "testi..."



def test_snip_type():
    
    with pytest.raises(Exception) as e:
        make_snippet(17)
    error = str(e.value)
    assert error == "Not a string"
    
    