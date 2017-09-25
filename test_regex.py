import pytest

def myfunc():
    raise ValueError("Exception 123 raised")

# specify the regular expression to match - in this case '123' with spaces around
def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        myfunc()
