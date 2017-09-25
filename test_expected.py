import pytest

# expect a 0 divison error to be raised
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# retrieve the error message and check it has something about max recursion in there		
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)
	
# specify a custom failure message - and this test will fail to print it
def test_custom_msg():
    with pytest.raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
        pass

