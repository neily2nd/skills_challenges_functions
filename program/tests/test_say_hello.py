from lib.say_hello import *

def test_say_hello():
    new_say_hello = say_hello("kay")
    assert new_say_hello == "hello kay"